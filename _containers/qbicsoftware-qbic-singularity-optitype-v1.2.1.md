---
id: 1803
name: "qbicsoftware/qbic-singularity-optitype"
branch: "master"
tag: "v1.2.1"
commit: "a53ca92323de758d2679e0490489cc01f08df1fd"
version: "2983d9060362e212af9de91ddb35c4d5"
build_date: "2018-02-23T10:06:41.395Z"
size_mb: 1290
size: 375439391
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/v1.2.1/2018-02-23-a53ca923-2983d906/2983d9060362e212af9de91ddb35c4d5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-optitype/v1.2.1/2018-02-23-a53ca923-2983d906/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/v1.2.1/2018-02-23-a53ca923-2983d906/Singularity
collection: qbicsoftware/qbic-singularity-optitype
---

# qbicsoftware/qbic-singularity-optitype:v1.2.1

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-optitype:v1.2.1
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

