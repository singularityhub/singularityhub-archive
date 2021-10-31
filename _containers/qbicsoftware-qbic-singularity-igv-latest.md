---
id: 1828
name: "qbicsoftware/qbic-singularity-igv"
branch: "master"
tag: "latest"
commit: "e8b0baf2adec61aa8425e1bbb78fdb1e2718ba5e"
version: "958c8c3762c53f8c4b9f27ce5246494c"
build_date: "2019-08-20T00:30:51.474Z"
size_mb: 200
size: 108703775
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-igv/latest/2019-08-20-e8b0baf2-958c8c37/958c8c3762c53f8c4b9f27ce5246494c.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-igv/latest/2019-08-20-e8b0baf2-958c8c37/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-igv/latest/2019-08-20-e8b0baf2-958c8c37/Singularity
collection: qbicsoftware/qbic-singularity-igv
---

# qbicsoftware/qbic-singularity-igv:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-igv:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/igv:2.4.6--0
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    IGV=2.4.6
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-igv](https://github.com/qbicsoftware/qbic-singularity-igv)
 - License: [MIT License](https://api.github.com/licenses/mit)

