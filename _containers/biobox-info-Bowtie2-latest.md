---
id: 10907
name: "biobox-info/Bowtie2"
branch: "master"
tag: "latest"
commit: "f6e6ebd09749d88c0c6a1b2e318d8abed05306d6"
version: "b25c4ff24b77e5168d10915e6686982221cf6d9394404d942e51be9dd6d0db18"
build_date: "2019-09-16T13:14:41.868Z"
size_mb: 185.4453125
size: 194453504
sif: "https://datasets.datalad.org/shub/biobox-info/Bowtie2/latest/2019-09-16-f6e6ebd0-b25c4ff2/b25c4ff24b77e5168d10915e6686982221cf6d9394404d942e51be9dd6d0db18.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/biobox-info/Bowtie2/latest/2019-09-16-f6e6ebd0-b25c4ff2/
recipe: https://datasets.datalad.org/shub/biobox-info/Bowtie2/latest/2019-09-16-f6e6ebd0-b25c4ff2/Singularity
collection: biobox-info/Bowtie2
---

# biobox-info/Bowtie2:latest

```bash
$ singularity pull shub://biobox-info/Bowtie2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
PATH=/usr/local/src/bowtie2-2.3.5.1-linux-x86_64:$PATH
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

%post
sed -i "s/archive.ubuntu/de.archive.ubuntu/" /etc/apt/sources.list && \
sed -i "s/security.ubuntu/de.security.ubuntu/" /etc/apt/sources.list && \
apt-get update
apt-get dist-upgrade -y 
apt-get install wget python python3 build-essential unzip git -y 
rm -rf /var/lib/apt/lists/*
mkdir -p /usr/local/src
cd /usr/local/src && \
wget -c https://netix.dl.sourceforge.net/project/bowtie-bio/bowtie2/2.3.5.1/bowtie2-2.3.5.1-linux-x86_64.zip && \
unzip bowtie2-2.3.5.1-linux-x86_64.zip && \
rm bowtie2-2.3.5.1-linux-x86_64.zip

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/Bowtie2](https://github.com/biobox-info/Bowtie2)
 - License: None

