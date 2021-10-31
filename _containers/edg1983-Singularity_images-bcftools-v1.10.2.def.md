---
id: 14541
name: "edg1983/Singularity_images"
branch: "master"
tag: "bcftools-v1.10.2.def"
commit: "f468b8d11ab886dddbb5aecaa3cd6983d3eeeaca"
version: "9bc153bc4699d74cc0c49b179447523fea12b45e6d294d821ec99facbed864e4"
build_date: "2020-10-02T15:48:11.512Z"
size_mb: 186.2265625
size: 195272704
sif: "https://datasets.datalad.org/shub/edg1983/Singularity_images/bcftools-v1.10.2.def/2020-10-02-f468b8d1-9bc153bc/9bc153bc4699d74cc0c49b179447523fea12b45e6d294d821ec99facbed864e4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/edg1983/Singularity_images/bcftools-v1.10.2.def/2020-10-02-f468b8d1-9bc153bc/
recipe: https://datasets.datalad.org/shub/edg1983/Singularity_images/bcftools-v1.10.2.def/2020-10-02-f468b8d1-9bc153bc/Singularity
collection: edg1983/Singularity_images
---

# edg1983/Singularity_images:bcftools-v1.10.2.def

```bash
$ singularity pull shub://edg1983/Singularity_images:bcftools-v1.10.2.def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/resources/ROH

%environment
    SHELL=/bin/bash
    PATH=$PATH:/usr/local/bin
    LC_ALL=C.UTF-8

%help
    Perform ROH detection with bcftools roh
    You will need chromosomes map files to be mounted in the container

%post
    apt-get update
    apt-get -y install apt-transport-https \
        build-essential \
        cmake \
        gcc \
        language-pack-en-base \
        libbz2-dev \
        libcurl4-openssl-dev \
        liblzma-dev \
        libncurses5-dev \
        libreadline-dev \
        libssl-dev \
        make \
        wget \
        zlib1g-dev \
        autoconf
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    
    ## Install bcftools ROH
    cd /opt/ && wget https://github.com/samtools/bcftools/releases/download/1.10.2/bcftools-1.10.2.tar.bz2
    tar -jxvf bcftools-1.10.2.tar.bz2
    rm bcftools-1.10.2.tar.bz2
    cd bcftools-1.10.2
    ./configure
    make
    make install
    cd htslib-1.10.2
    ./configure
    make
    make install
```

## Collection

 - Name: [edg1983/Singularity_images](https://github.com/edg1983/Singularity_images)
 - License: None

