---
id: 781
name: "qbicsoftware/qbic-singularity-featureCounts"
branch: "master"
tag: "latest"
commit: "c21c6c0903c7b0c5e5db07ae9c18dda07b157178"
version: "c04d5ce2d83776d2bc1d0a03ce9e03f9"
build_date: "2017-11-10T17:45:22.290Z"
size_mb: 672
size: 163905567
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-featureCounts/latest/2017-11-10-c21c6c09-c04d5ce2/c04d5ce2d83776d2bc1d0a03ce9e03f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-featureCounts/latest/2017-11-10-c21c6c09-c04d5ce2/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-featureCounts/latest/2017-11-10-c21c6c09-c04d5ce2/Singularity
collection: qbicsoftware/qbic-singularity-featureCounts
---

# qbicsoftware/qbic-singularity-featureCounts:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-featureCounts:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
#Installation of Subread
build.sh

%environment
    SubRead_VERSION=1.5.3

%labels
Maintainer	alexander.peltzer@qbic.uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-featureCounts](https://github.com/qbicsoftware/qbic-singularity-featureCounts)
 - License: None

