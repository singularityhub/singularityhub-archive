---
id: 782
name: "qbicsoftware/qbic-singularity-featureCounts"
branch: "master"
tag: "v1.5.3"
commit: "c21c6c0903c7b0c5e5db07ae9c18dda07b157178"
version: "fdf92c3f287824ca5e44d8337ef070e6"
build_date: "2017-11-10T17:45:22.283Z"
size_mb: 672
size: 163905567
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-featureCounts/v1.5.3/2017-11-10-c21c6c09-fdf92c3f/fdf92c3f287824ca5e44d8337ef070e6.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-featureCounts/v1.5.3/2017-11-10-c21c6c09-fdf92c3f/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-featureCounts/v1.5.3/2017-11-10-c21c6c09-fdf92c3f/Singularity
collection: qbicsoftware/qbic-singularity-featureCounts
---

# qbicsoftware/qbic-singularity-featureCounts:v1.5.3

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-featureCounts:v1.5.3
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

