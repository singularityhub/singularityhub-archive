---
id: 6884
name: "powerPlant/abyss-srf"
branch: "master"
tag: "2.1.3"
commit: "c36f714ed5b0d6006fbbe410d40124daee458445"
version: "0662e0c669398d3cba958cd20f391d64"
build_date: "2019-02-05T05:54:32.345Z"
size_mb: 153
size: 58646559
sif: "https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.3/2019-02-05-c36f714e-0662e0c6/0662e0c669398d3cba958cd20f391d64.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/abyss-srf/2.1.3/2019-02-05-c36f714e-0662e0c6/
recipe: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.3/2019-02-05-c36f714e-0662e0c6/Singularity
collection: powerPlant/abyss-srf
---

# powerPlant/abyss-srf:2.1.3

```bash
$ singularity pull shub://powerPlant/abyss-srf:2.1.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:cosmic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.1.3

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

