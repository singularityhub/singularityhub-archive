---
id: 750
name: "qbicsoftware/qbic-singularity-tophat2"
branch: "master"
tag: "v2.1.1"
commit: "68710e710780eb5c00aeb203fa64ba32442c8c5a"
version: "27d9fcd9c13f880caebb9a39420f0451"
build_date: "2017-11-09T13:22:23.847Z"
size_mb: 668
size: 128409631
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tophat2/v2.1.1/2017-11-09-68710e71-27d9fcd9/27d9fcd9c13f880caebb9a39420f0451.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tophat2/v2.1.1/2017-11-09-68710e71-27d9fcd9/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tophat2/v2.1.1/2017-11-09-68710e71-27d9fcd9/Singularity
collection: qbicsoftware/qbic-singularity-tophat2
---

# qbicsoftware/qbic-singularity-tophat2:v2.1.1

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-tophat2:v2.1.1
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

 - Name: [qbicsoftware/qbic-singularity-tophat2](https://github.com/qbicsoftware/qbic-singularity-tophat2)
 - License: None

