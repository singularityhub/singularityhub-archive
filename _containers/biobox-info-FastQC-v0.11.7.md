---
id: 10719
name: "biobox-info/FastQC"
branch: "v0.11.7"
tag: "v0.11.7"
commit: "7457c5f6f7e73184ff8eec97477eca982ccd8df4"
version: "c002718bf649efefa914cbdf3a1b5f963483122be022c4f9e5591a998442897e"
build_date: "2019-09-06T14:36:08.109Z"
size_mb: 216.953125
size: 227491840
sif: "https://datasets.datalad.org/shub/biobox-info/FastQC/v0.11.7/2019-09-06-7457c5f6-c002718b/c002718bf649efefa914cbdf3a1b5f963483122be022c4f9e5591a998442897e.sif"
url: https://datasets.datalad.org/shub/biobox-info/FastQC/v0.11.7/2019-09-06-7457c5f6-c002718b/
recipe: https://datasets.datalad.org/shub/biobox-info/FastQC/v0.11.7/2019-09-06-7457c5f6-c002718b/Singularity
collection: biobox-info/FastQC
---

# biobox-info/FastQC:v0.11.7

```bash
$ singularity pull shub://biobox-info/FastQC:v0.11.7
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

