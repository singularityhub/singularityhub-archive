---
id: 1832
name: "qbicsoftware/qbic-singularity-malt"
branch: "master"
tag: "latest"
commit: "9088bfc4c9d7c419e78d0da68851c52caaa81235"
version: "34927f97d83acb0b02bfff0f35f62426"
build_date: "2018-02-26T23:07:29.410Z"
size_mb: 556
size: 244863007
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-malt/latest/2018-02-26-9088bfc4-34927f97/34927f97d83acb0b02bfff0f35f62426.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-malt/latest/2018-02-26-9088bfc4-34927f97/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-malt/latest/2018-02-26-9088bfc4-34927f97/Singularity
collection: qbicsoftware/qbic-singularity-malt
---

# qbicsoftware/qbic-singularity-malt:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-malt:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:16.04

%post
/bin/sh build.sh

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    MALT_VERSION=v0_4_0

%runscript
exec malt-run "$@"

%test
java -version

%labels
Maintainer  sven.fillinger@qbic.uni-tuebingen.de+
Organization    Quantitative Biology Center (QBiC)
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-malt](https://github.com/qbicsoftware/qbic-singularity-malt)
 - License: [MIT License](https://api.github.com/licenses/mit)

