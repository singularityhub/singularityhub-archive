---
id: 6945
name: "powerPlant/angsd-srf"
branch: "master"
tag: "0.925"
commit: "cc40b6c8a3d8021ed5df2aa40f18c5a0e9993ceb"
version: "31528a971c5ebe4c6c0fa01998375db3"
build_date: "2019-02-07T08:10:41.380Z"
size_mb: 142
size: 59486239
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.925/2019-02-07-cc40b6c8-31528a97/31528a971c5ebe4c6c0fa01998375db3.simg"
url: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.925/2019-02-07-cc40b6c8-31528a97/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.925/2019-02-07-cc40b6c8-31528a97/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:0.925

```bash
$ singularity pull shub://powerPlant/angsd-srf:0.925
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

