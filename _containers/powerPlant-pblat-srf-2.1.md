---
id: 7306
name: "powerPlant/pblat-srf"
branch: "master"
tag: "2.1"
commit: "768d1bb5a23e5728e084afedeae8f81d9d644b86"
version: "ee90f217c0485b9a9e72368ed411d217"
build_date: "2019-02-19T08:13:34.113Z"
size_mb: 106
size: 48992287
sif: "https://datasets.datalad.org/shub/powerPlant/pblat-srf/2.1/2019-02-19-768d1bb5-ee90f217/ee90f217c0485b9a9e72368ed411d217.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/pblat-srf/2.1/2019-02-19-768d1bb5-ee90f217/
recipe: https://datasets.datalad.org/shub/powerPlant/pblat-srf/2.1/2019-02-19-768d1bb5-ee90f217/Singularity
collection: powerPlant/pblat-srf
---

# powerPlant/pblat-srf:2.1

```bash
$ singularity pull shub://powerPlant/pblat-srf:2.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.1

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gcc libssl-dev make wget zlib1g-dev

  ## Build
  cd /opt
  wget https://github.com/icebert/pblat/archive/2.1.tar.gz
  tar -xzf 2.1.tar.gz
  cd pblat-2.1
  make

  ## Install
  install pblat /usr/local/bin

  ## Cleanup
  cd
  rm -rf /opt/*
  apt-get -y remove gcc libssl-dev make wget zlib1g-dev
  apt-get -y autoremove
  apt-get -y clean all

%runscript
  exec pblat "$@"
```

## Collection

 - Name: [powerPlant/pblat-srf](https://github.com/powerPlant/pblat-srf)
 - License: None

