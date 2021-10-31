---
id: 5660
name: "CHRUdeLille/bcl2fastq2_containers"
branch: "master"
tag: "2.20.0.422"
commit: "1d23b0b160c3efdb7b47809ae07f89b26948304f"
version: "94110c9f334a0bf9905e5f4b4ca3505f"
build_date: "2018-11-20T17:27:30.328Z"
size_mb: 497
size: 187277343
sif: "https://datasets.datalad.org/shub/CHRUdeLille/bcl2fastq2_containers/2.20.0.422/2018-11-20-1d23b0b1-94110c9f/94110c9f334a0bf9905e5f4b4ca3505f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CHRUdeLille/bcl2fastq2_containers/2.20.0.422/2018-11-20-1d23b0b1-94110c9f/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/bcl2fastq2_containers/2.20.0.422/2018-11-20-1d23b0b1-94110c9f/Singularity
collection: CHRUdeLille/bcl2fastq2_containers
---

# CHRUdeLille/bcl2fastq2_containers:2.20.0.422

```bash
$ singularity pull shub://CHRUdeLille/bcl2fastq2_containers:2.20.0.422
```

## Singularity Recipe

```singularity
#!/bin/bash
#
# Emilie Ait Yahya <emilie.aityahya@chru-lille.fr>
# 2018/11/18: initial version

BootStrap: docker
From: phusion/baseimage:0.11
%labels
MAINTAINER emilie.aityahya@chru-lille.fr
BCL2FASTQ2_VERSION 2.20.0
RECIPE_VERSION 0.1

%environment
export TMP=/tmp
export SOURCE=${TMP}/bcl2fastq2
export BUILD=${TMP}/bcl2fastq2-v2-20-0-build
export INSTALL_DIR=/usr/local/bcl2fastq2-v2.20.0

%help
echo ""
Singularity container for bcl2fastq2 2.20.0 <http://emea.support.illumina.com/downloads/bcl2fastq-conversion-software-v2-20.html>
bcl2fastq2 Conversion Software v2.20 User Guide available here <http://emea.support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl2fastq/bcl2fastq2_guide_15051736_v2.pdf>

%post
apt-get update
apt-get install -y wget unzip alien dpkg-dev debhelper build-essential
cd ${SOURCE}/
wget http://emea.support.illumina.com/content/dam/illumina-support/documents/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-linux-x86-64.zip
unzip *.zip
alien ${TMP}/bcl2fastq2-*.rpm
dpkg -i ${TMP}/bcl2fastq2*.deb

#cd ${INSTALL_DIR}
apt-get clean
```

## Collection

 - Name: [CHRUdeLille/bcl2fastq2_containers](https://github.com/CHRUdeLille/bcl2fastq2_containers)
 - License: None

