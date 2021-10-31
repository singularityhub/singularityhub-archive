---
id: 868
name: "qbicsoftware/qbic-singularity-salmon"
branch: "master"
tag: "v0.8.2"
commit: "5f1cc6a462d581c8605b81223fb016f47c42d110"
version: "7ecb78f11bef3bdf17db0defe6ac5cee"
build_date: "2017-11-21T09:20:46.828Z"
size_mb: 671
size: 132612127
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-salmon/v0.8.2/2017-11-21-5f1cc6a4-7ecb78f1/7ecb78f11bef3bdf17db0defe6ac5cee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-salmon/v0.8.2/2017-11-21-5f1cc6a4-7ecb78f1/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-salmon/v0.8.2/2017-11-21-5f1cc6a4-7ecb78f1/Singularity
collection: qbicsoftware/qbic-singularity-salmon
---

# qbicsoftware/qbic-singularity-salmon:v0.8.2

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-salmon:v0.8.2
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh

%files
#Installation of Salmon
build.sh

%environment
    SALMON_VERSION=v0.8.2

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-salmon](https://github.com/qbicsoftware/qbic-singularity-salmon)
 - License: None

