---
id: 1178
name: "qbicsoftware/qbic-singularity-fastqc"
branch: "master"
tag: "latest"
commit: "72cf41fded6f4ed35f600c50a41a1e7f77f33ee9"
version: "6386229e79c932e86baffe4c629ce8f1"
build_date: "2020-07-09T16:50:15.998Z"
size_mb: 434
size: 158945311
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-fastqc/latest/2020-07-09-72cf41fd-6386229e/6386229e79c932e86baffe4c629ce8f1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-fastqc/latest/2020-07-09-72cf41fd-6386229e/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-fastqc/latest/2020-07-09-72cf41fd-6386229e/Singularity
collection: qbicsoftware/qbic-singularity-fastqc
---

# qbicsoftware/qbic-singularity-fastqc:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-fastqc:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:java:openjdk-8-jre-alpine

%post
/bin/sh build.sh
mkdir -p /build
cd /build
wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.6.zip
unzip fastqc_v0.11.6.zip
mv FastQC/ /usr/bin/
ln -s /usr/bin/FastQC/fastqc /usr/bin/fastqc
chmod +x /usr/bin/fastqc

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
FASTQC_VERSION=v0.11.6
LANG=en_US.UTF-8
FC_LANG=en-US
LC_CTYPE=en_US.UTF-8

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-fastqc](https://github.com/qbicsoftware/qbic-singularity-fastqc)
 - License: [MIT License](https://api.github.com/licenses/mit)

