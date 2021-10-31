---
id: 748
name: "qbicsoftware/qbic-singularity-cutadapt"
branch: "master"
tag: "v1.14"
commit: "3ab2540ca18a53d7f749034cd1b32a6cb7e9a3f5"
version: "425c9b0ecacd78f66bc36edd0297541b"
build_date: "2017-11-09T13:22:23.837Z"
size_mb: 404
size: 81973279
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-cutadapt/v1.14/2017-11-09-3ab2540c-425c9b0e/425c9b0ecacd78f66bc36edd0297541b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-cutadapt/v1.14/2017-11-09-3ab2540c-425c9b0e/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-cutadapt/v1.14/2017-11-09-3ab2540c-425c9b0e/Singularity
collection: qbicsoftware/qbic-singularity-cutadapt
---

# qbicsoftware/qbic-singularity-cutadapt:v1.14

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-cutadapt:v1.14
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    <TOOL>_VERSION=v1.0

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-cutadapt](https://github.com/qbicsoftware/qbic-singularity-cutadapt)
 - License: None

