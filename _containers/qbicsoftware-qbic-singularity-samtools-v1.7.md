---
id: 1496
name: "qbicsoftware/qbic-singularity-samtools"
branch: "master"
tag: "v1.7"
commit: "83257ec098afff98930c26bf41acc034e63dbc7f"
version: "f59344906d4f982c119b900d124598d9"
build_date: "2021-03-05T17:39:26.814Z"
size_mb: 236
size: 76431391
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/v1.7/2021-03-05-83257ec0-f5934490/f59344906d4f982c119b900d124598d9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-samtools/v1.7/2021-03-05-83257ec0-f5934490/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/v1.7/2021-03-05-83257ec0-f5934490/Singularity
collection: qbicsoftware/qbic-singularity-samtools
---

# qbicsoftware/qbic-singularity-samtools:v1.7

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-samtools:v1.7
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

