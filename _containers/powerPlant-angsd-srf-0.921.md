---
id: 6947
name: "powerPlant/angsd-srf"
branch: "master"
tag: "0.921"
commit: "cc5e9efa024a6c72e654aefe8b2dfafa8fbe648d"
version: "de42503709804343cc1a1bc8d071cd25"
build_date: "2019-02-07T08:10:41.374Z"
size_mb: 141
size: 59359263
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.921/2019-02-07-cc5e9efa-de425037/de42503709804343cc1a1bc8d071cd25.simg"
url: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.921/2019-02-07-cc5e9efa-de425037/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.921/2019-02-07-cc5e9efa-de425037/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:0.921

```bash
$ singularity pull shub://powerPlant/angsd-srf:0.921
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.921

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ gcc libbz2-dev libcurl4 libcurl4-openssl-dev libhts2 libhts-dev libssl-dev libzip4 libzip-dev make wget

  cd /opt
  wget https://github.com/ANGSD/angsd/archive/0.921.tar.gz
  tar -xzf 0.921.tar.gz
  cd angsd-0.921
  make
  make install

  ## Cleanup
  apt-get -y autoremove g++ gcc libcurl4-openssl-dev libhts-dev libssl-dev libzip-dev make wget
  apt-get -y clean all
  rm -rf /opt/*

%runscript
  exec angsd "$@"
```

## Collection

 - Name: [powerPlant/angsd-srf](https://github.com/powerPlant/angsd-srf)
 - License: None

