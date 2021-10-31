---
id: 6888
name: "powerPlant/angsd-srf"
branch: "master"
tag: "0.917"
commit: "cc40b6c8a3d8021ed5df2aa40f18c5a0e9993ceb"
version: "62a2b569253d4dde25da972bf7df64e2"
build_date: "2019-02-07T08:10:41.399Z"
size_mb: 142
size: 59420703
sif: "https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.917/2019-02-07-cc40b6c8-62a2b569/62a2b569253d4dde25da972bf7df64e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/angsd-srf/0.917/2019-02-07-cc40b6c8-62a2b569/
recipe: https://datasets.datalad.org/shub/powerPlant/angsd-srf/0.917/2019-02-07-cc40b6c8-62a2b569/Singularity
collection: powerPlant/angsd-srf
---

# powerPlant/angsd-srf:0.917

```bash
$ singularity pull shub://powerPlant/angsd-srf:0.917
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 0.917

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ gcc libbz2-dev libcurl4 libcurl4-openssl-dev libhts2 libhts-dev libssl-dev libzip4 libzip-dev make wget

  cd /opt
  wget https://github.com/ANGSD/angsd/archive/0.917.tar.gz
  tar -xzf 0.917.tar.gz
  cd angsd-0.917
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

