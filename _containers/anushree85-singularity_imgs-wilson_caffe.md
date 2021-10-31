---
id: 2992
name: "anushree85/singularity_imgs"
branch: "master"
tag: "wilson_caffe"
commit: "3f1af35fde1d998b564d0108dd64568ee26c2cd8"
version: "d02e1258e03b67d083ae9f52ee153355"
build_date: "2018-05-30T12:30:56.355Z"
size_mb: 4432
size: 2067615775
sif: "https://datasets.datalad.org/shub/anushree85/singularity_imgs/wilson_caffe/2018-05-30-3f1af35f-d02e1258/d02e1258e03b67d083ae9f52ee153355.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/anushree85/singularity_imgs/wilson_caffe/2018-05-30-3f1af35f-d02e1258/
recipe: https://datasets.datalad.org/shub/anushree85/singularity_imgs/wilson_caffe/2018-05-30-3f1af35f-d02e1258/Singularity
collection: anushree85/singularity_imgs
---

# anushree85/singularity_imgs:wilson_caffe

```bash
$ singularity pull shub://anushree85/singularity_imgs:wilson_caffe
```

## Singularity Recipe

```singularity
#
# Ubuntu ML container
#

BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04
IncludeCmd: false

%labels

Maintainer J.Simone
Date: 2017-10-27
cuda_driver unspecified

%help

A portable Ubuntu 16.04 environment with pre-built caffe.

%environment
    # set these environment variables
    export CUDA_ROOT=/usr/local/cuda
    export CUDA_HOME=/usr/local/cuda
    export PATH=$PATH:$CUDA_ROOT/bin
    export LD_LIBRARY_PATH=$CUDA_ROOT/lib64

%runscript
    # Check the current environment
    chk_nvidia_uvm=$(grep nvidia_uvm /proc/modules)
    if [ -z "$chk_nvidia_uvm" ]; then
      echo "Problem detected on the host: the Linux kernel module nvidia_uvm is not loaded"
    fi
    exec /bin/bash

%setup
    # Runs from outside the container during Bootstrap
    workdir=$(pwd)

%post
    # Runs within the container during Bootstrap

    # make lqcd filesystem mount points
    mkdir /scratch /data /project /lqcdproj

    # Set up some required environment defaults
    export LC_ALL=C
    export CUDA_HOME=/usr/local/cuda
    export CUDA_ROOT=/usr/local/cuda
    export PATH=/bin:/sbin:/usr/bin:/usr/sbin:${CUDA_HOME}/bin:$PATH
    export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${CUDA_HOME}/extras/CUPTI/lib64

    # Install the necessary packages (from repo)
    apt-get update && apt-get install -y --no-install-recommends \
      autoconf \
      automake \
      bc \
      cmake \
      curl \
      g++ \
      gfortran \
      git \
      libatlas-base-dev \
      libatlas3-base \
      libblas-dev \
      libboost-all-dev \
      libcupti-dev \
      libcurl4-openssl-dev \
      libffi-dev \
      libfreetype6-dev \
      libgflags-dev \
      libgoogle-glog-dev \
      libgraphviz-dev \
      libhdf5-serial-dev \
      libibverbs-dev \
      libjpeg-dev \
      libleveldb-dev \
      liblcms2-dev \
      liblapack-dev \
      liblapacke-dev \
      liblmdb-dev \
      libopenblas-dev \
      libopenmpi-dev \
      libopencv-dev \
      libprotobuf-dev \
      libpng-dev \
      libsnappy-dev \
      libssl-dev \
      libxml2-dev \
      libtiff5-dev \
      libwebp-dev \
      libzmq3-dev \
      pkg-config \
      protobuf-compiler \
      graphviz \
      python-dev \
      python-pip \
      python-pydot \
      python-setuptools \
      python-tk \
      rsync \
      software-properties-common \
      time \
      unzip \
      vim \
      zip \
      wget \
      zlib1g-dev
    apt-get clean && \
      apt-get autoremove && \
      rm -rf /var/lib/apt/lists/*

    # Update to the latest pip (newer than repo)
    pip install --no-cache-dir --upgrade pip==9.0.3
    pip install -U setuptools
    # Install other needed packages
    pip install --no-cache-dir --upgrade \
      chardet \
      Cheetah \
      Cython \
      deepdish \
      future \
      h5py \
      ipykernel \
      jupyter \
      leveldb \
      lmdb \
      Mako \
      matplotlib \
      ndg-httpsclient \
      nose \
      numpy \
      pandas \
      path.py \
      Pillow \
      pyasn1 \
      pygments \
      pyopenssl \
      python-dateutil \
      python-gflags \
      pyyaml \
      requests \
      scipy \
      scikit-image \
      scikit-learn \
      six \
      sqlalchemy \
      sympy \
      urllib3 \
      virtualenv \
      wheel \
      zmq

    # libgpuarray with python binding
    git clone https://github.com/Theano/libgpuarray.git
    sdir=`pwd`
    cd libgpuarray && \
      mkdir Build && \
      cd Build && \
      cmake .. -DCMAKE_BUILD_TYPE=Release && \
      make && \
      make install && \
      cd .. && \
      python2.7 setup.py install && \
      cd $sdir && \
      rm -rf libgpuarray
    /sbin/ldconfig


    # pyCUDA
    ( cd /tmp && \
      wget https://pypi.python.org/packages/b3/30/9e1c0a4c10e90b4c59ca7aa3c518e96f37aabcac73ffe6b5d9658f6ef843/pycuda-2017.1.1.tar.gz#md5=9e509f53a23e062b31049eb8220b2e3d && \
      tar xf pycuda-2017.1.1.tar.gz && \
      cd pycuda-2017.1.1 && \
      python configure.py --cuda-root=${CUDA_HOME} --cudadrv-lib-dir=${NV_DRIVER_ROOT} && \
      make install \
    )

    # Caffe master branch
    #
    ( mkdir -p /usr/local/caffe/source && \
        git clone -b master --depth 1 https://github.com/BVLC/caffe.git /usr/local/caffe/source && \
        cd /usr/local/caffe/source && \
        cat python/requirements.txt | xargs -n1 pip install && \
        mkdir build && cd build && \
        git clone https://github.com/NVIDIA/nccl.git && cd nccl && make -j install && cd .. && rm -rf nccl && \
        cmake -DCMAKE_INSTALL_PREFIX=/usr/local/caffe -DUSE_CUDNN=1 -DUSE_NCCL=1 -DCUDA_ARCH_NAME="Manual" -DCUDA_ARCH_BIN="30 35 50 60 61" .. && \
        make all && \
        make install \
    )

    /sbin/ldconfig

%test
# Sanity check that the container is operating
#
# nosetests /usr/local/caffe/source/python
# nosetests
```

## Collection

 - Name: [anushree85/singularity_imgs](https://github.com/anushree85/singularity_imgs)
 - License: None

