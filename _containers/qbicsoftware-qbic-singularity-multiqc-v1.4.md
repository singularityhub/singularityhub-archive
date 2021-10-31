---
id: 1309
name: "qbicsoftware/qbic-singularity-multiqc"
branch: "master"
tag: "v1.4"
commit: "c7c52a320ec7dedae02df3f236a260c0028b88ab"
version: "bca4c0509d6c9c233a18d570218783fc"
build_date: "2020-07-09T21:38:47.117Z"
size_mb: 389
size: 153894943
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-multiqc/v1.4/2020-07-09-c7c52a32-bca4c050/bca4c0509d6c9c233a18d570218783fc.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-multiqc/v1.4/2020-07-09-c7c52a32-bca4c050/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-multiqc/v1.4/2020-07-09-c7c52a32-bca4c050/Singularity
collection: qbicsoftware/qbic-singularity-multiqc
---

# qbicsoftware/qbic-singularity-multiqc:v1.4

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-multiqc:v1.4
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.7

%post
#MultiQC Version
/bin/sh build.sh
pip install multiqc==1.4 

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

