---
id: 1877
name: "qbicsoftware/qbic-singularity-razers3"
branch: "master"
tag: "latest"
commit: "ae2464b8af4f6244594f74a792041f463e98a379"
version: "1f354ec328a458459f5d9f5d7f9d6743"
build_date: "2018-02-27T17:10:25.414Z"
size_mb: 47
size: 15167519
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-razers3/latest/2018-02-27-ae2464b8-1f354ec3/1f354ec328a458459f5d9f5d7f9d6743.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-razers3/latest/2018-02-27-ae2464b8-1f354ec3/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-razers3/latest/2018-02-27-ae2464b8-1f354ec3/Singularity
collection: qbicsoftware/qbic-singularity-razers3
---

# qbicsoftware/qbic-singularity-razers3:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-razers3:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/razers3:3.5.3--0
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    RAZERS3=3.5.3
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-razers3](https://github.com/qbicsoftware/qbic-singularity-razers3)
 - License: [MIT License](https://api.github.com/licenses/mit)

