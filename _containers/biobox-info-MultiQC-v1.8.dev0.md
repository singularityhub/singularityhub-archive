---
id: 10715
name: "biobox-info/MultiQC"
branch: "v1.8.dev0"
tag: "v1.8.dev0"
commit: "2499f126d183baedff0358eb86c56ae5aad14114"
version: "cfce51f6b7203548487c42bb8575e34556e8cec624004fbff02da917c3ee600b"
build_date: "2019-08-29T15:15:19.346Z"
size_mb: 174.03125
size: 182484992
sif: "https://datasets.datalad.org/shub/biobox-info/MultiQC/v1.8.dev0/2019-08-29-2499f126-cfce51f6/cfce51f6b7203548487c42bb8575e34556e8cec624004fbff02da917c3ee600b.sif"
url: https://datasets.datalad.org/shub/biobox-info/MultiQC/v1.8.dev0/2019-08-29-2499f126-cfce51f6/
recipe: https://datasets.datalad.org/shub/biobox-info/MultiQC/v1.8.dev0/2019-08-29-2499f126-cfce51f6/Singularity
collection: biobox-info/MultiQC
---

# biobox-info/MultiQC:v1.8.dev0

```bash
$ singularity pull shub://biobox-info/MultiQC:v1.8.dev0
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

