---
id: 6646
name: "arcsUVA/singularity-scripts"
branch: "master"
tag: "tensorflow-1.12.0-py27"
commit: "11924b108ba513b83aa424b3383ee313e3698f09"
version: "0fae53f9cba22575a384cc70bb094208"
build_date: "2019-01-28T22:35:36.583Z"
size_mb: 8454
size: 3703091231
sif: "https://datasets.datalad.org/shub/arcsUVA/singularity-scripts/tensorflow-1.12.0-py27/2019-01-28-11924b10-0fae53f9/0fae53f9cba22575a384cc70bb094208.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/singularity-scripts/tensorflow-1.12.0-py27/2019-01-28-11924b10-0fae53f9/
recipe: https://datasets.datalad.org/shub/arcsUVA/singularity-scripts/tensorflow-1.12.0-py27/2019-01-28-11924b10-0fae53f9/Singularity
collection: arcsUVA/singularity-scripts
---

# arcsUVA/singularity-scripts:tensorflow-1.12.0-py27

```bash
$ singularity pull shub://arcsUVA/singularity-scripts:tensorflow-1.12.0-py27
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-devel-ubuntu16.04


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    CUDA_MAJVERSION=9 # as of 2019-01-16 the tensorflow 1.12 wheel is built with cuda 9.0
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

    wget --quiet https://repo.continuum.io/archive/Anaconda2-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh
    /bin/bash ~/anaconda.sh -b -p /opt/conda
    rm ~/anaconda.sh

    conda update conda
#    conda install \
#        pyqt=5.6.0 \
#        spyder=3.3.2 \
#        qtconsole=4.3.1 \
#        qtpy=1.5.2 
    pip install --upgrade \
        pip \
        setuptools \
        argparse \
        msgpack

    # install tensorflow with gpu support
    pip install tensorflow-gpu==1.12

    # install tflearn
    pip install tflearn

    # install pytorch
    conda install pytorch=1.0 cuda${CUDA_MAJVERSION}${CUDA_MINVERSION} torchvision -c pytorch

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
    * Tensorflow 1.12.0 with Keras implementation
    * PyTorch 1.0
    * XGBoost
    * LightGBM
    * OpenCV
    * CUDA 9.0
    * CuDNN 7.4.1.5


%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH"
    export PATH="$CUDA_HOME/bin:$PATH"

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

 - Name: [arcsUVA/singularity-scripts](https://github.com/arcsUVA/singularity-scripts)
 - License: None

