---
id: 6948
name: "powerPlant/angsd-srf"
branch: "master"
tag: "0.922"
commit: "cc5e9efa024a6c72e654aefe8b2dfafa8fbe648d"
version: "7c2306889a950ec91f1956665e1341fb"
build_date: "2019-02-07T08:10:41.368Z"
size_mb: 142
size: 59465759
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.922/2019-02-07-cc5e9efa-7c230688/7c2306889a950ec91f1956665e1341fb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/angsd-srf/0.922/2019-02-07-cc5e9efa-7c230688/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.922/2019-02-07-cc5e9efa-7c230688/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:0.922

```bash
$ singularity pull shub://powerPlant/angsd-srf:0.922
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.922

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ gcc libbz2-dev libcurl4 libcurl4-openssl-dev libhts2 libhts-dev libssl-dev libzip4 libzip-dev make wget

  cd /opt
  wget https://github.com/ANGSD/angsd/archive/0.922.tar.gz
  tar -xzf 0.922.tar.gz
  cd angsd-0.922
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

