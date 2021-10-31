---
id: 1473
name: "qbicsoftware/qbic-singularity-tradis"
branch: "master"
tag: "latest"
commit: "9f2e703caf0cf5646660e5245b5921b8f8572991"
version: "18d1f0e98036267800416782b0ab13a1"
build_date: "2018-01-25T14:23:39.338Z"
size_mb: 1536
size: 643932191
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tradis/latest/2018-01-25-9f2e703c-18d1f0e9/18d1f0e98036267800416782b0ab13a1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-tradis/latest/2018-01-25-9f2e703c-18d1f0e9/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tradis/latest/2018-01-25-9f2e703c-18d1f0e9/Singularity
collection: qbicsoftware/qbic-singularity-tradis
---

# qbicsoftware/qbic-singularity-tradis:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-tradis:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:17.10

%post
/bin/sh build.sh


%files
#Installation of deps
build.sh



%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    TRADIS_VERSION=v1.4.0
    LC_ALL="C"
    PATH="/usr/bin/miniconda/bin:$PATH"

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-tradis](https://github.com/qbicsoftware/qbic-singularity-tradis)
 - License: [MIT License](https://api.github.com/licenses/mit)

