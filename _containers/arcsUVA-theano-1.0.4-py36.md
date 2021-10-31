---
id: 8258
name: "arcsUVA/theano"
branch: "master"
tag: "1.0.4-py36"
commit: "f4b98e88e585250e8564e48601ed9fb585c9ba72"
version: "c99ca8ef0c6d49f4955de4b88c8f4f16"
build_date: "2019-04-05T22:25:26.949Z"
size_mb: 5910
size: 2604089375
sif: "https://datasets.datalad.org/shub/arcsUVA/theano/1.0.4-py36/2019-04-05-f4b98e88-c99ca8ef/c99ca8ef0c6d49f4955de4b88c8f4f16.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/theano/1.0.4-py36/2019-04-05-f4b98e88-c99ca8ef/
recipe: https://datasets.datalad.org/shub/arcsUVA/theano/1.0.4-py36/2019-04-05-f4b98e88-c99ca8ef/Singularity
collection: arcsUVA/theano
---

# arcsUVA/theano:1.0.4-py36

```bash
$ singularity pull shub://arcsUVA/theano:1.0.4-py36
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-devel-ubuntu16.04


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    CUDA_MAJVERSION=9 
    CUDA_MINVERSION=0
    CUDA_VERSION=${CUDA_MAJVERSION}.${CUDA_MINVERSION}
    CUDNN_VERSION=7.0.3.11   # Theano 1.0 requires cudnn >=v5 and <=v7.0
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
        libcudnn7-dev=${CUDNN_VERSION}-1+cuda${CUDA_VERSION} \
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
 
    # install Anaconda
    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh
    /bin/bash ~/anaconda.sh -b -p /opt/conda
    rm ~/anaconda.sh

    # update basic Anaconda packages
    conda update conda pandas
    pip install --upgrade \
        pip \
        setuptools \
        future

    # install Theano
    pip install \
        parameterized \
        pydot \
        scikit-cuda \
        nose \
        sphinx \
        Theano==1.0.4
    conda install -c conda-forge \
        pygpu=0.7.6

    # install Keras and Keras Visualization Toolkit
    pip install keras==2.2.4    
    pip install keras-vis
    
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
    * Theano 1.0.4
    * Keras 2.2.4
    * Keras-vis
    * OpenCV
    * CUDA 9.0
    * CuDNN 7.0


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

    export KERAS_BACKEND=theano
    export THEANO_FLAGS=device=cuda # use cuda device by default
```

## Collection

 - Name: [arcsUVA/theano](https://github.com/arcsUVA/theano)
 - License: None

