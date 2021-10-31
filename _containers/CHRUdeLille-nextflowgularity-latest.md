---
id: 3804
name: "CHRUdeLille/nextflowgularity"
branch: "master"
tag: "latest"
commit: "3c43d853b377b27a4e402a0571f5a98f8885bac8"
version: "8e31175439ed6748cab9f5182c148583"
build_date: "2018-08-01T12:24:34.930Z"
size_mb: 373
size: 161660959
sif: "https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/latest/2018-08-01-3c43d853-8e311754/8e31175439ed6748cab9f5182c148583.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CHRUdeLille/nextflowgularity/latest/2018-08-01-3c43d853-8e311754/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/latest/2018-08-01-3c43d853-8e311754/Singularity
collection: CHRUdeLille/nextflowgularity
---

# CHRUdeLille/nextflowgularity:latest

```bash
$ singularity pull shub://CHRUdeLille/nextflowgularity:latest
```

## Singularity Recipe

```singularity
# =====================================
# HEADER
# =====================================
Bootstrap: docker
From: nextflow/nextflow:0.29.1

%labels
  MAINTAINER christophe.demay@chru-lille.fr
  CONTAINER_VERSION 0.0.1
  SINGULARITY_VERSION 2.5.1
  NEXTFLOW_VERSION 0.29.1

%setup

%files

%environment
  NXF_OPTS='-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap' 
  NXF_HOME=/.nextflow
  
%help

%post
  # =====================================
  # INSTALL DEPENDENCIES
  # =====================================
  apk update && apk upgrade 
  apk add --no-cache coreutils 
  apk add --no-cache curl bash 
  apk add --no-cache wget 
  apk add --no-cache build-base 
  apk add --no-cache python
  apk add --no-cache --upgrade tar
  apk add --no-cache linux-headers
  apk add --no-cache libarchive-dev
  apk add --no-cache squashfs-tools
  apk add --no-cache sudo
  
  
  # =====================================
  # INSTALL SINGULARITY
  # =====================================

  mkdir -p /opt/singularity && cd /opt/singularity

  SINGULARITY_VERSION=2.5.1
  wget https://github.com/singularityware/singularity/releases/download/$SINGULARITY_VERSION/singularity-$SINGULARITY_VERSION.tar.gz
  tar xvf singularity-$SINGULARITY_VERSION.tar.gz
  cd singularity-$SINGULARITY_VERSION
  ./configure --prefix=/usr/local
  make
  sudo make install
```

## Collection

 - Name: [CHRUdeLille/nextflowgularity](https://github.com/CHRUdeLille/nextflowgularity)
 - License: None

