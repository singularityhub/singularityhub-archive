---
id: 10829
name: "biobox-info/Samtools"
branch: "master"
tag: "latest"
commit: "d45965784415a53fe1e81a478c7ae0d7caa56110"
version: "c2a2ad6ee46aa4347f7bce5d89e55187e80cc31b07d8119cc04bbeddd986e19c"
build_date: "2019-10-21T07:12:07.628Z"
size_mb: 122.1875
size: 128122880
sif: "https://datasets.datalad.org/shub/biobox-info/Samtools/latest/2019-10-21-d4596578-c2a2ad6e/c2a2ad6ee46aa4347f7bce5d89e55187e80cc31b07d8119cc04bbeddd986e19c.sif"
url: https://datasets.datalad.org/shub/biobox-info/Samtools/latest/2019-10-21-d4596578-c2a2ad6e/
recipe: https://datasets.datalad.org/shub/biobox-info/Samtools/latest/2019-10-21-d4596578-c2a2ad6e/Singularity
collection: biobox-info/Samtools
---

# biobox-info/Samtools:latest

```bash
$ singularity pull shub://biobox-info/Samtools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
PATH=/usr/local/src/samtools-1.9:$PATH
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

%post
sed -i "s/archive.ubuntu/de.archive.ubuntu/" /etc/apt/sources.list && \
sed -i "s/security.ubuntu/de.security.ubuntu/" /etc/apt/sources.list && \
apt-get update
apt-get dist-upgrade -y 
apt-get install liblzma-dev libbz2-dev zlib1g-dev libncurses5-dev wget build-essential unzip git -y 
rm -rf /var/lib/apt/lists/*
mkdir -p /usr/local/src
cd /usr/local/src && \
wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
tar xf samtools-1.9.tar.bz2 && \
rm samtools-1.9.tar.bz2 && \
cd samtools-1.9 && \
./configure && \
make -j 6 && \
make install

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/Samtools](https://github.com/biobox-info/Samtools)
 - License: None

