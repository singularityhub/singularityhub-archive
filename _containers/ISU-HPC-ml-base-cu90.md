---
id: 2600
name: "ISU-HPC/ml-base"
branch: "master"
tag: "cu90"
commit: "bdbe34f6f65f4a6d630ac9a0c1af0e472b7d8c6e"
version: "4d5a91f12bae28fc4181e981aa9aae22"
build_date: "2020-01-30T15:41:26.530Z"
size_mb: 3219
size: 1638592543
sif: "https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu90/2020-01-30-bdbe34f6-4d5a91f1/4d5a91f12bae28fc4181e981aa9aae22.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu90/2020-01-30-bdbe34f6-4d5a91f1/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu90/2020-01-30-bdbe34f6-4d5a91f1/Singularity
collection: ISU-HPC/ml-base
---

# ISU-HPC/ml-base:cu90

```bash
$ singularity pull shub://ISU-HPC/ml-base:cu90
```

## Singularity Recipe

```singularity
bootstrap:docker
From:nvidia/cuda:9.0-cudnn7-devel-centos7

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%environment

    LD_LIBRARY_PATH=/host-libs:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda-9.0/lib64:/usr/local/lib:/usr/local/lib64
    export LD_LIBRARY_PATH
    PATH=/usr/local/cuda-9.0/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
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
            boost-devel \
            tkinter \
            python36-tkinter
    yum clean all
    
    rm -rf /var/cache/yum

    curl https://bootstrap.pypa.io/get-pip.py | python36

    pip3 --no-cache-dir install --upgrade pip
    
    ln -s /usr/bin/python36 /usr/bin/python3
```

## Collection

 - Name: [ISU-HPC/ml-base](https://github.com/ISU-HPC/ml-base)
 - License: None

