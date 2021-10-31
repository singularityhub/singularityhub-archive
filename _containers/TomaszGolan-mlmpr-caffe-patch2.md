---
id: 848
name: "TomaszGolan/mlmpr"
branch: "master"
tag: "caffe-patch2"
commit: "8e717bbdbf97dc2b3188f0a2a9cf9d16e843c0a7"
version: "0215e25c0225575cf88ab5f629a3475c"
build_date: "2017-11-20T13:56:11.981Z"
size_mb: 2346
size: 1007333407
sif: "https://datasets.datalad.org/shub/TomaszGolan/mlmpr/caffe-patch2/2017-11-20-8e717bbd-0215e25c/0215e25c0225575cf88ab5f629a3475c.simg"
url: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/caffe-patch2/2017-11-20-8e717bbd-0215e25c/
recipe: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/caffe-patch2/2017-11-20-8e717bbd-0215e25c/Singularity
collection: TomaszGolan/mlmpr
---

# TomaszGolan/mlmpr:caffe-patch2

```bash
$ singularity pull shub://TomaszGolan/mlmpr:caffe-patch2
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with CUDA 7 and cuDNN 3
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

