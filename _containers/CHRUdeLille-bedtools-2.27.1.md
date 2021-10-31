---
id: 2873
name: "CHRUdeLille/bedtools"
branch: "master"
tag: "2.27.1"
commit: "91a119e50040fe0dca9645efb07ba6ea1398394b"
version: "f8f61b88498fc9e365c3bc03afe1b362"
build_date: "2020-06-04T09:03:08.747Z"
size_mb: 674
size: 288477215
sif: "https://datasets.datalad.org/shub/CHRUdeLille/bedtools/2.27.1/2020-06-04-91a119e5-f8f61b88/f8f61b88498fc9e365c3bc03afe1b362.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CHRUdeLille/bedtools/2.27.1/2020-06-04-91a119e5-f8f61b88/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/bedtools/2.27.1/2020-06-04-91a119e5-f8f61b88/Singularity
collection: CHRUdeLille/bedtools
---

# CHRUdeLille/bedtools:2.27.1

```bash
$ singularity pull shub://CHRUdeLille/bedtools:2.27.1
```

## Singularity Recipe

```singularity
#!/bin/bash
#
# Christophe Demay <christophe.demay@chru-lille.fr>
# 2018/04/24: initial version
BootStrap: docker
From: phusion/baseimage:0.10.1
%labels
  MAINTAINER christophe.demay@chru-lille.fr
  BEDTOOLS_VERSION 2.27.1
  RECIPE_VERSION 0.1

%environment

%help
  echo "   _              _ _____           _       ____    ____ _____ _ 
          | |__   ___  __| |_   _|__   ___ | |___  |___ \  |___ \___  / |
          | '_ \ / _ \/ _` | | |/ _ \ / _ \| / __|   __) |   __) | / /| |
          | |_) |  __/ (_| | | | (_) | (_) | \__ \  / __/ _ / __/ / /_| |
          |_.__/ \___|\__,_| |_|\___/ \___/|_|___/ |_____(_)_____/_/(_)_|"
  
  Singularity container for BedTools 2.27.1 <https://github.com/arq5x/bedtools2> application. Documentation available at <http://bedtools.readthedocs.io/en/latest/index.html>
  
%post

  apt-get update
  apt-get -y install  build-essential \
  libgcc1 \
  libc6 \
  libstdc++6 \
  gcc-multilib \
  apt-utils \
  unzip \
  zlib1g \
  zlib1g-dev \
  filo \
  aria2 \
  python2.7 \
  python2.7-dev \
  libpython2.7 \
  libpython2.7-dev

  ln -s /usr/bin/python2.7 /usr/bin/python
  
  cd /usr/local/
  aria2c -x 6 -s 6 https://github.com/arq5x/bedtools2/releases/download/v2.27.1/bedtools-2.27.1.tar.gz
  tar -zxvf bedtools-2.27.1.tar.gz
  cd /usr/local/bedtools2
  make
  ln -s /usr/local/bedtools2/bin/* /usr/local/bin/
  
  apt-get clean
```

## Collection

 - Name: [CHRUdeLille/bedtools](https://github.com/CHRUdeLille/bedtools)
 - License: None

