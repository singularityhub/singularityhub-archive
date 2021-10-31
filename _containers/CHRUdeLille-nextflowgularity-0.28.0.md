---
id: 3805
name: "CHRUdeLille/nextflowgularity"
branch: "master"
tag: "0.28.0"
commit: "e5f6537e5601032f0a67a40fe63135e84e3e90e7"
version: "baf6f0cf2c1d60a37c7f4daba54b1c28"
build_date: "2018-08-01T12:24:34.937Z"
size_mb: 368
size: 160342047
sif: "https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/0.28.0/2018-08-01-e5f6537e-baf6f0cf/baf6f0cf2c1d60a37c7f4daba54b1c28.simg"
url: https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/0.28.0/2018-08-01-e5f6537e-baf6f0cf/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/0.28.0/2018-08-01-e5f6537e-baf6f0cf/Singularity
collection: CHRUdeLille/nextflowgularity
---

# CHRUdeLille/nextflowgularity:0.28.0

```bash
$ singularity pull shub://CHRUdeLille/nextflowgularity:0.28.0
```

## Singularity Recipe

```singularity
# =====================================
# HEADER
# =====================================
Bootstrap: docker
From: nextflow/nextflow:0.28.0

%labels
  MAINTAINER christophe.demay@chru-lille.fr
  CONTAINER_VERSION 0.0.1
  SINGULARITY_VERSION 2.4.6
  NEXTFLOW_VERSION 0.28.0

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
  apk add --no-cache sudo
  
  
  # =====================================
  # INSTALL SINGULARITY
  # =====================================

  mkdir -p /opt/singularity && cd /opt/singularity

  SINGULARITY_VERSION=2.4.6
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

