---
id: 3151
name: "anushree85/singularity_imgs"
branch: "master"
tag: "caffe_md_ez"
commit: "8a670f49fe99ce7ed285fd6b471a5ffb622f38be"
version: "9aeaebbce86a691fe5146cddbd62aba4"
build_date: "2018-06-11T21:20:29.192Z"
size_mb: 2456
size: 1050058783
sif: "https://datasets.datalad.org/shub/anushree85/singularity_imgs/caffe_md_ez/2018-06-11-8a670f49-9aeaebbc/9aeaebbce86a691fe5146cddbd62aba4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/anushree85/singularity_imgs/caffe_md_ez/2018-06-11-8a670f49-9aeaebbc/
recipe: https://datasets.datalad.org/shub/anushree85/singularity_imgs/caffe_md_ez/2018-06-11-8a670f49-9aeaebbc/Singularity
collection: anushree85/singularity_imgs
---

# anushree85/singularity_imgs:caffe_md_ez

```bash
$ singularity pull shub://anushree85/singularity_imgs:caffe_md_ez
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with CUDA 7 and cuDNN 3 (and python)
  
BootStrap: docker
From: nvidia/cuda:7.0-cudnn3-devel-ubuntu14.04

%help
You're on your own.

%labels
Maintainer anushreephy@gmail.com
CUDA 7
cuDNN 3
OS Ubuntu14.04
cuda_driver unspecified

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
    git clone -b caffe_weighedsoftmax_new --depth 1 https://github.com/anushree85/caffe.git
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

