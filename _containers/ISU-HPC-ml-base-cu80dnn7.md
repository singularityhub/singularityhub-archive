---
id: 2601
name: "ISU-HPC/ml-base"
branch: "master"
tag: "cu80dnn7"
commit: "aa68610e62fe4500417db54edb9866ab48427127"
version: "c212ea5f57b05da320cab6707a27a4db"
build_date: "2018-07-12T08:20:46.733Z"
size_mb: 2871
size: 1467379743
sif: "https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu80dnn7/2018-07-12-aa68610e-c212ea5f/c212ea5f57b05da320cab6707a27a4db.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu80dnn7/2018-07-12-aa68610e-c212ea5f/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu80dnn7/2018-07-12-aa68610e-c212ea5f/Singularity
collection: ISU-HPC/ml-base
---

# ISU-HPC/ml-base:cu80dnn7

```bash
$ singularity pull shub://ISU-HPC/ml-base:cu80dnn7
```

## Singularity Recipe

```singularity
bootstrap:docker
From:nvidia/cuda:8.0-cudnn7-devel-centos7

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%environment

    LD_LIBRARY_PATH=/host-libs:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda-8.0/lib64:/usr/local/lib:/usr/local/lib64
    export LD_LIBRARY_PATH
    PATH=/usr/local/cuda-8.0/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
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

