---
id: 3442
name: "zhcf/caffe_singularity_images"
branch: "master"
tag: "caffe1.0_cpu"
commit: "5c9210e65214467d72176f099c07c6ca6a13e461"
version: "3ea5229ba83f4111dcccc2dd48400ff9"
build_date: "2018-07-08T15:19:20.932Z"
size_mb: 1539
size: 558215199
sif: "https://datasets.datalad.org/shub/zhcf/caffe_singularity_images/caffe1.0_cpu/2018-07-08-5c9210e6-3ea5229b/3ea5229ba83f4111dcccc2dd48400ff9.simg"
url: https://datasets.datalad.org/shub/zhcf/caffe_singularity_images/caffe1.0_cpu/2018-07-08-5c9210e6-3ea5229b/
recipe: https://datasets.datalad.org/shub/zhcf/caffe_singularity_images/caffe1.0_cpu/2018-07-08-5c9210e6-3ea5229b/Singularity
collection: zhcf/caffe_singularity_images
---

# zhcf/caffe_singularity_images:caffe1.0_cpu

```bash
$ singularity pull shub://zhcf/caffe_singularity_images:caffe1.0_cpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
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
        python-scipy && \
    rm -rf /var/lib/apt/lists/*

%post
    cd /opt
    git clone -b 1.0 --depth 1 https://github.com/BVLC/caffe.git
    pip install -U pip~=9.0
    cd caffe/python
    for req in $(cat requirements.txt) pydot; do pip install $req; done
    cd ..
    mkdir build && cd build
    cmake -DCPU_ONLY=1 .. && \
    make -j"$(nproc)"

%environment
    PYTHONPATH=/opt/caffe/python:$PYTHONPATH
    PATH=/opt/caffe/build/tools:/opt/caffe/python:$PATH
    export PYTHONPATH PATH

%post
    echo "/opt/caffe/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig
```

## Collection

 - Name: [zhcf/caffe_singularity_images](https://github.com/zhcf/caffe_singularity_images)
 - License: None

