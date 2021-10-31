---
id: 10831
name: "biobox-info/Samtools"
branch: "v1.9"
tag: "v1.9"
commit: "73c1eecff06fd48466249e10e4fbf26b8beebddb"
version: "63bbf98369ceb9c486290b2858f54e3e7361d8ee9feab264237a1e002ac64f7f"
build_date: "2019-09-09T14:43:44.248Z"
size_mb: 122.1875
size: 128122880
sif: "https://datasets.datalad.org/shub/biobox-info/Samtools/v1.9/2019-09-09-73c1eecf-63bbf983/63bbf98369ceb9c486290b2858f54e3e7361d8ee9feab264237a1e002ac64f7f.sif"
url: https://datasets.datalad.org/shub/biobox-info/Samtools/v1.9/2019-09-09-73c1eecf-63bbf983/
recipe: https://datasets.datalad.org/shub/biobox-info/Samtools/v1.9/2019-09-09-73c1eecf-63bbf983/Singularity
collection: biobox-info/Samtools
---

# biobox-info/Samtools:v1.9

```bash
$ singularity pull shub://biobox-info/Samtools:v1.9
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

