---
id: 14881
name: "willgpaik/centos8_roar"
branch: "main"
tag: "latest"
commit: "21e47966461479c19054a6e459bbcb2bed6ae365"
version: "1d137e5fd92da3f71377eddba931d6b5"
build_date: "2021-03-24T20:32:44.461Z"
size_mb: 2845.0
size: 1026035743
sif: "https://datasets.datalad.org/shub/willgpaik/centos8_roar/latest/2021-03-24-21e47966-1d137e5f/1d137e5fd92da3f71377eddba931d6b5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/centos8_roar/latest/2021-03-24-21e47966-1d137e5f/
recipe: https://datasets.datalad.org/shub/willgpaik/centos8_roar/latest/2021-03-24-21e47966-1d137e5f/Singularity
collection: willgpaik/centos8_roar
---

# willgpaik/centos8_roar:latest

```bash
$ singularity pull shub://willgpaik/centos8_roar:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:8

%setup

%files

%environment
    export BOOST_ROOT=/usr/local/
    
%runscript

%post
    dnf install -y epel-release
    dnf install -y dnf-plugins-core
    dnf config-manager --set-enabled powertools
    dnf group install -y "Development Tools"
    dnf group install -y "Base"
    dnf install -y vim \
            git \
            cmake \
            gcc \
            gcc-c++ \
            gcc-gfortran \
            python2-devel \
            python2-pip \
            python38-devel \
            python38-pip \
            patch \
            openssl-devel \
            pcre-devel \
            mesa-libGL-devel \
            mesa-libGLU-devel \
            glibc-devel \
            Lmod \
            qt5-qtbase-devel \
            qt5-qtcharts-devel \
            qt5-qtsvg-devel \
            qt5-qtx11extras-devel \
            libX11-devel \
            libXpm-devel \
            libXft-devel \
            libXext-devel \
            gsl-devel \
            hdf5-devel \
            bzip2-devel \
            zlib-devel \
            libcurl-devel \
            ca-certificates \
            autoconf \
            tix \
            tk-devel \
            python2-tkinter \
            python38-tkinter \
            libxkbcommon-devel \
            libxkbcommon-x11 \
            readline-devel
    dnf -y install tix-devel python3-tkinter python38-tkinter \
            libxkbcommon-devel libxkbcommon-x11-devel \
            lapack-devel \
            blas-devel \
            openblas-devel \
            netcdf-devel \
            atlas-devel \
            libX11-devel \
            libXt-devel \
            xorg-x11-server-devel \
            xorg-x11-drv-evdev-devel \
            xz-devel
    dnf -y update
    
    # Make python 3.8 as default
    ln -sf /usr/bin/python3.8 /usr/bin/python3
    ln -sf /usr/bin/pip3.8 /usr/bin/pip3
    
    # Install CMake 3.19.7
    cd /tmp
    wget https://github.com/Kitware/CMake/releases/download/v3.19.7/cmake-3.19.7.tar.gz
    tar -xf cmake-3.19.7.tar.gz
    cd cmake-3.19.7
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf cmake-*
    
    # Install Boost 1.75.0
    cd /tmp/
    wget https://dl.bintray.com/boostorg/release/1.75.0/source/boost_1_75_0.tar.gz
    tar -xf boost_1_75_0.tar.gz
    cd boost_1_75_0
    ./bootstrap.sh
    ./b2 -j 2 install
    cd ..
    rm -rf boost_*
    
    # Install R 4.0.4
    cd /tmp
    wget https://cran.r-project.org/src/base/R-4/R-4.0.4.tar.gz
    tar -xf R-4.0.4.tar.gz
    cd R-4.0.4
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf R-*
```

## Collection

 - Name: [willgpaik/centos8_roar](https://github.com/willgpaik/centos8_roar)
 - License: None

