---
id: 1824
name: "qbicsoftware/qbic-singularity-varscan"
branch: "master"
tag: "latest"
commit: "8009459c4fd08587935496d93ea24729920ddcf4"
version: "483f017dd184aecd83ee080c2b30ee9a"
build_date: "2020-03-10T21:09:41.991Z"
size_mb: 169
size: 78606367
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/latest/2020-03-10-8009459c-483f017d/483f017dd184aecd83ee080c2b30ee9a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-varscan/latest/2020-03-10-8009459c-483f017d/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/latest/2020-03-10-8009459c-483f017d/Singularity
collection: qbicsoftware/qbic-singularity-varscan
---

# qbicsoftware/qbic-singularity-varscan:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-varscan:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/varscan:2.4.3--0
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    VARSCAN=2.4.3
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-varscan](https://github.com/qbicsoftware/qbic-singularity-varscan)
 - License: None

