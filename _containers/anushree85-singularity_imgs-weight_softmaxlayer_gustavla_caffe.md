---
id: 3117
name: "anushree85/singularity_imgs"
branch: "master"
tag: "weight_softmaxlayer_gustavla_caffe"
commit: "5881b3af618cca0fe7468082a48f0f1e5e1a5131"
version: "0fa6fffccd5be7bf585f1d6a961a0504"
build_date: "2018-06-08T18:30:25.933Z"
size_mb: 2523
size: 1103466527
sif: "https://datasets.datalad.org/shub/anushree85/singularity_imgs/weight_softmaxlayer_gustavla_caffe/2018-06-08-5881b3af-0fa6fffc/0fa6fffccd5be7bf585f1d6a961a0504.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/anushree85/singularity_imgs/weight_softmaxlayer_gustavla_caffe/2018-06-08-5881b3af-0fa6fffc/
recipe: https://datasets.datalad.org/shub/anushree85/singularity_imgs/weight_softmaxlayer_gustavla_caffe/2018-06-08-5881b3af-0fa6fffc/Singularity
collection: anushree85/singularity_imgs
---

# anushree85/singularity_imgs:weight_softmaxlayer_gustavla_caffe

```bash
$ singularity pull shub://anushree85/singularity_imgs:weight_softmaxlayer_gustavla_caffe
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

