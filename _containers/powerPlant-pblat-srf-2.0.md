---
id: 7305
name: "powerPlant/pblat-srf"
branch: "master"
tag: "2.0"
commit: "768d1bb5a23e5728e084afedeae8f81d9d644b86"
version: "c8671c95dc771912921e741805c2f465"
build_date: "2019-02-19T08:13:34.119Z"
size_mb: 106
size: 48791583
sif: "https://datasets.datalad.org/shub/powerPlant/pblat-srf/2.0/2019-02-19-768d1bb5-c8671c95/c8671c95dc771912921e741805c2f465.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/pblat-srf/2.0/2019-02-19-768d1bb5-c8671c95/
recipe: https://datasets.datalad.org/shub/powerPlant/pblat-srf/2.0/2019-02-19-768d1bb5-c8671c95/Singularity
collection: powerPlant/pblat-srf
---

# powerPlant/pblat-srf:2.0

```bash
$ singularity pull shub://powerPlant/pblat-srf:2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 2.0

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install gcc libssl-dev make wget zlib1g-dev

  ## Build
  cd /opt
  wget https://github.com/icebert/pblat/archive/2.0.tar.gz
  tar -xzf 2.0.tar.gz
  cd pblat-2.0
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

