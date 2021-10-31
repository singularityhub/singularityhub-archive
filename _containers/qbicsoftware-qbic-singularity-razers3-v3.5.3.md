---
id: 1878
name: "qbicsoftware/qbic-singularity-razers3"
branch: "master"
tag: "v3.5.3"
commit: "ae2464b8af4f6244594f74a792041f463e98a379"
version: "104ee1657be07b253d8dc1fc74c351eb"
build_date: "2018-02-27T17:10:25.406Z"
size_mb: 47
size: 15167519
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-razers3/v3.5.3/2018-02-27-ae2464b8-104ee165/104ee1657be07b253d8dc1fc74c351eb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-razers3/v3.5.3/2018-02-27-ae2464b8-104ee165/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-razers3/v3.5.3/2018-02-27-ae2464b8-104ee165/Singularity
collection: qbicsoftware/qbic-singularity-razers3
---

# qbicsoftware/qbic-singularity-razers3:v3.5.3

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-razers3:v3.5.3
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

