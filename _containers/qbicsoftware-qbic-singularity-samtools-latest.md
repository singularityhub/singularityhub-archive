---
id: 1111
name: "qbicsoftware/qbic-singularity-samtools"
branch: "master"
tag: "latest"
commit: "83257ec098afff98930c26bf41acc034e63dbc7f"
version: "20610977262027476c546ef86fa671c6"
build_date: "2021-03-10T22:27:52.358Z"
size_mb: 236
size: 76431391
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/latest/2021-03-10-83257ec0-20610977/20610977262027476c546ef86fa671c6.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/latest/2021-03-10-83257ec0-20610977/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/latest/2021-03-10-83257ec0-20610977/Singularity
collection: qbicsoftware/qbic-singularity-samtools
---

# qbicsoftware/qbic-singularity-samtools:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-samtools:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.7

%post
/bin/sh build.sh
cd /build
SAMTOOLS_VERSION=1.7
wget https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VERSION/samtools-$SAMTOOLS_VERSION.tar.bz2
tar jxf samtools-$SAMTOOLS_VERSION.tar.bz2
cd samtools-$SAMTOOLS_VERSION
make
make install prefix=/usr


%files
#Installation of Samtools
build.sh

%environment
SAMTOOLS_VERSION=1.7

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-samtools](https://github.com/qbicsoftware/qbic-singularity-samtools)
 - License: None

