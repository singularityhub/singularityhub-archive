---
id: 1802
name: "qbicsoftware/qbic-singularity-optitype"
branch: "master"
tag: "v1.2"
commit: "a53ca92323de758d2679e0490489cc01f08df1fd"
version: "964c7c2ba66e4490b8d422fab802ed6c"
build_date: "2018-02-22T15:06:01.952Z"
size_mb: 1354
size: 394641439
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/v1.2/2018-02-22-a53ca923-964c7c2b/964c7c2ba66e4490b8d422fab802ed6c.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/v1.2/2018-02-22-a53ca923-964c7c2b/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-optitype/v1.2/2018-02-22-a53ca923-964c7c2b/Singularity
collection: qbicsoftware/qbic-singularity-optitype
---

# qbicsoftware/qbic-singularity-optitype:v1.2

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-optitype:v1.2
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/optitype:1.2--py35_0
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    OPTITYPE=1.2
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-optitype](https://github.com/qbicsoftware/qbic-singularity-optitype)
 - License: None

