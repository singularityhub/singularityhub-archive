---
id: 13325
name: "TovRudyy/KapitanPOP"
branch: "master"
tag: "latest"
commit: "967280e91933bd302caa73bbfe9ce2ba4e5b0a58"
version: "14653b3b245be93b3423de9d0b0b13a9"
build_date: "2020-06-18T08:39:03.613Z"
size_mb: 1410.0
size: 452915231
sif: "https://datasets.datalad.org/shub/TovRudyy/KapitanPOP/latest/2020-06-18-967280e9-14653b3b/14653b3b245be93b3423de9d0b0b13a9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TovRudyy/KapitanPOP/latest/2020-06-18-967280e9-14653b3b/
recipe: https://datasets.datalad.org/shub/TovRudyy/KapitanPOP/latest/2020-06-18-967280e9-14653b3b/Singularity
collection: TovRudyy/KapitanPOP
---

# TovRudyy/KapitanPOP:latest

```bash
$ singularity pull shub://TovRudyy/KapitanPOP:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%labels
MAINTAINER TovRudyy

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/opt

%environment
    KAPITANPOP_HOME=/opt/KapitanPOP
    HDF5_HOME=/opt/hdf5-hdf5-1_12_0/install
    DASK_HOME=/opt/dask-2.18.1
    PATH=/opt/KapitanPOP:/opt/KapitanPOP/bin:/opt/dimemas-5.4.2-Linux_x86_64/bin:$PATH
    HDF5_USE_FILE_LOCKING=FALSE

%post
    # Basic OS packages
    apt-get update
    apt-get install -y build-essential python3 python3-pip python3-dev git wget vim
    ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip

    # Download & install HDF5-1.12.0
    cd /opt && wget -nv https://github.com/HDFGroup/hdf5/archive/hdf5-1_12_0.tar.gz
    tar -xf hdf5-1_12_0.tar.gz
    cd hdf5-hdf5-1_12_0 && mkdir -p build install
    HDF5_ROOT=/opt/hdf5-hdf5-1_12_0/install
    cd build
    ../configure --prefix=$HDF5_ROOT --enable-shared --enable-optimization=high
    make -j 4 install
    export HDF5_HOME=/opt/hdf5-hdf5-1_12_0/install

    # Donwload & install Dask master
    cd /opt && git clone https://github.com/dask/dask.git
    cd dask
    DASK_HOME=/opt/dask
    python -m pip install ".[complete]"

    # Download & install Dimemas
    cd /opt && wget -nv https://ftp.tools.bsc.es/dimemas/dimemas-5.4.2-Linux_x86_64.tar.bz2
    tar -xvf dimemas-5.4.2-Linux_x86_64.tar.bz2

    # Download & install KapitanPOP
    cd /opt && git clone https://github.com/TovRudyy/KapitanPOP.git
    cd KapitanPOP
    pip install -r requirements.txt
    mkdir -p obj bin
    make
    chmod +x kapitanPOP.py
```

## Collection

 - Name: [TovRudyy/KapitanPOP](https://github.com/TovRudyy/KapitanPOP)
 - License: None

