---
id: 749
name: "qbicsoftware/qbic-singularity-tophat2"
branch: "master"
tag: "latest"
commit: "68710e710780eb5c00aeb203fa64ba32442c8c5a"
version: "b3d1f82b7baf8091536cabacb78ef69e"
build_date: "2020-10-06T07:47:35.381Z"
size_mb: 669
size: 128409631
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tophat2/latest/2020-10-06-68710e71-b3d1f82b/b3d1f82b7baf8091536cabacb78ef69e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-tophat2/latest/2020-10-06-68710e71-b3d1f82b/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tophat2/latest/2020-10-06-68710e71-b3d1f82b/Singularity
collection: qbicsoftware/qbic-singularity-tophat2
---

# qbicsoftware/qbic-singularity-tophat2:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-tophat2:latest
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

