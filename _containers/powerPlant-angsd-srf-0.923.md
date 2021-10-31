---
id: 6891
name: "powerPlant/angsd-srf"
branch: "master"
tag: "0.923"
commit: "714757936007cfa6b1e9a1195b111c6f989ed788"
version: "2c8b1733a03ac5ffff607fe5c137aa71"
build_date: "2019-02-05T05:54:32.689Z"
size_mb: 142
size: 59449375
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.923/2019-02-05-71475793-2c8b1733/2c8b1733a03ac5ffff607fe5c137aa71.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/angsd-srf/0.923/2019-02-05-71475793-2c8b1733/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.923/2019-02-05-71475793-2c8b1733/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:0.923

```bash
$ singularity pull shub://powerPlant/angsd-srf:0.923
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.923

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ gcc libbz2-dev libcurl4 libcurl4-openssl-dev libhts2 libhts-dev libssl-dev libzip4 libzip-dev make wget

  cd /opt
  wget https://github.com/ANGSD/angsd/archive/0.923.tar.gz
  tar -xzf 0.923.tar.gz
  cd angsd-0.923
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

