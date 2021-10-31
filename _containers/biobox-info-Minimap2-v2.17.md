---
id: 10828
name: "biobox-info/Minimap2"
branch: "v2.17"
tag: "v2.17"
commit: "433913d787e12afc5ea0ddc02f526b54812171bc"
version: "d7a17eb41c30ef5bc1d810becdbebe817e27e57bb8fae52bd2e0418ddbc68d88"
build_date: "2019-09-09T06:56:55.753Z"
size_mb: 106.24609375
size: 111407104
sif: "https://datasets.datalad.org/shub/biobox-info/Minimap2/v2.17/2019-09-09-433913d7-d7a17eb4/d7a17eb41c30ef5bc1d810becdbebe817e27e57bb8fae52bd2e0418ddbc68d88.sif"
url: https://datasets.datalad.org/shub/biobox-info/Minimap2/v2.17/2019-09-09-433913d7-d7a17eb4/
recipe: https://datasets.datalad.org/shub/biobox-info/Minimap2/v2.17/2019-09-09-433913d7-d7a17eb4/Singularity
collection: biobox-info/Minimap2
---

# biobox-info/Minimap2:v2.17

```bash
$ singularity pull shub://biobox-info/Minimap2:v2.17
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
PATH=/usr/local/src/minimap2-2.17_x64-linux:$PATH
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

%post
sed -i "s/archive.ubuntu/de.archive.ubuntu/" /etc/apt/sources.list && \
sed -i "s/security.ubuntu/de.security.ubuntu/" /etc/apt/sources.list && \
apt-get update
apt-get dist-upgrade -y 
apt-get install wget build-essential unzip git -y 
rm -rf /var/lib/apt/lists/*
mkdir -p /usr/local/src
cd /usr/local/src && \
wget -c https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
tar xf minimap2-2.17_x64-linux.tar.bz2 && \
rm minimap2-2.17_x64-linux.tar.bz2

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/Minimap2](https://github.com/biobox-info/Minimap2)
 - License: None

