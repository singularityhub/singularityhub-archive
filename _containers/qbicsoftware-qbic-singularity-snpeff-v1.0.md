---
id: 505
name: "qbicsoftware/qbic-singularity-snpeff"
branch: "master"
tag: "v1.0"
commit: "0456f44ce4f7908d2e97b676596264b99dbf0afd"
version: "2d1072f61bdc5ce22a3486e7d60bc4b0"
build_date: "2017-10-23T15:43:13.865Z"
size_mb: 571
size: 185929759
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-snpeff/v1.0/2017-10-23-0456f44c-2d1072f6/2d1072f61bdc5ce22a3486e7d60bc4b0.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-snpeff/v1.0/2017-10-23-0456f44c-2d1072f6/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-snpeff/v1.0/2017-10-23-0456f44c-2d1072f6/Singularity
collection: qbicsoftware/qbic-singularity-snpeff
---

# qbicsoftware/qbic-singularity-snpeff:v1.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-snpeff:v1.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
build.sh

%environment
SNPEFF_VERSION=v4.3p

%runscript
echo "Arguments received: $*"
exec snpEff "$@"

%labels
Maintainer	sven.fillinger@qbic.uni-tuebingen.de

%test
snpEff -version
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-snpeff](https://github.com/qbicsoftware/qbic-singularity-snpeff)
 - License: None

