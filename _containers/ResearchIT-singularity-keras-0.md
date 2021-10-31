---
id: 3414
name: "ResearchIT/singularity-keras"
branch: "master"
tag: "0"
commit: "2914728b710d7538443fc3503e9b04c6ca08a12b"
version: "e78530c8b8c562ef8573ebb423f638e1"
build_date: "2018-07-05T21:26:03.948Z"
size_mb: 4551
size: 2202640415
sif: "https://datasets.datalad.org/shub/ResearchIT/singularity-keras/0/2018-07-05-2914728b-e78530c8/e78530c8b8c562ef8573ebb423f638e1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/singularity-keras/0/2018-07-05-2914728b-e78530c8/
recipe: https://datasets.datalad.org/shub/ResearchIT/singularity-keras/0/2018-07-05-2914728b-e78530c8/Singularity
collection: ResearchIT/singularity-keras
---

# ResearchIT/singularity-keras:0

```bash
$ singularity pull shub://ResearchIT/singularity-keras:0
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
yum install -y git gcc-c++ sudo curl openblas lapack python36 wget
wget https://bootstrap.pypa.io/get-pip.py
python36 get-pip.py
python36 -m pip install tensorflow-gpu
python36 -m pip install keras pillow

%runscript
#exec th "$@"
```

## Collection

 - Name: [ResearchIT/singularity-keras](https://github.com/ResearchIT/singularity-keras)
 - License: None

