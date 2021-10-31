---
id: 753
name: "qbicsoftware/qbic-singularity-htseq"
branch: "master"
tag: "latest"
commit: "d2f7c0fc1a5d800698d986768fee04a167e40abc"
version: "570a86a456b9feb9a72ab48db6526016"
build_date: "2017-11-09T13:22:23.863Z"
size_mb: 533
size: 154472479
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-htseq/latest/2017-11-09-d2f7c0fc-570a86a4/570a86a456b9feb9a72ab48db6526016.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-htseq/latest/2017-11-09-d2f7c0fc-570a86a4/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-htseq/latest/2017-11-09-d2f7c0fc-570a86a4/Singularity
collection: qbicsoftware/qbic-singularity-htseq
---

# qbicsoftware/qbic-singularity-htseq:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-htseq:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
#MultiQC Version
/bin/sh build.sh

%files
#Installation of MultiQC
build.sh

%environment
    MULTIQC_VERSION=v1.3-dev0-2017-10-16

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-htseq](https://github.com/qbicsoftware/qbic-singularity-htseq)
 - License: None

