---
id: 6887
name: "powerPlant/angsd-srf"
branch: "master"
tag: "latest"
commit: "cc5e9efa024a6c72e654aefe8b2dfafa8fbe648d"
version: "88476175965f7af52893ae900647f229e287bc0a38e1a04a82ad61db75d2a2af"
build_date: "2020-06-08T21:39:22.927Z"
size_mb: 57.7578125
size: 60563456
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/latest/2020-06-08-cc5e9efa-88476175/88476175965f7af52893ae900647f229e287bc0a38e1a04a82ad61db75d2a2af.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/angsd-srf/latest/2020-06-08-cc5e9efa-88476175/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/latest/2020-06-08-cc5e9efa-88476175/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:latest

```bash
$ singularity pull shub://powerPlant/angsd-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.925

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ gcc libbz2-dev libcurl4 libcurl4-openssl-dev libhts2 libhts-dev libssl-dev libzip4 libzip-dev make wget

  cd /opt
  wget https://github.com/ANGSD/angsd/archive/0.925.tar.gz
  tar -xzf 0.925.tar.gz
  cd angsd-0.925
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

