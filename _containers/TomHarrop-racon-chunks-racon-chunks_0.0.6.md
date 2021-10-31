---
id: 11965
name: "TomHarrop/racon-chunks"
branch: "master"
tag: "racon-chunks_0.0.6"
commit: "26a27d768f862055340e0b429bd5ba75042006f2"
version: "8244ed1c1dc3591c516e2bc998673d9ba0e0a41d2d7d2a92078aade844eeeabc"
build_date: "2020-01-08T23:34:39.205Z"
size_mb: 475.8203125
size: 498933760
sif: "https://datasets.datalad.org/shub/TomHarrop/racon-chunks/racon-chunks_0.0.6/2020-01-08-26a27d76-8244ed1c/8244ed1c1dc3591c516e2bc998673d9ba0e0a41d2d7d2a92078aade844eeeabc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/racon-chunks/racon-chunks_0.0.6/2020-01-08-26a27d76-8244ed1c/
recipe: https://datasets.datalad.org/shub/TomHarrop/racon-chunks/racon-chunks_0.0.6/2020-01-08-26a27d76-8244ed1c/Singularity
collection: TomHarrop/racon-chunks
---

# TomHarrop/racon-chunks:racon-chunks_0.0.6

```bash
$ singularity pull shub://TomHarrop/racon-chunks:racon-chunks_0.0.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Container for racon-chunks
    https://github.com/tomharrop/racon-chunks

    Python 3.7.5 with biopython 1.73
    samtools 1.9 using htslib 1.9
    bwa 0.7.17-r1188
    bbmap 38.50b
    racon 1.4.10

%labels
    MAINTAINER "Tom Harrop"

%runscript
    exec /usr/local/bin/racon_chunks "$@"

%environment
    export PATH="${PATH}:/racon/build/bin"
    export LC_ALL=C
    
%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        bwa \
        cmake \
        default-jre \
        gawk \
        git \
        libbz2-dev  \
        liblzma-dev \
        libncurses-dev \
        python3-pip \
        wget \
        zlib1g-dev 

    # python + biopython + racon_chunks
    /usr/bin/pip3 install --upgrade pip
    /usr/local/bin/pip3 install \
        biopython==1.73 \
        git+git://github.com/tomharrop/racon-chunks.git@v0.0.6 \
        git+https://github.com/pytries/datrie.git@3e22a27ca0104fe3c62b3251c0b75c281f089e43
    update-alternatives \
        --install /usr/bin/python \
        python \
        /usr/bin/python3 \
        1

    # samtools
    mkdir htslib
    wget \
        -O "htslib.tar.bz2" \
        --no-check-certificate \
        https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
    tar -jxf htslib.tar.bz2 \
        -C htslib \
        --strip-components 1
    cd htslib || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf htslib.tar.bz2 htslib

    mkdir samtools
    wget \
        -O "samtools.tar.bz2" \
        --no-check-certificate \
        https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar -jxf samtools.tar.bz2 \
        -C samtools \
        --strip-components 1
    cd samtools || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf samtools.tar.bz2 samtools

    mkdir bcftools
    wget \
        -O "bcftools.tar.bz2" \
        --no-check-certificate \
        https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
    tar -jxf bcftools.tar.bz2 \
        -C bcftools \
        --strip-components 1
    cd bcftools || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf bcftools.tar.bz2 bcftools

    # bbmap
    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.50b.tar.gz"
    mkdir bbmap-install
    tar -zxf bbmap.tar.gz \
        -C bbmap-install \
        --strip-components 1
    cp -r bbmap-install/resources/* /
    cp -r bbmap-install/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap-install

    # racon master
    git clone \
        https://github.com/lbcb-sci/racon.git
    cd racon || exit 1
    git checkout 1.4.10
    git submodule update --init --recursive || true     # have to allow fail

    # build and install    
    mkdir build && cd build || exit 1
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -Dracon_build_tests=ON \
        -Dracon_build_wrapper=ON \
        ..
    make && make install
```

## Collection

 - Name: [TomHarrop/racon-chunks](https://github.com/TomHarrop/racon-chunks)
 - License: None

