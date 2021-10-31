---
id: 10908
name: "biobox-info/Bowtie2"
branch: "v2.3.5.1"
tag: "v2.3.5.1"
commit: "fc38292e070679e577aa32750636e9e1cfecc43c"
version: "579c01e1bdb077348701efa59d48eca2d6cd6528c68b3e25c8b26fc711da167f"
build_date: "2019-09-16T13:40:31.744Z"
size_mb: 185.4453125
size: 194453504
sif: "https://datasets.datalad.org/shub/biobox-info/Bowtie2/v2.3.5.1/2019-09-16-fc38292e-579c01e1/579c01e1bdb077348701efa59d48eca2d6cd6528c68b3e25c8b26fc711da167f.sif"
url: https://datasets.datalad.org/shub/biobox-info/Bowtie2/v2.3.5.1/2019-09-16-fc38292e-579c01e1/
recipe: https://datasets.datalad.org/shub/biobox-info/Bowtie2/v2.3.5.1/2019-09-16-fc38292e-579c01e1/Singularity
collection: biobox-info/Bowtie2
---

# biobox-info/Bowtie2:v2.3.5.1

```bash
$ singularity pull shub://biobox-info/Bowtie2:v2.3.5.1
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

