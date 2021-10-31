---
id: 10718
name: "biobox-info/FastQC"
branch: "master"
tag: "latest"
commit: "c26f5de8911b18b24a5e23d9bf63bfbb83254b2e"
version: "3f2651827be652b67a7b128586e5466df5c3320caccc4cd8e4174792065a062a"
build_date: "2019-10-21T12:21:25.179Z"
size_mb: 216.953125
size: 227491840
sif: "https://datasets.datalad.org/shub/biobox-info/FastQC/latest/2019-10-21-c26f5de8-3f265182/3f2651827be652b67a7b128586e5466df5c3320caccc4cd8e4174792065a062a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/biobox-info/FastQC/latest/2019-10-21-c26f5de8-3f265182/
recipe: https://datasets.datalad.org/shub/biobox-info/FastQC/latest/2019-10-21-c26f5de8-3f265182/Singularity
collection: biobox-info/FastQC
---

# biobox-info/FastQC:latest

```bash
$ singularity pull shub://biobox-info/FastQC:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
PATH=/usr/local/src/FastQC:$PATH
export LC_ALL=C

%post
apt-get update 
apt-get dist-upgrade -y 
apt-get install wget build-essential unzip openjdk-11-jre -y 
rm -rf /var/lib/apt/lists/*
mkdir -p /usr/local/src
cd /usr/local/src && \
wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip -O fastqc.zip && \
unzip fastqc.zip && \
rm fastqc.zip && \
chmod +X FastQC/fastqc && \
chmod 755 FastQC/fastqc

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/FastQC](https://github.com/biobox-info/FastQC)
 - License: None

