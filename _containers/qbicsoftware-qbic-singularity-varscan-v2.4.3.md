---
id: 1826
name: "qbicsoftware/qbic-singularity-varscan"
branch: "master"
tag: "v2.4.3"
commit: "8009459c4fd08587935496d93ea24729920ddcf4"
version: "5f5315ee9bf982459fe202d5e42171fa"
build_date: "2018-02-23T14:00:14.666Z"
size_mb: 169
size: 78606367
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/v2.4.3/2018-02-23-8009459c-5f5315ee/5f5315ee9bf982459fe202d5e42171fa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-varscan/v2.4.3/2018-02-23-8009459c-5f5315ee/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-varscan/v2.4.3/2018-02-23-8009459c-5f5315ee/Singularity
collection: qbicsoftware/qbic-singularity-varscan
---

# qbicsoftware/qbic-singularity-varscan:v2.4.3

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-varscan:v2.4.3
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

