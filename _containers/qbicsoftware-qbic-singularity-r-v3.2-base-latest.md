---
id: 1766
name: "qbicsoftware/qbic-singularity-r-v3.2-base"
branch: "master"
tag: "latest"
commit: "10625d54981c5d0c72abcda22163295830fb5d48"
version: "e877cfd5c4d7999acd309347c9c71f5c"
build_date: "2018-02-19T11:09:57.216Z"
size_mb: 942
size: 333893663
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-r-v3.2-base/latest/2018-02-19-10625d54-e877cfd5/e877cfd5c4d7999acd309347c9c71f5c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-r-v3.2-base/latest/2018-02-19-10625d54-e877cfd5/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-r-v3.2-base/latest/2018-02-19-10625d54-e877cfd5/Singularity
collection: qbicsoftware/qbic-singularity-r-v3.2-base
---

# qbicsoftware/qbic-singularity-r-v3.2-base:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-r-v3.2-base:latest
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
    R_VERSION=v3.2.3-4

%labels
Maintainer	sven.fillinger@qbic.uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-r-v3.2-base](https://github.com/qbicsoftware/qbic-singularity-r-v3.2-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

