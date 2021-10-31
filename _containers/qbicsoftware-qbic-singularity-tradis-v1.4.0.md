---
id: 1474
name: "qbicsoftware/qbic-singularity-tradis"
branch: "master"
tag: "v1.4.0"
commit: "9f2e703caf0cf5646660e5245b5921b8f8572991"
version: "a45f5487d1981d9f7639af396a4cb44a"
build_date: "2018-01-25T14:23:39.347Z"
size_mb: 1537
size: 643932191
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tradis/v1.4.0/2018-01-25-9f2e703c-a45f5487/a45f5487d1981d9f7639af396a4cb44a.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tradis/v1.4.0/2018-01-25-9f2e703c-a45f5487/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-tradis/v1.4.0/2018-01-25-9f2e703c-a45f5487/Singularity
collection: qbicsoftware/qbic-singularity-tradis
---

# qbicsoftware/qbic-singularity-tradis:v1.4.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-tradis:v1.4.0
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

