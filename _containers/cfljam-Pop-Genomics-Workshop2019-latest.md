---
id: 6834
name: "cfljam/Pop-Genomics-Workshop2019"
branch: "master"
tag: "latest"
commit: "6f04091618b97a3550a8fd0dfc653b712df4c3ba"
version: "f6ea633e87d2f1386e0090bbc38a646a"
build_date: "2019-02-18T10:57:37.362Z"
size_mb: 633
size: 231665695
sif: "https://datasets.datalad.org/shub/cfljam/Pop-Genomics-Workshop2019/latest/2019-02-18-6f040916-f6ea633e/f6ea633e87d2f1386e0090bbc38a646a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cfljam/Pop-Genomics-Workshop2019/latest/2019-02-18-6f040916-f6ea633e/
recipe: https://datasets.datalad.org/shub/cfljam/Pop-Genomics-Workshop2019/latest/2019-02-18-6f040916-f6ea633e/Singularity
collection: cfljam/Pop-Genomics-Workshop2019
---

# cfljam/Pop-Genomics-Workshop2019:latest

```bash
$ singularity pull shub://cfljam/Pop-Genomics-Workshop2019:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu
%labels
MAINTAINER John McCallum cfljam@users.noreply.github.com
%post

## A Docker Image for MAPGD + htslib + Samtools


DEBIAN_FRONTEND=noninteractive
apt-get update && \
apt-get -y install \
build-essential \
curl \
gcc \
git \
gettext \
libgsl-dev \
libcurl4-openssl-dev \
libgettextpo-dev \
libbz2-dev \
libncurses5-dev \
libsqlite3-dev \
liblzma-dev \
nano \
sqlite3 \
unzip \
zlib1g \
zlib1g-dev \
zip \
wget && \
rm -rf /var/lib/apt/lists/*

###############################
## Install Samtools + htlslib##
###############################

export SAMTOOLS_URL="https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2"

wget $SAMTOOLS_URL  -O samtools.tar.bz2 && \
tar -xjvf samtools.tar.bz2 && \
cd samtools-* && \
./configure && \
make && \
make prefix=/usr/local install &&\
cd htslib-* && \
./configure && \
make && \
sudo make install && \
make test

LD_LIBRARY_PATH='/samtools-1.9/htslib-1.9/'

###########
# MAPGD ###
###########

MAPGD_URL="https://github.com/LynchLab/MAPGD/archive/master.zip"
wget -O MAPGD.zip $MAPGD_URL  && \
unzip MAPGD.zip   && \
cd MAPGD-* && \
./configure && \
make && \
make install  # && \
#make test

%environment
export DEBIAN_FRONTEND=noninteractive
export LD_LIBRARY_PATH='/samtools-1.9/htslib-1.9/'
%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [cfljam/Pop-Genomics-Workshop2019](https://github.com/cfljam/Pop-Genomics-Workshop2019)
 - License: None

