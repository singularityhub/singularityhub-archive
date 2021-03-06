---
id: 1102
name: "NuWro/builds"
branch: "master"
tag: "root5"
commit: "c78b6fb0667c2dfa39c4600748a6b3e551a52ff1"
version: "a59afa87fcab49e05918e7b554974b16"
build_date: "2017-12-20T18:05:20.636Z"
size_mb: 1388
size: 389926943
sif: "https://datasets.datalad.org/shub/NuWro/builds/root5/2017-12-20-c78b6fb0-a59afa87/a59afa87fcab49e05918e7b554974b16.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NuWro/builds/root5/2017-12-20-c78b6fb0-a59afa87/
recipe: https://datasets.datalad.org/shub/NuWro/builds/root5/2017-12-20-c78b6fb0-a59afa87/Singularity
collection: NuWro/builds
---

# NuWro/builds:root5

```bash
$ singularity pull shub://NuWro/builds:root5
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with ROOT 5 (with Pythia 6)
# used for NuWro builds to avoid compiling ROOT 5 every time 

BootStrap: docker
From: ubuntu:14.04

%labels
Maintainer tomasz.golan@gmail.com
OS Ubuntu14.04
ROOT 5.34/36

%environment
    export ROOTSYS=/opt/root/
    export PATH=$PATH:$ROOTSYS/bin/
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib/

%post
    ##### INSTALL ALL DEPENDENCIES #####

    apt update && apt install -y --no-install-recommends \
        binutils \
        ca-certificates \
        cmake \
        dpkg-dev \
        g++ \
        gcc \
        gfortran \
        git \
        graphviz-dev \
        libavahi-compat-libdnssd-dev \
        libfftw3-dev \
        libftgl-dev \
        libglew1.5-dev \
        libgsl0-dev \
        libkrb5-dev \
        libldap2-dev \
        libmysqlclient-dev \
        libpcre3-dev \
        libqt4-dev \
        libssl-dev \
        libx11-dev \
        libxext-dev \
        libxft-dev \
        libxml2-dev \
	libxml2-utils \
        libxpm-dev \
        python-dev \
        xlibmesa-glu-dev \
        wget

    # clean after apt
    rm -rf /var/lib/apt/lists/*

    # create g77 symbolic link for pythia installer
    ln -s /usr/bin/gfortran /usr/bin/g77
    
    ##### INSTALL ROOT with PYTHIA #####
    
    # get ROOT
    cd /opt/
    wget https://root.cern.ch/download/root_v5.34.36.source.tar.gz
    tar -zxf root_v5.34.36.source.tar.gz
    rm root_v5.34.36.source.tar.gz

    # get PYTHIA
    wget http://neutrino.ift.uni.wroc.pl/files/pythia6.tar.gz
    tar -zxf pythia6.tar.gz
    rm pythia6.tar.gz
    cd pythia6 && ./makePythia6.linux && cd ..
    mkdir root/lib
    mv pythia6/libPythia6.so root/lib
    rm -rf pythia6

    # compile ROOT
    cd root && ./configure --with-pythia6-libdir=lib --enable-builtin-freetype
    make
```

## Collection

 - Name: [NuWro/builds](https://github.com/NuWro/builds)
 - License: None

