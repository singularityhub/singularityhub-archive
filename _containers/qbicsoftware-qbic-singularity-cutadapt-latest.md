---
id: 755
name: "qbicsoftware/qbic-singularity-cutadapt"
branch: "master"
tag: "latest"
commit: "c6c49dd0508e947af66b7836161cddbea8c93196"
version: "f9d5a20423a666d72bd8502d66830d6a"
build_date: "2020-08-05T12:43:02.259Z"
size_mb: 405
size: 81973279
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-cutadapt/latest/2020-08-05-c6c49dd0-f9d5a204/f9d5a20423a666d72bd8502d66830d6a.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-cutadapt/latest/2020-08-05-c6c49dd0-f9d5a204/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-cutadapt/latest/2020-08-05-c6c49dd0-f9d5a204/Singularity
collection: qbicsoftware/qbic-singularity-cutadapt
---

# qbicsoftware/qbic-singularity-cutadapt:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-cutadapt:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    <TOOL>_VERSION=v1.0

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-cutadapt](https://github.com/qbicsoftware/qbic-singularity-cutadapt)
 - License: None

