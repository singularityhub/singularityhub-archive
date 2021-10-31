---
id: 853
name: "TomaszGolan/mlmpr"
branch: "master"
tag: "pycaffe-patch2"
commit: "4b8f5e065542b28b7de6cd8b93161290e5130f8c"
version: "5d5d968075e94e373eba2b5532d807c7"
build_date: "2017-11-20T13:56:11.972Z"
size_mb: 2723
size: 1138798623
sif: "https://datasets.datalad.org/shub/TomaszGolan/mlmpr/pycaffe-patch2/2017-11-20-4b8f5e06-5d5d9680/5d5d968075e94e373eba2b5532d807c7.simg"
url: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/pycaffe-patch2/2017-11-20-4b8f5e06-5d5d9680/
recipe: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/pycaffe-patch2/2017-11-20-4b8f5e06-5d5d9680/Singularity
collection: TomaszGolan/mlmpr
---

# TomaszGolan/mlmpr:pycaffe-patch2

```bash
$ singularity pull shub://TomaszGolan/mlmpr:pycaffe-patch2
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with CUDA 7 and cuDNN 3 (and python)
# Prepared to run with https://github.com/sohiniu/caffe/tree/patch-2
# see https://hub.docker.com/r/nvidia/cuda/ for more up to date dockers

BootStrap: docker
From: nvidia/cuda:7.0-cudnn3-devel-ubuntu14.04

%help
You're on your own.

%labels
Maintainer tomasz.golan@gmail.com
CUDA 7
cuDNN 3
OS Ubuntu14.04
NVIDIA-DRIVER 375.26

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
        python-dev \
        python-numpy \
        python-pip \
        python-setuptools \
        python-scipy \
        wget

    # clean after apt
    rm -rf /var/lib/apt/lists/*

    ##### INSTALL NVIDIA DRIVERS #####
    
    # get NVIDIA drivers
    cd /opt/
    wget http://us.download.nvidia.com/XFree86/Linux-x86_64/375.26/NVIDIA-Linux-x86_64-375.26.run
    # extract .run file to /usr/local/
    sh NVIDIA-Linux-x86_64-375.26.run -x
    mv NVIDIA-Linux-x86_64-375.26 /usr/local/NVIDIA-Linux-x86_64
    rm NVIDIA-Linux-x86_64-375.26.run
    
    # create symbolic links
    cd /usr/local/NVIDIA-Linux-x86_64
    for n in *.375.26; do
        ln -v -s $n ${n%.375.26}
    done
    ln -v -s libnvidia-ml.so.375.26 libnvidia-ml.so.1
    ln -v -s libcuda.so.375.26 libcuda.so.1

    ##### INSTALL CAFFE #####

    # get Caffe source code (with Sohini's patch v2)
    cd /opt/
    # to avoid "Problem with the SSL CA cert (path? access rights?)"
    update-ca-certificates
    git clone -b patch-2 --depth 1 https://github.com/sohiniu/caffe.git
    cd caffe

    # install python packages for Caffe
    pip install --upgrade pip
    # during build from recipe file pip install ipython>=1.1.0 try to install
    # ipython v6 which is incompatible with python version
    # sed is added to force ipython < 6
    for req in $(cat python/requirements.txt | sed 's/ipython>=1.1.0/ipython>=1.1.0,<6/g') pydot
    do
        pip install $req
    done

    # make Caffe
    # NOTE: in the future we may want -DUSE_NCCL=1
    mkdir build
    cd build/
    cmake -DUSE_CUDNN=1 ..
    make

%runscript
    exec /opt/caffe/build/tools/caffe
```

## Collection

 - Name: [TomaszGolan/mlmpr](https://github.com/TomaszGolan/mlmpr)
 - License: None

