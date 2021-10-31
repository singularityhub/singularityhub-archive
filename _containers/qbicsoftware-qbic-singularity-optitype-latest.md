---
id: 1801
name: "qbicsoftware/qbic-singularity-optitype"
branch: "master"
tag: "latest"
commit: "a53ca92323de758d2679e0490489cc01f08df1fd"
version: "ba8333cf3c7f248f3293764d3ca20543"
build_date: "2020-03-30T11:17:44.868Z"
size_mb: 1290
size: 375439391
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/latest/2020-03-30-a53ca923-ba8333cf/ba8333cf3c7f248f3293764d3ca20543.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-optitype/latest/2020-03-30-a53ca923-ba8333cf/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/latest/2020-03-30-a53ca923-ba8333cf/Singularity
collection: qbicsoftware/qbic-singularity-optitype
---

# qbicsoftware/qbic-singularity-optitype:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-optitype:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/optitype:1.2.1--py27_0
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    OPTITYPE=1.2.1
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-optitype](https://github.com/qbicsoftware/qbic-singularity-optitype)
 - License: None

