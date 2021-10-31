---
id: 6849
name: "powerPlant/abyss-srf"
branch: "master"
tag: "2.1.5"
commit: "c36f714ed5b0d6006fbbe410d40124daee458445"
version: "f8242d27cdc5bc6a150d18ed90647167"
build_date: "2019-07-18T14:51:58.111Z"
size_mb: 158
size: 59052063
sif: "https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.5/2019-07-18-c36f714e-f8242d27/f8242d27cdc5bc6a150d18ed90647167.simg"
url: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.5/2019-07-18-c36f714e-f8242d27/
recipe: https://datasets.datalad.org/shub/powerPlant/abyss-srf/2.1.5/2019-07-18-c36f714e-f8242d27/Singularity
collection: powerPlant/abyss-srf
---

# powerPlant/abyss-srf:2.1.5

```bash
$ singularity pull shub://powerPlant/abyss-srf:2.1.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:disco

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.1.5

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

