---
id: 1880
name: "qbicsoftware/qbic-singularity-skewer"
branch: "master"
tag: "v0.2.2"
commit: "8568b77d87ad723e6f652d0e86c01c5ef20dc2a5"
version: "61e12c2d85ac5b4936ca9d1ba06721b0"
build_date: "2018-02-27T17:10:25.426Z"
size_mb: 11
size: 4526111
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-skewer/v0.2.2/2018-02-27-8568b77d-61e12c2d/61e12c2d85ac5b4936ca9d1ba06721b0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-skewer/v0.2.2/2018-02-27-8568b77d-61e12c2d/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-skewer/v0.2.2/2018-02-27-8568b77d-61e12c2d/Singularity
collection: qbicsoftware/qbic-singularity-skewer
---

# qbicsoftware/qbic-singularity-skewer:v0.2.2

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-skewer:v0.2.2
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/skewer:0.2.2--1
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    SKEWER=0.2.2
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-skewer](https://github.com/qbicsoftware/qbic-singularity-skewer)
 - License: None

