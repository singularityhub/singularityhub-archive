---
id: 1805
name: "qbicsoftware/qbic-singularity-freebayes"
branch: "master"
tag: "v1.0.2"
commit: "1fd4d5e80b9cd1bbaf03dde5f8083e3f6eeda410"
version: "ab83761784ef2ac363ac5887ae0fab4c"
build_date: "2018-02-22T15:06:01.981Z"
size_mb: 25
size: 8904735
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-freebayes/v1.0.2/2018-02-22-1fd4d5e8-ab837617/ab83761784ef2ac363ac5887ae0fab4c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-freebayes/v1.0.2/2018-02-22-1fd4d5e8-ab837617/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-freebayes/v1.0.2/2018-02-22-1fd4d5e8-ab837617/Singularity
collection: qbicsoftware/qbic-singularity-freebayes
---

# qbicsoftware/qbic-singularity-freebayes:v1.0.2

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-freebayes:v1.0.2
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/freebayes:1.0.2--0
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    FREEBAYES=1.0.2--0
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-freebayes](https://github.com/qbicsoftware/qbic-singularity-freebayes)
 - License: None

