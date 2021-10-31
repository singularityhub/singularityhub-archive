---
id: 3544
name: "ResearchIT/singularity-keras"
branch: "master"
tag: "1"
commit: "eafa605c1826c91c8c362e15417ef038c8803eff"
version: "3d202cc9021b7d09b19f6d50682baf83"
build_date: "2018-07-14T18:00:14.414Z"
size_mb: 6020
size: 2777673759
sif: "https://datasets.datalad.org/shub/ResearchIT/singularity-keras/1/2018-07-14-eafa605c-3d202cc9/3d202cc9021b7d09b19f6d50682baf83.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/singularity-keras/1/2018-07-14-eafa605c-3d202cc9/
recipe: https://datasets.datalad.org/shub/ResearchIT/singularity-keras/1/2018-07-14-eafa605c-3d202cc9/Singularity
collection: ResearchIT/singularity-keras
---

# ResearchIT/singularity-keras:1

```bash
$ singularity pull shub://ResearchIT/singularity-keras:1
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
yum install -y git gcc-c++ sudo curl openblas lapack python36 wget python-devel python36-devel
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

 - Name: [ResearchIT/singularity-keras](https://github.com/ResearchIT/singularity-keras)
 - License: None

