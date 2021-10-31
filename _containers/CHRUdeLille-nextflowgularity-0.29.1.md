---
id: 3806
name: "CHRUdeLille/nextflowgularity"
branch: "master"
tag: "0.29.1"
commit: "fda06b8114ea42f453826b703666af4f51fc9251"
version: "6fa7739dd240f593a5ea75ffeefbcbc4"
build_date: "2018-08-01T12:24:34.923Z"
size_mb: 355
size: 155635743
sif: "https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/0.29.1/2018-08-01-fda06b81-6fa7739d/6fa7739dd240f593a5ea75ffeefbcbc4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CHRUdeLille/nextflowgularity/0.29.1/2018-08-01-fda06b81-6fa7739d/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/nextflowgularity/0.29.1/2018-08-01-fda06b81-6fa7739d/Singularity
collection: CHRUdeLille/nextflowgularity
---

# CHRUdeLille/nextflowgularity:0.29.1

```bash
$ singularity pull shub://CHRUdeLille/nextflowgularity:0.29.1
```

## Singularity Recipe

```singularity
# =====================================
# HEADER
# =====================================
Bootstrap: docker
From: openjdk:8-jre-alpine3.7

%labels
  MAINTAINER fabrice.bonte@chru-lille.fr
  CONTAINER_VERSION 0.0.1
  SINGULARITY_VERSION 2.4.5
  NEXTFLOW_VERSION 0.29.0

%setup

%files

%environment

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
  # INSTALL NEXTFLOW
  # =====================================

  HOME=/opt/nextflow
  mkdir -p /opt/nextflow 
  cd /opt/nextflow 
  curl -fsSL https://github.com/nextflow-io/nextflow/releases/download/v0.29.1/nextflow | bash 
  chmod 755 /opt/nextflow/nextflow 
  ln -s /opt/nextflow/nextflow /usr/bin/nextflow


  # =====================================
  # INSTALL SINGULARITY
  # =====================================

  mkdir -p /opt/singularity && cd /opt/singularity

  VERSION=2.4.5
  wget https://github.com/singularityware/singularity/releases/download/$VERSION/singularity-$VERSION.tar.gz
  tar xvf singularity-$VERSION.tar.gz
  cd singularity-$VERSION
  ./configure --prefix=/usr/local
  make
  sudo make install
```

## Collection

 - Name: [CHRUdeLille/nextflowgularity](https://github.com/CHRUdeLille/nextflowgularity)
 - License: None

