---
id: 10717
name: "biobox-info/MultiQC"
branch: "master"
tag: "latest"
commit: "a0f37519ffc461e945c877ffbd7c68d89a0192dd"
version: "8a734a2eb66fbcfb79e76b902269c18626ec8482d10130ecde4a920d1546f674"
build_date: "2019-10-21T07:11:58.471Z"
size_mb: 174.03125
size: 182484992
sif: "https://datasets.datalad.org/shub/biobox-info/MultiQC/latest/2019-10-21-a0f37519-8a734a2e/8a734a2eb66fbcfb79e76b902269c18626ec8482d10130ecde4a920d1546f674.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/biobox-info/MultiQC/latest/2019-10-21-a0f37519-8a734a2e/
recipe: https://datasets.datalad.org/shub/biobox-info/MultiQC/latest/2019-10-21-a0f37519-8a734a2e/Singularity
collection: biobox-info/MultiQC
---

# biobox-info/MultiQC:latest

```bash
$ singularity pull shub://biobox-info/MultiQC:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
PATH=/usr/local/src/MultiQC:$PATH
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

%post
apt-get update 
apt-get dist-upgrade -y 
apt-get install wget build-essential unzip git python3-setuptools python3 -y 
rm -rf /var/lib/apt/lists/*
mkdir -p /usr/local/src
cd /usr/local/src && \
git clone https://github.com/ewels/MultiQC.git && \
cd MultiQC && \
python3 setup.py install

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/MultiQC](https://github.com/biobox-info/MultiQC)
 - License: None

