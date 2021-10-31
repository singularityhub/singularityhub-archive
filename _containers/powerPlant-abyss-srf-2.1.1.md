---
id: 6882
name: "powerPlant/abyss-srf"
branch: "master"
tag: "2.1.1"
commit: "c36f714ed5b0d6006fbbe410d40124daee458445"
version: "8e29f9bc08c0598e949bcb7141501604"
build_date: "2019-02-05T05:54:32.357Z"
size_mb: 153
size: 58646559
sif: "https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.1/2019-02-05-c36f714e-8e29f9bc/8e29f9bc08c0598e949bcb7141501604.simg"
url: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.1/2019-02-05-c36f714e-8e29f9bc/
recipe: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.1/2019-02-05-c36f714e-8e29f9bc/Singularity
collection: powerPlant/abyss-srf
---

# powerPlant/abyss-srf:2.1.1

```bash
$ singularity pull shub://powerPlant/abyss-srf:2.1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:cosmic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.1.1

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

