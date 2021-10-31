---
id: 1901
name: "edgano/mBed-nf"
branch: "master"
tag: "latest"
commit: "c770be65da5d88c9205675e2747b13afe657861e"
version: "dbae504732edc14294ee05239461f818"
build_date: "2018-03-01T21:03:58.440Z"
size_mb: 756
size: 308367391
sif: "https://datasets.datalad.org/shub/edgano/mBed-nf/latest/2018-03-01-c770be65-dbae5047/dbae504732edc14294ee05239461f818.simg"
url: https://datasets.datalad.org/shub/edgano/mBed-nf/latest/2018-03-01-c770be65-dbae5047/
recipe: https://datasets.datalad.org/shub/edgano/mBed-nf/latest/2018-03-01-c770be65-dbae5047/Singularity
collection: edgano/mBed-nf
---

# edgano/mBed-nf:latest

```bash
$ singularity pull shub://edgano/mBed-nf:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:debian:jessie

%labels
MAINTAINER Edgar Garriga

%post
  apt-get update
  apt-get install -y --no-install-recommends ed less vim-tiny wget git
  apt-get install -y --no-install-recommends python build-essential cmake curl libargtable2-0
  apt-get install -y --no-install-recommends python-biopython python-numpy ruby python-setuptools
  apt-get install -y --no-install-recommends default-jdk libpng-dev

##
# install SeqFilter
##
  git clone https://github.com/edgano/mBed-nf
  cd mBed-nf/bin/SeqFilter
  rm -rf lib
  make

##
# install mBed
##
  cd ../mBed
  make

%environment
export PATH=/mBed-nf/bin/mBed/:/mBed-nf/bin/SeqFilter:$PATH
```

## Collection

 - Name: [edgano/mBed-nf](https://github.com/edgano/mBed-nf)
 - License: None

