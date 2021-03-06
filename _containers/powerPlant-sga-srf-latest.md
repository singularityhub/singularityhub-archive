---
id: 12018
name: "powerPlant/sga-srf"
branch: "master"
tag: "latest"
commit: "99d433982b8db60122ee51c7613c3deef673a115"
version: "9db152a2c67104a3577bb1668b40e04cea9dffc43c9804e0065b683689699b4d"
build_date: "2020-01-17T03:38:37.848Z"
size_mb: 177.859375
size: 186499072
sif: "https://datasets.datalad.org/shub/powerPlant/sga-srf/latest/2020-01-17-99d43398-9db152a2/9db152a2c67104a3577bb1668b40e04cea9dffc43c9804e0065b683689699b4d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/sga-srf/latest/2020-01-17-99d43398-9db152a2/
recipe: https://datasets.datalad.org/shub/powerPlant/sga-srf/latest/2020-01-17-99d43398-9db152a2/Singularity
collection: powerPlant/sga-srf
---

# powerPlant/sga-srf:latest

```bash
$ singularity pull shub://powerPlant/sga-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty

%labels
Maintainer @plantandfood.co.nz
Version 0.10.15

%post
  ## Download build prerequisites
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get -y install automake autotools-dev build-essential cmake libhts-dev libjemalloc-dev libsparsehash-dev libz-dev python-matplotlib wget zlib1g-dev
  
  ## Build bamtools
  cd /opt
  wget https://github.com/pezmaster31/bamtools/archive/v2.4.0.tar.gz
  tar -xzvf v2.4.0.tar.gz
  rm -f v2.4.0.tar.gz
  cd bamtools-2.4.0
  mkdir build
  cd build
  cmake ..
  make

  ## Build SGA
  cd /opt
  wget https://github.com/jts/sga/archive/v0.10.15.tar.gz
  tar -xzvf v0.10.15.tar.gz
  rm -f v0.10.15.tar.gz
  cd sga-0.10.15/src
  ./autogen.sh
  ./configure --with-bamtools=/opt/bamtools-2.4.0 --with-jemalloc=/usr --prefix=/usr/local
  make
  make install

%runscript
  exec sga "$@"
```

## Collection

 - Name: [powerPlant/sga-srf](https://github.com/powerPlant/sga-srf)
 - License: None

