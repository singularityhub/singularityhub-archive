---
id: 1804
name: "qbicsoftware/qbic-singularity-freebayes"
branch: "master"
tag: "latest"
commit: "1fd4d5e80b9cd1bbaf03dde5f8083e3f6eeda410"
version: "fbaddd0ae75fc371b8b196ac2a7274aa"
build_date: "2018-02-22T15:06:01.991Z"
size_mb: 264
size: 76918815
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-freebayes/latest/2018-02-22-1fd4d5e8-fbaddd0a/fbaddd0ae75fc371b8b196ac2a7274aa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-freebayes/latest/2018-02-22-1fd4d5e8-fbaddd0a/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-freebayes/latest/2018-02-22-1fd4d5e8-fbaddd0a/Singularity
collection: qbicsoftware/qbic-singularity-freebayes
---

# qbicsoftware/qbic-singularity-freebayes:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-freebayes:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/freebayes:1.1.0.46--htslib1.7_3
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    FREEBAYES=1.1.0.46
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-freebayes](https://github.com/qbicsoftware/qbic-singularity-freebayes)
 - License: None

