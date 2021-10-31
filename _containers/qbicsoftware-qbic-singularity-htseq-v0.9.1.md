---
id: 754
name: "qbicsoftware/qbic-singularity-htseq"
branch: "master"
tag: "v0.9.1"
commit: "d2f7c0fc1a5d800698d986768fee04a167e40abc"
version: "eabbcc35b106951e33f4127113455fad"
build_date: "2017-11-09T13:22:23.869Z"
size_mb: 531
size: 154472479
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-htseq/v0.9.1/2017-11-09-d2f7c0fc-eabbcc35/eabbcc35b106951e33f4127113455fad.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-htseq/v0.9.1/2017-11-09-d2f7c0fc-eabbcc35/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-htseq/v0.9.1/2017-11-09-d2f7c0fc-eabbcc35/Singularity
collection: qbicsoftware/qbic-singularity-htseq
---

# qbicsoftware/qbic-singularity-htseq:v0.9.1

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-htseq:v0.9.1
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

