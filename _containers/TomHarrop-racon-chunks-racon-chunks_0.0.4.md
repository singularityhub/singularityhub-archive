---
id: 10805
name: "TomHarrop/racon-chunks"
branch: "master"
tag: "racon-chunks_0.0.4"
commit: "c7f63547de9fee1ffb9f69255d97f99b1d09b37d"
version: "35a9143b817dc2223f56085a9bc7b8da7f274ef802e1b66d106a565da07baf80"
build_date: "2019-10-11T23:54:35.038Z"
size_mb: 482.1171875
size: 505536512
sif: "https://datasets.datalad.org/shub/TomHarrop/racon-chunks/racon-chunks_0.0.4/2019-10-11-c7f63547-35a9143b/35a9143b817dc2223f56085a9bc7b8da7f274ef802e1b66d106a565da07baf80.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/racon-chunks/racon-chunks_0.0.4/2019-10-11-c7f63547-35a9143b/
recipe: https://datasets.datalad.org/shub/TomHarrop/racon-chunks/racon-chunks_0.0.4/2019-10-11-c7f63547-35a9143b/Singularity
collection: TomHarrop/racon-chunks
---

# TomHarrop/racon-chunks:racon-chunks_0.0.4

```bash
$ singularity pull shub://TomHarrop/racon-chunks:racon-chunks_0.0.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.04

%help
    Container for racon-chunks
    https://github.com/tomharrop/racon-chunks

    Python 3.7.3 with biopython 1.73
    samtools 1.9 using htslib 1.9
    bwa 0.7.17-r1188
    bbmap 38.45
    racon 1.3.2

%labels
    MAINTAINER "Tom Harrop"

%runscript
    exec /usr/local/bin/racon_chunks "$@"

%environment
    export PATH="${PATH}:/racon/build/bin"

%post
    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        bwa \
        cmake \
        default-jre \
        gawk \
        git \
        language-pack-en \
        libbz2-dev  \
        liblzma-dev \
        libncurses-dev \
        python3-pip \
        wget \
        zlib1g-dev 

    # python + biopython
    /usr/bin/pip3 install --upgrade pip
    /usr/local/bin/pip3 install \
        biopython==1.73

    # datrie
    /usr/bin/pip3 install \
        git+https://github.com/pytries/datrie.git@3e22a27ca0104fe3c62b3251c0b75c281f089e43

    # racon-chunks
    /usr/local/bin/pip3 \
        install \
        git+git://github.com/tomharrop/racon-chunks.git@v0.0.5

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
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.45.tar.gz"
    mkdir bbmap-install
    tar -zxf bbmap.tar.gz \
        -C bbmap-install \
        --strip-components 1
    cp -r bbmap-install/resources/* /
    cp -r bbmap-install/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap-install

    # racon
    mkdir racon
    wget -O "racon.tar.gz" \
        --no-check-certificate \
        https://github.com/isovic/racon/releases/download/1.3.2/racon-v1.3.2.tar.gz
    tar -zxf racon.tar.gz \
        -C racon \
        --strip-components 1

    cd racon || exit 1
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

