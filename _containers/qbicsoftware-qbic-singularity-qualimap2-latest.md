---
id: 1493
name: "qbicsoftware/qbic-singularity-qualimap2"
branch: "master"
tag: "latest"
commit: "47ace9d37c81911da18798626b0c2815b6aecae7"
version: "13cbe8f4298538e117098da26aa5b794"
build_date: "2018-01-29T21:32:15.428Z"
size_mb: 1022
size: 414146591
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qualimap2/latest/2018-01-29-47ace9d3-13cbe8f4/13cbe8f4298538e117098da26aa5b794.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-qualimap2/latest/2018-01-29-47ace9d3-13cbe8f4/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qualimap2/latest/2018-01-29-47ace9d3-13cbe8f4/Singularity
collection: qbicsoftware/qbic-singularity-qualimap2
---

# qbicsoftware/qbic-singularity-qualimap2:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-qualimap2:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.7

%post
/bin/sh build.sh

%files
#Installation of Qualimap
build.sh

%environment
    QUALIMAP_VERSION=22-08-17

%labels
Maintainer	alexander.peltzer@qbic.uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-qualimap2](https://github.com/qbicsoftware/qbic-singularity-qualimap2)
 - License: None

