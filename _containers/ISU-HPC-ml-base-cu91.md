---
id: 2599
name: "ISU-HPC/ml-base"
branch: "master"
tag: "cu91"
commit: "a64e27bfa3eebd2a2fad0bf1cef7c1d9db4dcb19"
version: "402cd6878653c1500480dab32b37edef"
build_date: "2018-07-31T22:10:06.268Z"
size_mb: 3222
size: 1645715487
sif: "https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu91/2018-07-31-a64e27bf-402cd687/402cd6878653c1500480dab32b37edef.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/ml-base/cu91/2018-07-31-a64e27bf-402cd687/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu91/2018-07-31-a64e27bf-402cd687/Singularity
collection: ISU-HPC/ml-base
---

# ISU-HPC/ml-base:cu91

```bash
$ singularity pull shub://ISU-HPC/ml-base:cu91
```

## Singularity Recipe

```singularity
bootstrap:docker
From:nvidia/cuda:9.1-cudnn7-devel-centos7

%environment

    LD_LIBRARY_PATH=/host-libs:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda-9.1/lib64:/usr/local/lib:/usr/local/lib64
    export LD_LIBRARY_PATH
    PATH=/usr/local/cuda-9.1/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
    export PATH
    PYTHONPATH=/usr/local:/usr/local/lib/python2.7/site-packages
    export PYTHONPATH

%post

    yum update -y

    yum install -y epel-release

        yum install -y \
            cmake \
            cuda-drivers \
            curl \
            git \
            freetype-devel \
            libpng-devel \
            openssl-devel \
            libXpm-devel \
            zeromq3-devel \
            module-init-tools \
            pkgconfig \
            python \
            python-devel \
            python-pip \
            python36 \
            python36-devel \
            rsync \
            unzip \
            zip \
            zlib-devel \
            vim \
            wget \
            java \
            pygtk2 \
            cmake3 \
            boost \
            boost-devel
    yum clean all
    rm -rf /var/cache/yum

    curl https://bootstrap.pypa.io/get-pip.py | python36

    pip3 --no-cache-dir install --upgrade pip
```

## Collection

 - Name: [ISU-HPC/ml-base](https://github.com/ISU-HPC/ml-base)
 - License: None

