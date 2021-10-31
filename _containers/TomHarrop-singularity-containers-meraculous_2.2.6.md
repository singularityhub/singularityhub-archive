---
id: 4008
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "meraculous_2.2.6"
commit: "21208dbd98041732b2cf5826e4c3e4c34d361ccb"
version: "fc495f2c1532dae13e9003d3ac092b4d"
build_date: "2020-07-16T09:28:55.225Z"
size_mb: 1519
size: 427659295
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/meraculous_2.2.6/2020-07-16-21208dbd-fc495f2c/fc495f2c1532dae13e9003d3ac092b4d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/meraculous_2.2.6/2020-07-16-21208dbd-fc495f2c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/meraculous_2.2.6/2020-07-16-21208dbd-fc495f2c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:meraculous_2.2.6

```bash
$ singularity pull shub://TomHarrop/singularity-containers:meraculous_2.2.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    meraculous 2.2.6
    https://jgi.doe.gov/data-and-tools/meraculous/

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "meraculous 2.2.6"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        cmake \
        gcc-6 \
        g++-6 \
        gnuplot \
        language-pack-en \
        libgd-dev \
        libboost-dev \
        libboost-thread-dev \
        libboost-system-dev \
        libboost-filesystem-dev \
        liblog-log4perl-perl \
        make \
        perl \
        wget

    # download meraculous
    wget -O 'mer.tar.gz' \
        --no-check-certificate \
        'https://downloads.sourceforge.net/project/meraculous20/Meraculous-v2.2.6.tar.gz'
    mkdir mer
    tar -zxf mer.tar.gz \
        -C mer \
        --strip-components 1

    # build and install
    cd mer || exit 1
    mkdir build && cd build || exit 1
    export BOOST_ROOT=/usr/include/boost
    cmake \
        -DCMAKE_C_COMPILER=/usr/bin/gcc-6 \
        -DCMAKE_CXX_COMPILER=/usr/bin/g++-6 \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        ..
    make && make install

    # tidy up
    cd ../../ || exit 1
    rm -rf mer mer.tar.gz

%runscript

    exec /usr/local/bin/run_meraculous.sh "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

