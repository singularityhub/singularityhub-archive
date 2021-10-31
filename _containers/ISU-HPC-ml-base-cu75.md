---
id: 2602
name: "ISU-HPC/ml-base"
branch: "master"
tag: "cu75"
commit: "72a23302556d489b619ce3af3c3d8cef6c4a6d76"
version: "0293f93446282096bcf15b12ed98d4cc"
build_date: "2018-07-12T08:20:46.709Z"
size_mb: 2226
size: 1017749535
sif: "https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu75/2018-07-12-72a23302-0293f934/0293f93446282096bcf15b12ed98d4cc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/ml-base/cu75/2018-07-12-72a23302-0293f934/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ml-base/cu75/2018-07-12-72a23302-0293f934/Singularity
collection: ISU-HPC/ml-base
---

# ISU-HPC/ml-base:cu75

```bash
$ singularity pull shub://ISU-HPC/ml-base:cu75
```

## Singularity Recipe

```singularity
bootstrap:docker
From:nvidia/cuda:7.5-cudnn6-devel-centos7

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%environment

    LD_LIBRARY_PATH=/host-libs:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda-7.5/lib64:/usr/local/lib:/usr/local/lib64
    export LD_LIBRARY_PATH
    PATH=/usr/local/cuda-7.5/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
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

