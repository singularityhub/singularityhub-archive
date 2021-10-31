---
id: 923
name: "TomaszGolan/mlmpr"
branch: "master"
tag: "vanilla-caffe"
commit: "7313d0e5454bd701784b4d31ec15bab877d71d14"
version: "1adc88fc9cf5ce4c23dae31a20018a87"
build_date: "2017-11-23T00:35:31.430Z"
size_mb: 3858
size: 1893077023
sif: "https://datasets.datalad.org/shub/TomaszGolan/mlmpr/vanilla-caffe/2017-11-23-7313d0e5-1adc88fc/1adc88fc9cf5ce4c23dae31a20018a87.simg"
url: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/vanilla-caffe/2017-11-23-7313d0e5-1adc88fc/
recipe: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/vanilla-caffe/2017-11-23-7313d0e5-1adc88fc/Singularity
collection: TomaszGolan/mlmpr
---

# TomaszGolan/mlmpr:vanilla-caffe

```bash
$ singularity pull shub://TomaszGolan/mlmpr:vanilla-caffe
```

## Singularity Recipe

```singularity
# Ubuntu 16.04 based container with CUDA 8 and cuDNN 7 (and python)

BootStrap: docker
From: nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04

%help
You're on your own.

%labels
Maintainer tomasz.golan@gmail.com
CUDA 8
cuDNN 7
OS Ubuntu16.04
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

    ##### INSTALL NCLL #####

    cd /opt/
    git clone https://github.com/NVIDIA/nccl.git
    cd nccl/
    make
    make install
    cd ../
    rm -rf nccl

    ##### INSTALL CAFFE #####

    # get Caffe source code (with DANN included)
    cd /opt/
    # to avoid "Problem with the SSL CA cert (path? access rights?)"
    update-ca-certificates
    git clone --depth 1 https://github.com/BVLC/caffe.git
    cd caffe

    # install python packages for Caffe
    pip install --upgrade pip
    for req in $(cat python/requirements.txt) pydot
    do
        pip install $req
    done

    # make Caffe
    mkdir build
    cd build/
    cmake -DUSE_CUDNN=1 -DUSE_NCCL=1 ..
    make

%runscript
    exec /opt/caffe/build/tools/caffe
```

## Collection

 - Name: [TomaszGolan/mlmpr](https://github.com/TomaszGolan/mlmpr)
 - License: None

