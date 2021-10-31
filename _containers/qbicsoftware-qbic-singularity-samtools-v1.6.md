---
id: 1110
name: "qbicsoftware/qbic-singularity-samtools"
branch: "master"
tag: "v1.6"
commit: "0fbb5d32558ab02c4d3a3230d5bc28d387f878f2"
version: "f28af7210f95911f4a851fd6e86b8741"
build_date: "2017-12-12T10:16:50.184Z"
size_mb: 338
size: 56188959
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/v1.6/2017-12-12-0fbb5d32-f28af721/f28af7210f95911f4a851fd6e86b8741.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/v1.6/2017-12-12-0fbb5d32-f28af721/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-samtools/v1.6/2017-12-12-0fbb5d32-f28af721/Singularity
collection: qbicsoftware/qbic-singularity-samtools
---

# qbicsoftware/qbic-singularity-samtools:v1.6

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-samtools:v1.6
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
#Installation of Samtools
build.sh

%environment
    SAMTOOLS_VERSION=1.6-2017-10-16

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-samtools](https://github.com/qbicsoftware/qbic-singularity-samtools)
 - License: None

