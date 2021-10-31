---
id: 1797
name: "qbicsoftware/qbic-singularity-bowtie2"
branch: "master"
tag: "latest"
commit: "b332c8ec532ea2b9e60b52a2f9dca112a8949d9f"
version: "1c3efe049236df109cfaa49750fd58b1"
build_date: "2019-11-29T03:55:11.323Z"
size_mb: 983
size: 462184479
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-bowtie2/latest/2019-11-29-b332c8ec-1c3efe04/1c3efe049236df109cfaa49750fd58b1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-bowtie2/latest/2019-11-29-b332c8ec-1c3efe04/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-bowtie2/latest/2019-11-29-b332c8ec-1c3efe04/Singularity
collection: qbicsoftware/qbic-singularity-bowtie2
---

# qbicsoftware/qbic-singularity-bowtie2:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-bowtie2:latest
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

