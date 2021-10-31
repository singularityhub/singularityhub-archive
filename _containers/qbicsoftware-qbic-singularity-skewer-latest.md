---
id: 1879
name: "qbicsoftware/qbic-singularity-skewer"
branch: "master"
tag: "latest"
commit: "8568b77d87ad723e6f652d0e86c01c5ef20dc2a5"
version: "2aec83a4e59fe8df8bccf9e35fbf1bd2"
build_date: "2018-02-27T17:10:25.434Z"
size_mb: 11
size: 4526111
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-skewer/latest/2018-02-27-8568b77d-2aec83a4/2aec83a4e59fe8df8bccf9e35fbf1bd2.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-skewer/latest/2018-02-27-8568b77d-2aec83a4/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-skewer/latest/2018-02-27-8568b77d-2aec83a4/Singularity
collection: qbicsoftware/qbic-singularity-skewer
---

# qbicsoftware/qbic-singularity-skewer:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-skewer:latest
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

