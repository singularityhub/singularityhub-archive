---
id: 887
name: "qbicsoftware/qbic-singularity-diamond"
branch: "master"
tag: "template"
commit: "f673418d66a39f0fb9cdde8039fa50f3a021a7ca"
version: "c1fab208e0931d4eb3c0ff271f9284e2"
build_date: "2017-11-21T18:32:11.766Z"
size_mb: 399
size: 81317919
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-diamond/template/2017-11-21-f673418d-c1fab208/c1fab208e0931d4eb3c0ff271f9284e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-diamond/template/2017-11-21-f673418d-c1fab208/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-diamond/template/2017-11-21-f673418d-c1fab208/Singularity
collection: qbicsoftware/qbic-singularity-diamond
---

# qbicsoftware/qbic-singularity-diamond:template

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-diamond:template
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

 - Name: [qbicsoftware/qbic-singularity-diamond](https://github.com/qbicsoftware/qbic-singularity-diamond)
 - License: None

