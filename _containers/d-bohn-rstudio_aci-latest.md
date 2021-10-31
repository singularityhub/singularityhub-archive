---
id: 8634
name: "d-bohn/rstudio_aci"
branch: "master"
tag: "latest"
commit: "b0e04b881304a6280db0a3a36ccaaffbe258f6b7"
version: "d0372e6820a2e0ff22cf8d9e2a6c5d92"
build_date: "2019-10-22T19:05:02.375Z"
size_mb: 3096
size: 1018007583
sif: "https://datasets.datalad.org/shub/d-bohn/rstudio_aci/latest/2019-10-22-b0e04b88-d0372e68/d0372e6820a2e0ff22cf8d9e2a6c5d92.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/d-bohn/rstudio_aci/latest/2019-10-22-b0e04b88-d0372e68/
recipe: https://datasets.datalad.org/shub/d-bohn/rstudio_aci/latest/2019-10-22-b0e04b88-d0372e68/Singularity
collection: d-bohn/rstudio_aci
---

# d-bohn/rstudio_aci:latest

```bash
$ singularity pull shub://d-bohn/rstudio_aci:latest
```

## Singularity Recipe

```singularity
BOOTSTRAP: docker
FROM: dalbohn/rstudio_aci

%labels
MAINTAINER Daniel Albohn <d.albohn@gmail.com>
VERSION v1.2

%post
# ACI mappings so you can access your files.
mkdir -p /storage/home
mkdir -p /storage/work
mkdir -p /gpfs/group
mkdir -p /gpfs/scratch
```

## Collection

 - Name: [d-bohn/rstudio_aci](https://github.com/d-bohn/rstudio_aci)
 - License: None

