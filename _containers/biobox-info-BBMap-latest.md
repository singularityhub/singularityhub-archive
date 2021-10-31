---
id: 10937
name: "biobox-info/BBMap"
branch: "master"
tag: "latest"
commit: "0a233ff0626619f5bf62a493e23a79fd3a7a1f3c"
version: "160c536668ebb816b475952d8c941a481927737a3be1fb0b65e3fcddff40355a"
build_date: "2019-09-17T06:15:32.111Z"
size_mb: 130.56640625
size: 136908800
sif: "https://datasets.datalad.org/shub/biobox-info/BBMap/latest/2019-09-17-0a233ff0-160c5366/160c536668ebb816b475952d8c941a481927737a3be1fb0b65e3fcddff40355a.sif"
url: https://datasets.datalad.org/shub/biobox-info/BBMap/latest/2019-09-17-0a233ff0-160c5366/
recipe: https://datasets.datalad.org/shub/biobox-info/BBMap/latest/2019-09-17-0a233ff0-160c5366/Singularity
collection: biobox-info/BBMap
---

# biobox-info/BBMap:latest

```bash
$ singularity pull shub://biobox-info/BBMap:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
PATH=/usr/local/src/bbmap:$PATH
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
wget -c https://netix.dl.sourceforge.net/project/bbmap/BBMap_38.67.tar.gz -O bbmap_38.67.tar.gz && \
tar xf bbmap_38.67.tar.gz && \
rm bbmap_38.67.tar.gz

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/BBMap](https://github.com/biobox-info/BBMap)
 - License: None

