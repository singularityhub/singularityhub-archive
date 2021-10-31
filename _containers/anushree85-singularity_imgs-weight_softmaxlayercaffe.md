---
id: 3120
name: "anushree85/singularity_imgs"
branch: "master"
tag: "weight_softmaxlayercaffe"
commit: "04bf6026adaab1b82bccc789dff47e5eb340fed1"
version: "1b97a790dba3fe27f50a04c576947855"
build_date: "2018-06-09T14:17:49.857Z"
size_mb: 2523
size: 1103548447
sif: "https://datasets.datalad.org/shub/anushree85/singularity_imgs/weight_softmaxlayercaffe/2018-06-09-04bf6026-1b97a790/1b97a790dba3fe27f50a04c576947855.simg"
url: https://datasets.datalad.org/shub/anushree85/singularity_imgs/weight_softmaxlayercaffe/2018-06-09-04bf6026-1b97a790/
recipe: https://datasets.datalad.org/shub/anushree85/singularity_imgs/weight_softmaxlayercaffe/2018-06-09-04bf6026-1b97a790/Singularity
collection: anushree85/singularity_imgs
---

# anushree85/singularity_imgs:weight_softmaxlayercaffe

```bash
$ singularity pull shub://anushree85/singularity_imgs:weight_softmaxlayercaffe
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with CUDA 7.5 and cuDNN 5.1 (and python)
  
BootStrap: docker
From: nvidia/cuda:7.5-cudnn5-devel-ubuntu14.04

%help
You're on your own.

%labels
Maintainer anushreephy@gmail.com
CUDA 7.5
cuDNN 5
OS Ubuntu14.04

%environment
    export CUDA_ROOT=/usr/local/cuda/
    export CUDA_HOME=/usr/local/cuda/
    export PATH=$PATH:/usr/local/NVIDIA-Linux-x86_64/:$CUDA_ROOT/bin
    export LD_LIBRARY_PATH=/usr/local/NVIDIA-Linux-x86_64/:$CUDA_ROOT/lib64

%post
    # not sure if they all are required?
    # following J. Simone here
    mkdir /scratch /data /project /lqcdproj
	##### INSTALL ALL DEPENDENCIES #####

    apt update && apt install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        git \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
	graphviz \
        python-dev \
        python-numpy \
        python-pip \
	python-pydot \
        python-setuptools \
        python-scipy \
	python-tk \
	rsync \
        software-properties-common \
        time \
        unzip \
        vim \
        zip \
        wget

    # clean after apt
    rm -rf /var/lib/apt/lists/* 
    
    ##### INSTALL NCLL #####

    #cd /opt/
    #git clone https://github.com/NVIDIA/nccl.git
    #cd nccl/
    #make
    #make install
    #cd ../
    #rm -rf nccl

    ##### INSTALL CAFFE #####

    # get Caffe source code (NO DANN included)
    cd /opt/
    # to avoid "Problem with the SSL CA cert (path? access rights?)"
    update-ca-certificates
    git clone -b weightsoftmax_caffe --depth 1 https://github.com/anushree85/caffe.git
    cd caffe/

    # install python packages for Caffe
    pip install --upgrade pip
    # during build from recipe file pip install ipython>=3.0.0 try to install
    # sed is added to force ipython < 6
    for req in $(cat python/requirements.txt | sed 's/ipython>=3.0.0/ipython>=3.0.0,<6/g') pydot
    do
        pip install $req
    done

    # make Caffe
    mkdir build
    cd build/
    #cmake -DUSE_CUDNN=1 -DUSE_NCCL=1 ..
    cmake -DUSE_CUDNN=1 ..
    make
    make pycaffe
    
%runscript
    exec /opt/caffe/build/tools/caffe
```

## Collection

 - Name: [anushree85/singularity_imgs](https://github.com/anushree85/singularity_imgs)
 - License: None

