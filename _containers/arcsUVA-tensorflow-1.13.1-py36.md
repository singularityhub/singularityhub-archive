---
id: 9794
name: "arcsUVA/tensorflow"
branch: "master"
tag: "1.13.1-py36"
commit: "37e456e9bbf68075fac5e38bb593c9bbf87dd723"
version: "e6d8bf8e9858f4310206b1568d23cc36"
build_date: "2019-06-14T05:35:08.054Z"
size_mb: 8994
size: 3644137503
sif: "https://datasets.datalad.org/shub/arcsUVA/tensorflow/1.13.1-py36/2019-06-14-37e456e9-e6d8bf8e/e6d8bf8e9858f4310206b1568d23cc36.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/tensorflow/1.13.1-py36/2019-06-14-37e456e9-e6d8bf8e/
recipe: https://datasets.datalad.org/shub/arcsUVA/tensorflow/1.13.1-py36/2019-06-14-37e456e9-e6d8bf8e/Singularity
collection: arcsUVA/tensorflow
---

# arcsUVA/tensorflow:1.13.1-py36

```bash
$ singularity pull shub://arcsUVA/tensorflow:1.13.1-py36
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.0-devel-ubuntu16.04


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    CUDA_MAJVERSION=10 # tensorflow 1.13 wheel is built with cuda 10.0
    CUDA_MINVERSION=0
    CUDA_VERSION=${CUDA_MAJVERSION}.${CUDA_MINVERSION}
    CUDNN_VERSION=7.4.1.5
    apt-get -y update --fix-missing

    # install cuDNN and accessories
    apt-get install -y --no-install-recommends \
        build-essential \
        cuda-command-line-tools-${CUDA_MAJVERSION}-${CUDA_MINVERSION} \
        cuda-cublas-${CUDA_MAJVERSION}-${CUDA_MINVERSION} \
        cuda-cufft-${CUDA_MAJVERSION}-${CUDA_MINVERSION} \
        cuda-curand-${CUDA_MAJVERSION}-${CUDA_MINVERSION} \
        cuda-cusolver-${CUDA_MAJVERSION}-${CUDA_MINVERSION} \
        cuda-cusparse-${CUDA_MAJVERSION}-${CUDA_MINVERSION} \
        libcudnn7=${CUDNN_VERSION}-1+cuda${CUDA_VERSION} \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        software-properties-common \
        unzip

    # install other tools and dependencies
    apt-get -y install --allow-downgrades --no-install-recommends \
        dbus \
        wget \
        git \
        mercurial \
        subversion \
        vim \
        nano \
        cmake \
        bzip2 \
        ca-certificates \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1 \
        libboost-all-dev

    CMAKE_VERSION=3.14.4
    CMAKE_INSTALL_PATH=/opt/cmake/
    mkdir -p $CMAKE_INSTALL_PATH
    cd $CMAKE_INSTALL_PATH 
    wget https://github.com/Kitware/CMake/releases/download/v$CMAKE_VERSION/cmake-$CMAKE_VERSION.tar.gz
    tar xzf cmake-$CMAKE_VERSION.tar.gz
    mv cmake-$CMAKE_VERSION $CMAKE_VERSION
    cd $CMAKE_VERSION
    ./bootstrap
    make
    make install
    ls $CMAKE_INSTALL_PATH
    ls $CMAKE_INSTALL_PATH/$CMAKE_VERSION
    export PATH=$CMAKE_INSTALL_PATH/$CMAKE_VERSION/bin:$PATH
    export ACLOCAL_PATH=$CMAKE_INSTALL_PATH/$CMAKE_VERSION/share/aclocal:$ACLOCAL_PATH
    which cmake
    ls $CMAKE_INSTALL_PATH/$CMAKE_VERSION/bin

    # install TensorRT
    apt-get install nvinfer-runtime-trt-repo-ubuntu1604-5.0.2-ga-cuda${CUDA_VERSION}
    apt-get update
    apt-get install -y --no-install-recommends libnvinfer5=5.0.2-1+cuda${CUDA_VERSION}

    apt-get clean
    rm -rf /var/lib/apt/lists/*

#    locale-gen en_US
#    locale-gen en_US.UTF-8
#    locale update

#    system-machine-id-setup
    rm /etc/machine-id
    dbus-uuidgen --ensure=/etc/machine-id

    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH"
    export PATH="$CUDA_HOME/bin:$PATH"
    export PATH="/opt/conda/bin:$PATH"
 
    # required for LightGBM
    mkdir -p /etc/OpenCL/vendors && \
    echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd
    
    export BOOST_ROOT=/usr/local/boost

    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh
    /bin/bash ~/anaconda.sh -b -p /opt/conda
    rm ~/anaconda.sh

    conda update conda pandas
#    conda install \
#        pyqt=5.6.0 \
#        msgpack-python
#        spyder=3.3.2 \
#        qtconsole=4.3.1 \
#        qtpy=1.5.2 
    pip install --upgrade \
        pip \
        setuptools \
        future \
        pydot

    # install tensorflow with gpu support
    pip install tensorflow-gpu==1.13.1

    # install tflearn
    pip install tflearn

    # install xgboost
    cd /opt
    # wget https://github.com/dmlc/xgboost/archive/v0.80.tar.gz
    # tar xzf v0.80.tar.gz
    # rm v0.80.tar.gz
    # mv xgboost-0.80 xgboost    
    git clone --recursive https://github.com/dmlc/xgboost
    cd xgboost
    mkdir build
    cd build
    cmake .. -DUSE_CUDA=ON
    make -j4 

    cd ../python-package
    python setup.py install

    # install lightgbm
    cd /opt
    git clone --recursive https://github.com/Microsoft/LightGBM
    cd LightGBM
    mkdir build
    cd build
    cmake -DUSE_GPU=1 -DOpenCL_LIBRARY=$CUDA_HOME/lib64/libOpenCL.so -DOpenCL_INCLUDE_DIR=$CUDA_HOME/include/ ..
    make -j4

    cd ../python-package
    python setup.py install --gpu --precompile

    # install OpenCV
    pip install opencv-python

    conda clean --index-cache --tarballs --packages --yes

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
exec python $@

%help
This container is backed by Anaconda version 5.2.0 and provides the Python 3.6 bindings for:
    * Tensorflow 1.13.1 with Keras implementation
    * XGBoost
    * LightGBM
    * OpenCV
    * CUDA 10.0
    * CuDNN 7.4.1.5


%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH"
    export PATH="$CUDA_HOME/bin:$PATH"

    export PATH=/opt/cmake/3.14.4:$PATH

    export PATH="/opt/conda/bin:$PATH"
    unset CONDA_DEFAULT_ENV
    export ANACONDA_HOME=/opt/conda
    
    XGBOOSTROOT=/opt/xgboost
    export CPATH="$XGBOOSTROOT/include:$CPATH"
    export LD_LIBRARY_PATH="$XGBOOSTROOT/lib:$LD_LIBRARY_PATH"
    export PATH="$XGBOOSTROOT:$PATH"
    export PYTHONPATH=$XGBOOSTROOT/python-package:$PYTHONPATH

    LIGHTGBMROOT=/opt/LightGBM
    export CPATH="$LIGHTGBMROOT/include:$CPATH"
    export LD_LIBRARY_PATH="$LIGHTGBMROOT:$LD_LIBRARY_PATH"
    export PATH="$LIGHTGBMROOT:$PATH"
    export PYTHONPATH=$LIGHTGBMROOT/python-package:$PYTHONPATH
```

## Collection

 - Name: [arcsUVA/tensorflow](https://github.com/arcsUVA/tensorflow)
 - License: None

