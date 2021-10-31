---
id: 1798
name: "qbicsoftware/qbic-singularity-bowtie2"
branch: "master"
tag: "v2.3.0"
commit: "b332c8ec532ea2b9e60b52a2f9dca112a8949d9f"
version: "cb0454239c5ad1713200f1ee228486c7"
build_date: "2021-03-03T23:37:21.294Z"
size_mb: 983
size: 462184479
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-bowtie2/v2.3.0/2021-03-03-b332c8ec-cb045423/cb0454239c5ad1713200f1ee228486c7.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-bowtie2/v2.3.0/2021-03-03-b332c8ec-cb045423/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-bowtie2/v2.3.0/2021-03-03-b332c8ec-cb045423/Singularity
collection: qbicsoftware/qbic-singularity-bowtie2
---

# qbicsoftware/qbic-singularity-bowtie2:v2.3.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-bowtie2:v2.3.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%post
/bin/sh build.sh
export PATH="/usr/bin/miniconda/bin:$PATH"
conda config --add channels bioconda
conda install bowtie2=2.3.0

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    BOWTIE2=v2.3.0
    PATH="/usr/bin/miniconda/bin:$PATH"

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-bowtie2](https://github.com/qbicsoftware/qbic-singularity-bowtie2)
 - License: None

