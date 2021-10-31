---
id: 11640
name: "powerPlant/mrbayes-srf"
branch: "master"
tag: "3.2.7a"
commit: "172eea0bdf97dd588b70f15ef2924706dff9bfaf"
version: "99197b4846425791f988c6337e06f2e6fb7fa652b088697cf673343af260a74e"
build_date: "2020-09-03T11:47:18.671Z"
size_mb: 104.6796875
size: 109764608
sif: "https://datasets.datalad.org/shub/powerPlant/mrbayes-srf/3.2.7a/2020-09-03-172eea0b-99197b48/99197b4846425791f988c6337e06f2e6fb7fa652b088697cf673343af260a74e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/mrbayes-srf/3.2.7a/2020-09-03-172eea0b-99197b48/
recipe: https://datasets.datalad.org/shub/powerPlant/mrbayes-srf/3.2.7a/2020-09-03-172eea0b-99197b48/Singularity
collection: powerPlant/mrbayes-srf
---

# powerPlant/mrbayes-srf:3.2.7a

```bash
$ singularity pull shub://powerPlant/mrbayes-srf:3.2.7a
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 3.2.7a

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install g++ libhmsbeagle1v5 libhmsbeagle-dev make wget

  ## Build
  cd /opt
  wget https://github.com/NBISweden/MrBayes/releases/download/v3.2.7a/mrbayes-3.2.7a.tar.gz
  tar -xzf mrbayes-3.2.7a.tar.gz
  cd mrbayes-3.2.7a
  ./configure
  make -j`nproc` install

  ## Cleanup
  apt-get -y remove g++ libhmsbeagle-dev make wget
  apt-get -y autoremove
  rm -rf /opt/*

%runscript
  exec mb "$@"
```

## Collection

 - Name: [powerPlant/mrbayes-srf](https://github.com/powerPlant/mrbayes-srf)
 - License: None

