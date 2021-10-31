---
id: 6753
name: "powerPlant/abyss-srf"
branch: "master"
tag: "2.1.0"
commit: "c36f714ed5b0d6006fbbe410d40124daee458445"
version: "429e6ec3b653ebb9c646888bd1bd8bc3"
build_date: "2019-02-05T02:55:37.535Z"
size_mb: 153
size: 58621983
sif: "https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.0/2019-02-05-c36f714e-429e6ec3/429e6ec3b653ebb9c646888bd1bd8bc3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/abyss-srf/2.1.0/2019-02-05-c36f714e-429e6ec3/
recipe: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.0/2019-02-05-c36f714e-429e6ec3/Singularity
collection: powerPlant/abyss-srf
---

# powerPlant/abyss-srf:2.1.0

```bash
$ singularity pull shub://powerPlant/abyss-srf:2.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:cosmic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.1.0

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install abyss
  
  ## Cleanup
  apt-get -y clean all

%runscript
  abyss-pe "$@"
```

## Collection

 - Name: [powerPlant/abyss-srf](https://github.com/powerPlant/abyss-srf)
 - License: None

