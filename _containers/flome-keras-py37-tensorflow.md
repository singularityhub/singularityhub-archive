---
id: 9190
name: "flome/keras"
branch: "master"
tag: "py37-tensorflow"
commit: "95c2e75be14ea8fb71ac6e34be6bd4fc60eba7d4"
version: "4309ef931503c24dbd649c485fe3e383"
build_date: "2019-05-21T02:41:10.754Z"
size_mb: 6952
size: 3287257119
sif: "https://datasets.datalad.org/shub/flome/keras/py37-tensorflow/2019-05-21-95c2e75b-4309ef93/4309ef931503c24dbd649c485fe3e383.simg"
url: https://datasets.datalad.org/shub/flome/keras/py37-tensorflow/2019-05-21-95c2e75b-4309ef93/
recipe: https://datasets.datalad.org/shub/flome/keras/py37-tensorflow/2019-05-21-95c2e75b-4309ef93/Singularity
collection: flome/keras
---

# flome/keras:py37-tensorflow

```bash
$ singularity pull shub://flome/keras:py37-tensorflow
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:nvidia/cuda:9.0-cudnn7-devel-centos7

%environment
    export KERAS_BACKEND=tensorflow
    export PATH=/usr/local/cuda/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64

%post
    yum update -y
    yum install -y @"Development Tools"
    yum install -y epel-release
    yum install -y libgomp cmake3 vim cuda-9.0 cuda-drivers xorg-x11-drv-nvidia-cuda
    yum install -y git gcc-c++ sudo curl openblas lapack python36 wget python-devel python36-devel openssl-devel curl-devel
    wget https://bootstrap.pypa.io/get-pip.py
    python36 get-pip.py
    python2 get-pip.py
    python36 -m pip install tensorflow-gpu
    python36 -m pip install keras pillow
    python2 -m pip install tensorflow-gpu
    python2 -m pip install keras pillow

%runscript
exec $@
```

## Collection

 - Name: [flome/keras](https://github.com/flome/keras)
 - License: None

