---
id: 1829
name: "qbicsoftware/qbic-singularity-igv"
branch: "master"
tag: "v2.4.6"
commit: "e8b0baf2adec61aa8425e1bbb78fdb1e2718ba5e"
version: "347856bdc584b480356223b6bb6a5648"
build_date: "2018-02-23T14:00:14.694Z"
size_mb: 200
size: 108703775
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-igv/v2.4.6/2018-02-23-e8b0baf2-347856bd/347856bdc584b480356223b6bb6a5648.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-igv/v2.4.6/2018-02-23-e8b0baf2-347856bd/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-igv/v2.4.6/2018-02-23-e8b0baf2-347856bd/Singularity
collection: qbicsoftware/qbic-singularity-igv
---

# qbicsoftware/qbic-singularity-igv:v2.4.6

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-igv:v2.4.6
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

