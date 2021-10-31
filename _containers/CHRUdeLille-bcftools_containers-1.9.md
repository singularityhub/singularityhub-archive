---
id: 5494
name: "CHRUdeLille/bcftools_containers"
branch: "master"
tag: "1.9"
commit: "c221483342206c596ecb8fcebfbe48809e8dc34e"
version: "951dd33e134cf17bfa3d43a68ff0e7d3"
build_date: "2019-11-20T07:57:49.592Z"
size_mb: 493
size: 175767583
sif: "https://datasets.datalad.org/shub/CHRUdeLille/bcftools_containers/1.9/2019-11-20-c2214833-951dd33e/951dd33e134cf17bfa3d43a68ff0e7d3.simg"
url: https://datasets.datalad.org/shub/CHRUdeLille/bcftools_containers/1.9/2019-11-20-c2214833-951dd33e/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/bcftools_containers/1.9/2019-11-20-c2214833-951dd33e/Singularity
collection: CHRUdeLille/bcftools_containers
---

# CHRUdeLille/bcftools_containers:1.9

```bash
$ singularity pull shub://CHRUdeLille/bcftools_containers:1.9
```

## Singularity Recipe

```singularity
#!/bin/bash
#
# Chadi Saad <chadi.saad@chru-lille.fr>
# 2018/11/06: initial version


BootStrap: docker
From: phusion/baseimage:0.11

%labels
  MAINTAINER chadi.saad@chru-lille.fr
  VERSION 1.9

%environment
  export  PATH=/opt/bcftools/bin:$PATH

%help

  ____   _____ ______ _______ ____   ____  _       _____ 
 |  _ \ / ____|  ____|__   __/ __ \ / __ \| |     / ____|
 | |_) | |    | |__     | | | |  | | |  | | |    | (___  
 |  _ <| |    |  __|    | | | |  | | |  | | |     \___ \ 
 | |_) | |____| |       | | | |__| | |__| | |____ ____) |
 |____/ \_____|_|       |_|  \____/ \____/|______|_____/ 
                                                         
                                                         
  Singularity container for BCFTOOLS 1.9 <https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2> application. Documentation available at http://samtools.github.io/bcftools/howtos/index.html
  Cache folder is not included in the container. You have to bind folder containing the cache and add it with the '--cache' option.

%post
  apt-get update
  apt-get -y install build-essential \
  zlibc \
  zlib1g-dev \
  libgsl-dev \
  libperl5.26 \
  libbz2-dev \
  liblzma-dev \
  libcurl4 \
  libcrypto++6 \
  wget

         
  mkdir -p /opt/bcftools/src


  cd /opt/bcftools/src
  wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
  tar xjf bcftools-1.9.tar.bz2

  cd /opt/bcftools/src/bcftools-1.9/

  ./configure --prefix=/opt/bcftools
  make
  make install
```

## Collection

 - Name: [CHRUdeLille/bcftools_containers](https://github.com/CHRUdeLille/bcftools_containers)
 - License: None

