---
id: 14797
name: "edg1983/Singularity_images"
branch: "master"
tag: "hapcut2.def"
commit: "85f26be1c0a2aaec4d4eba251bcf1f24da53987f"
version: "c4fbd7f59a48376b88c031973e37769dafcb9dd0cb109881741497d4c19f7fdd"
build_date: "2020-11-02T10:32:54.635Z"
size_mb: 196.96875
size: 206536704
sif: "https://datasets.datalad.org/shub/edg1983/Singularity_images/hapcut2.def/2020-11-02-85f26be1-c4fbd7f5/c4fbd7f59a48376b88c031973e37769dafcb9dd0cb109881741497d4c19f7fdd.sif"
url: https://datasets.datalad.org/shub/edg1983/Singularity_images/hapcut2.def/2020-11-02-85f26be1-c4fbd7f5/
recipe: https://datasets.datalad.org/shub/edg1983/Singularity_images/hapcut2.def/2020-11-02-85f26be1-c4fbd7f5/Singularity
collection: edg1983/Singularity_images
---

# edg1983/Singularity_images:hapcut2.def

```bash
$ singularity pull shub://edg1983/Singularity_images:hapcut2.def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%environment
    SHELL=/bin/bash
    PATH=$PATH:/usr/local/bin
    export C_INCLUDE_PATH=$C_INCLUDE_PATH:/opt/htslib-1.11
    export LIBRARY_PATH=$LIBRARY_PATH:/opt/htslib-1.11
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/htslib-1.11
    LC_ALL=C.UTF-8


%help
    HapCUT2 container latest version from
    https://github.com/vibansal/HapCUT2

    Available commands: HAPCUT2, extractHAIRS

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
        git \
        make \
        wget \
        zlib1g-dev \
        autoconf
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    
    ## Install HTSlib
    cd /opt
    wget https://github.com/samtools/htslib/releases/download/1.11/htslib-1.11.tar.bz2
    tar -jxvf htslib-1.11.tar.bz2
    rm htslib-1.11.tar.bz2
    cd htslib-1.11
    make
    make install

    ## Install HapCUT2
    cd /opt
    git clone https://github.com/vibansal/HapCUT2.git
    cd HapCUT2
    make HTSLIB=/opt/htslib-1.11
    ln -s /opt/HapCUT2/build/HAPCUT2 /usr/local/bin/HAPCUT2
    ln -s /opt/HapCUT2/build/extractHAIRS /usr/local/bin/extractHAIRS
```

## Collection

 - Name: [edg1983/Singularity_images](https://github.com/edg1983/Singularity_images)
 - License: None

