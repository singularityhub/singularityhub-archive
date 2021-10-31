---
id: 1754
name: "mafreitas/singularity-openms"
branch: "master"
tag: "dependencies"
commit: "f3b59e040b4daeeba57cfccd412c3813b2078a19"
version: "8f582fcce456c7b595383d7c6ce57123"
build_date: "2018-02-17T22:08:52.898Z"
size_mb: 824
size: 249741343
sif: "https://datasets.datalad.org/shub/mafreitas/singularity-openms/dependencies/2018-02-17-f3b59e04-8f582fcc/8f582fcce456c7b595383d7c6ce57123.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mafreitas/singularity-openms/dependencies/2018-02-17-f3b59e04-8f582fcc/
recipe: https://datasets.datalad.org/shub/mafreitas/singularity-openms/dependencies/2018-02-17-f3b59e04-8f582fcc/Singularity
collection: mafreitas/singularity-openms
---

# mafreitas/singularity-openms:dependencies

```bash
$ singularity pull shub://mafreitas/singularity-openms:dependencies
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:trusty

%environment
LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH

%post
apt-get -y update
apt-get install -y --no-install-recommends --no-install-suggests g++ autoconf patch libtool make git g++ automake
apt-get install -y --no-install-recommends --no-install-suggests software-properties-common python-software-properties
apt-get clean
apt-get purge
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

add-apt-repository ppa:george-edison55/cmake-3.x
apt-get -y update
apt-get install -y cmake
apt-get clean
apt-get purge
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install build dependencies: qt, libsvm, glpk
apt-get -y update
apt-get install -y cmake
apt-get install -y --no-install-recommends --no-install-suggests qt4-dev-tools qt4-default qt4-qtconfig qt4-qmake
apt-get install -y --no-install-recommends --no-install-suggests libqt4-dev libqt4-opengl-dev libqt4-svg
apt-get install -y --no-install-recommends --no-install-suggests libqtwebkit4 libqtwebkit-dev
apt-get install -y --no-install-recommends --no-install-suggests libsvm-dev libglpk-dev libzip-dev zlib1g-dev libxerces-c-dev libbz2-dev
apt-get install -y --no-install-recommends --no-install-suggests libboost-date-time-dev \
                                 libboost-iostreams-dev \
                                 libboost-regex-dev \
                                 libboost-math-dev \
                                 libboost-random-dev
apt-get clean
apt-get purge
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```

## Collection

 - Name: [mafreitas/singularity-openms](https://github.com/mafreitas/singularity-openms)
 - License: None

