---
id: 1825
name: "qbicsoftware/qbic-singularity-varscan"
branch: "master"
tag: "v2.4.2"
commit: "8009459c4fd08587935496d93ea24729920ddcf4"
version: "91155b6cb20e433cc7725d32152a6829"
build_date: "2020-02-15T13:19:16.739Z"
size_mb: 169
size: 78606367
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/v2.4.2/2020-02-15-8009459c-91155b6c/91155b6cb20e433cc7725d32152a6829.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/v2.4.2/2020-02-15-8009459c-91155b6c/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/v2.4.2/2020-02-15-8009459c-91155b6c/Singularity
collection: qbicsoftware/qbic-singularity-varscan
---

# qbicsoftware/qbic-singularity-varscan:v2.4.2

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-varscan:v2.4.2
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/varscan:2.4.2--1
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    VARSCAN=2.4.2
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-varscan](https://github.com/qbicsoftware/qbic-singularity-varscan)
 - License: None

