---
id: 3444
name: "zhcf/caffe_singularity_images"
branch: "master"
tag: "latest"
commit: "dedc46a5e874ec109e4f077e12adf75d9337086f"
version: "6818e4fd1ff0911c54efba93524b02bd"
build_date: "2018-07-08T15:19:20.919Z"
size_mb: 3206
size: 1628778527
sif: "https://datasets.datalad.org/shub/zhcf/caffe_singularity_images/latest/2018-07-08-dedc46a5-6818e4fd/6818e4fd1ff0911c54efba93524b02bd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/zhcf/caffe_singularity_images/latest/2018-07-08-dedc46a5-6818e4fd/
recipe: https://datasets.datalad.org/shub/zhcf/caffe_singularity_images/latest/2018-07-08-dedc46a5-6818e4fd/Singularity
collection: zhcf/caffe_singularity_images
---

# zhcf/caffe_singularity_images:latest

```bash
$ singularity pull shub://zhcf/caffe_singularity_images:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

%post
    # remove cuda drivers
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
    git clone https://github.com/NVIDIA/nccl.git && cd nccl && make -j install && cd .. && rm -rf nccl
    mkdir build && cd build
    cmake -DUSE_CUDNN=1 -DUSE_NCCL=1 .. && \
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

