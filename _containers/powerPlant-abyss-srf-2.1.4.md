---
id: 6885
name: "powerPlant/abyss-srf"
branch: "master"
tag: "2.1.4"
commit: "c36f714ed5b0d6006fbbe410d40124daee458445"
version: "3d694b0d0aa30eb04f91ce382d425ed1"
build_date: "2020-03-22T18:20:27.519Z"
size_mb: 153
size: 58646559
sif: "https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.4/2020-03-22-c36f714e-3d694b0d/3d694b0d0aa30eb04f91ce382d425ed1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/abyss-srf/2.1.4/2020-03-22-c36f714e-3d694b0d/
recipe: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.4/2020-03-22-c36f714e-3d694b0d/Singularity
collection: powerPlant/abyss-srf
---

# powerPlant/abyss-srf:2.1.4

```bash
$ singularity pull shub://powerPlant/abyss-srf:2.1.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:cosmic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.1.4

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install abyss
  
  ## Cleanup
  apt-get -y clean all

%runscript
  exec abyss-pe "$@"
```

## Collection

 - Name: [powerPlant/abyss-srf](https://github.com/powerPlant/abyss-srf)
 - License: None

