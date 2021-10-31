---
id: 11235
name: "TomHarrop/racon-chunks"
branch: "master"
tag: "racon-chunks_0.0.5"
commit: "8f3554ce92def0fce0a4ee4c6c222857605d45e4"
version: "71866b105a9bceeaf3b97da3cd00b82f9b0642770f9c09025b51000541c5bb0a"
build_date: "2020-01-08T20:29:25.712Z"
size_mb: 505.39453125
size: 529944576
sif: "https://datasets.datalad.org/shub/TomHarrop/racon-chunks/racon-chunks_0.0.5/2020-01-08-8f3554ce-71866b10/71866b105a9bceeaf3b97da3cd00b82f9b0642770f9c09025b51000541c5bb0a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/racon-chunks/racon-chunks_0.0.5/2020-01-08-8f3554ce-71866b10/
recipe: https://datasets.datalad.org/shub/TomHarrop/racon-chunks/racon-chunks_0.0.5/2020-01-08-8f3554ce-71866b10/Singularity
collection: TomHarrop/racon-chunks
---

# TomHarrop/racon-chunks:racon-chunks_0.0.5

```bash
$ singularity pull shub://TomHarrop/racon-chunks:racon-chunks_0.0.5
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
    racon 1.4.7

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

    # racon release
    # mkdir racon
    # wget -O "racon.tar.gz" \
    #     --no-check-certificate \
    #     https://github.com/lbcb-sci/racon/releases/download/1.4.7/racon-v1.4.7.tar.gz
    # tar -zxf racon.tar.gz \
    #     -C racon \
    #     --strip-components 1
    # cd racon || exit 1

    # racon master
    git clone --recursive \
        https://github.com/lbcb-sci/racon.git \
        /racon
    cd racon || exit 1
    git checkout ededb83

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

