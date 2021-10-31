---
id: 1310
name: "qbicsoftware/qbic-singularity-multiqc"
branch: "master"
tag: "latest"
commit: "c7c52a320ec7dedae02df3f236a260c0028b88ab"
version: "9b56ceb7a86d29c672f4c993a1554136"
build_date: "2018-01-15T15:00:25.630Z"
size_mb: 389
size: 153894943
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-multiqc/latest/2018-01-15-c7c52a32-9b56ceb7/9b56ceb7a86d29c672f4c993a1554136.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-multiqc/latest/2018-01-15-c7c52a32-9b56ceb7/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-multiqc/latest/2018-01-15-c7c52a32-9b56ceb7/Singularity
collection: qbicsoftware/qbic-singularity-multiqc
---

# qbicsoftware/qbic-singularity-multiqc:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-multiqc:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.7

%post
#MultiQC Version
/bin/sh build.sh
pip install multiqc

%files
#Installation of MultiQC
build.sh

%environment
    MULTIQC_VERSION=v1.4

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-multiqc](https://github.com/qbicsoftware/qbic-singularity-multiqc)
 - License: None

