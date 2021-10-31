---
id: 6889
name: "powerPlant/angsd-srf"
branch: "master"
tag: "0.918"
commit: "cc40b6c8a3d8021ed5df2aa40f18c5a0e9993ceb"
version: "1c61569dddc0b84da21fe06bc28359e4"
build_date: "2019-02-07T08:10:41.393Z"
size_mb: 142
size: 59432991
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.918/2019-02-07-cc40b6c8-1c61569d/1c61569dddc0b84da21fe06bc28359e4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/angsd-srf/0.918/2019-02-07-cc40b6c8-1c61569d/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.918/2019-02-07-cc40b6c8-1c61569d/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:0.918

```bash
$ singularity pull shub://powerPlant/angsd-srf:0.918
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.918

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ gcc libbz2-dev libcurl4 libcurl4-openssl-dev libhts2 libhts-dev libssl-dev libzip4 libzip-dev make wget

  cd /opt
  wget https://github.com/ANGSD/angsd/archive/0.918.tar.gz
  tar -xzf 0.918.tar.gz
  cd angsd-0.918
  make
  install -dm0755 /usr/local/bin
  install -Dm0755 angsd /usr/local/bin
  cd misc
  install -Dm0755 thetaStat realSFS /usr/local/bin

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

