---
id: 6677
name: "arcsUVA/tensorflow"
branch: "master"
tag: "1.6.0-py27"
commit: "80ade668b28d44770a9f37540aef895d69b38456"
version: "d60067b8acd68258b309f41b7086d323"
build_date: "2019-04-12T04:45:45.551Z"
size_mb: 8668
size: 3928473631
sif: "https://datasets.datalad.org/shub/arcsUVA/tensorflow/1.6.0-py27/2019-04-12-80ade668-d60067b8/d60067b8acd68258b309f41b7086d323.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/tensorflow/1.6.0-py27/2019-04-12-80ade668-d60067b8/
recipe: https://datasets.datalad.org/shub/arcsUVA/tensorflow/1.6.0-py27/2019-04-12-80ade668-d60067b8/Singularity
collection: arcsUVA/tensorflow
---

# arcsUVA/tensorflow:1.6.0-py27

```bash
$ singularity pull shub://arcsUVA/tensorflow:1.6.0-py27
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-devel-ubuntu16.04


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    CUDNN_VERSION=7.0.5.15
    apt-get -y update --fix-missing

    # install cuDNN version 7.0.5 required for keras
    apt-get install -y --no-install-recommends \
        libcudnn7=$CUDNN_VERSION-1+cuda9.0 \
        libcudnn7-dev=$CUDNN_VERSION-1+cuda9.0 && \
    rm -rf /var/lib/apt/lists/*
    apt-get -y update

    # install other dependencies
    apt-get -y install --allow-downgrades --no-install-recommends \
        build-essential \
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

#    locale-gen en_US
#    locale-gen en_US.UTF-8
#    locale update

#    system-machine-id-setup
    rm /etc/machine-id
    dbus-uuidgen --ensure=/etc/machine-id

    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"
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
    conda install \
        numpy=1.15 \
        pyqt=5.6.0 \
        spyder==3.2.6 \
        qtconsole==4.3.1 \
        qtpy==1.3.1
    pip install --upgrade pip

    # install tensorflow with gpu support
    pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.6.0-cp27-none-linux_x86_64.whl

    # install tflearn
    pip install tflearn

    # install keras
    pip install keras==2.2.4
    pip install keras-vis  # requires numpy 1.15

    # install pytorch
    conda install pytorch=0.4.0 torchvision -c pytorch

    # install xgboost
    cd /opt
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
This container is backed by Anaconda version 5.2.0 and provides the Python 2.7 bindings for:
    * Tensorflow 1.6.0
    * Keras 2.2.4
    * Keras Visualization Toolkit
    * PyTorch 0.4.0
    * XGBoost
    * LightGBM
    * OpenCV
    * CUDA 9.0
    * CuDNN 7.0.5.15


%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"
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

 - Name: [arcsUVA/tensorflow](https://github.com/arcsUVA/tensorflow)
 - License: None

