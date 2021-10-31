---
id: 472
name: "qbicsoftware/qbic-singularity-snpeff"
branch: "master"
tag: "latest"
commit: "4a5769d0e59d0edda95be1a2cc7ec120c50bf27f"
version: "6b41c86729937ad27eaffd67ff2a187e"
build_date: "2021-02-03T08:30:37.406Z"
size_mb: 576
size: 186986527
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-snpeff/latest/2021-02-03-4a5769d0-6b41c867/6b41c86729937ad27eaffd67ff2a187e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-snpeff/latest/2021-02-03-4a5769d0-6b41c867/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-snpeff/latest/2021-02-03-4a5769d0-6b41c867/Singularity
collection: qbicsoftware/qbic-singularity-snpeff
---

# qbicsoftware/qbic-singularity-snpeff:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-snpeff:latest
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

