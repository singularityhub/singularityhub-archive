---
id: 10825
name: "biobox-info/Minimap2"
branch: "v2.17"
tag: "latest"
commit: "1a28ba11d842cbd94a7c1e3f2e10716b952922d6"
version: "fc9eac006eabdbef684aa4608b89883a36873f6d99be909f432d65d3241e24f9"
build_date: "2019-10-21T07:13:23.235Z"
size_mb: 106.24609375
size: 111407104
sif: "https://datasets.datalad.org/shub/biobox-info/Minimap2/latest/2019-10-21-1a28ba11-fc9eac00/fc9eac006eabdbef684aa4608b89883a36873f6d99be909f432d65d3241e24f9.sif"
url: https://datasets.datalad.org/shub/biobox-info/Minimap2/latest/2019-10-21-1a28ba11-fc9eac00/
recipe: https://datasets.datalad.org/shub/biobox-info/Minimap2/latest/2019-10-21-1a28ba11-fc9eac00/Singularity
collection: biobox-info/Minimap2
---

# biobox-info/Minimap2:latest

```bash
$ singularity pull shub://biobox-info/Minimap2:latest
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

