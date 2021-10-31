---
id: 1475
name: "Sophylax/datagen-container"
branch: "master"
tag: "latest"
commit: "715395f61ead30c6383f5735227ce324a2d53805"
version: "877a0f7f0431764992676741568ae36d"
build_date: "2018-02-06T14:11:39.253Z"
size_mb: 2365
size: 696627231
sif: "https://datasets.datalad.org/shub/Sophylax/datagen-container/latest/2018-02-06-715395f6-877a0f7f/877a0f7f0431764992676741568ae36d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sophylax/datagen-container/latest/2018-02-06-715395f6-877a0f7f/
recipe: https://datasets.datalad.org/shub/Sophylax/datagen-container/latest/2018-02-06-715395f6-877a0f7f/Singularity
collection: Sophylax/datagen-container
---

# Sophylax/datagen-container:latest

```bash
$ singularity pull shub://Sophylax/datagen-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: osrf/ros:indigo-desktop-full-trusty


%runscript
    bash

%post
    export LANG=C.UTF-8 
    export LC_ALL=C.UTF-8
    apt-get update && apt-get install -y --no-install-recommends \
    libreadline6 \
    libreadline6-dev \
    libncurses5-dev \
    libgmp3-dev \
    libgsl0-dev \
    libgsl0ldbl \
    libboost-all-dev \
    libnss3 \
    build-essential \
    gdb \
    wget \
    vim \
    && rm -rf /var/lib/apt/lists/*
    cd /bin
    wget http://www.dcc.fc.up.pt/~vsc/Yap/yap-6.2.2.tar.gz
    tar -xzvf /bin/yap-6.2.2.tar.gz \
    && mkdir -p /bin/yap-6.2.2/arch
    cd /bin/yap-6.2.2/arch
    ../configure --enable-tabling=yes --enable-dynamic-loading \
    && make \
    && make install \
    && make install_library \
    && mkdir -p /bin/rg_ws/src
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib:/usr/local/lib

%environment
    LANG=C.UTF-8
    LC_ALL=C.UTF-8
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib:/usr/local/lib
```

## Collection

 - Name: [Sophylax/datagen-container](https://github.com/Sophylax/datagen-container)
 - License: None

