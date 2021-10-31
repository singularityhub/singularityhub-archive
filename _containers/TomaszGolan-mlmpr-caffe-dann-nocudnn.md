---
id: 952
name: "TomaszGolan/mlmpr"
branch: "master"
tag: "caffe-dann-nocudnn"
commit: "6b2430ca11d6aa026754c70ee90ee3ccd4b46bbe"
version: "eb41bd713953cdfdc49a50917f202b2f"
build_date: "2017-11-28T19:11:34.666Z"
size_mb: 3830
size: 1880174623
sif: "https://datasets.datalad.org/shub/TomaszGolan/mlmpr/caffe-dann-nocudnn/2017-11-28-6b2430ca-eb41bd71/eb41bd713953cdfdc49a50917f202b2f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomaszGolan/mlmpr/caffe-dann-nocudnn/2017-11-28-6b2430ca-eb41bd71/
recipe: https://datasets.datalad.org/shub/TomaszGolan/mlmpr/caffe-dann-nocudnn/2017-11-28-6b2430ca-eb41bd71/Singularity
collection: TomaszGolan/mlmpr
---

# TomaszGolan/mlmpr:caffe-dann-nocudnn

```bash
$ singularity pull shub://TomaszGolan/mlmpr:caffe-dann-nocudnn
```

## Singularity Recipe

```singularity
# Ubuntu 16.04 based container with CUDA 8 and cuDNN 7 (and python)
# Prepared to run with https://github.com/TomaszGolan/caffe
# which is master Caffe fork with gradient scalar layer 
# see: https://github.com/gnperdue/caffe-1/compare/master...gnperdue:grad_rev_layer_gnp2017april?expand=1

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
    git clone --depth 1 https://github.com/TomaszGolan/caffe
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
    cmake -DUSE_CUDNN=0 -DUSE_NCCL=0 ..
    make

%runscript
    exec /opt/caffe/build/tools/caffe
```

## Collection

 - Name: [TomaszGolan/mlmpr](https://github.com/TomaszGolan/mlmpr)
 - License: None

