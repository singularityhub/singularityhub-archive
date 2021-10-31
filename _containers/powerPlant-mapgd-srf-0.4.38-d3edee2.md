---
id: 7073
name: "powerPlant/mapgd-srf"
branch: "master"
tag: "0.4.38-d3edee2"
commit: "aa19c40ae6a33c4844f5b39c39fb793d722a8a2c"
version: "46c33a7267dc1ab20462b6c8ad67b176"
build_date: "2019-02-11T09:20:46.039Z"
size_mb: 161
size: 64966687
sif: "https://datasets.datalad.org/shub/powerPlant/mapgd-srf/0.4.38-d3edee2/2019-02-11-aa19c40a-46c33a72/46c33a7267dc1ab20462b6c8ad67b176.simg"
url: https://datasets.datalad.org/shub/powerPlant/mapgd-srf/0.4.38-d3edee2/2019-02-11-aa19c40a-46c33a72/
recipe: https://datasets.datalad.org/shub/powerPlant/mapgd-srf/0.4.38-d3edee2/2019-02-11-aa19c40a-46c33a72/Singularity
collection: powerPlant/mapgd-srf
---

# powerPlant/mapgd-srf:0.4.38-d3edee2

```bash
$ singularity pull shub://powerPlant/mapgd-srf:0.4.38-d3edee2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 0.4.38-d3edee2

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install g++ git gettext libgomp1 libgsl-dev libgsl23 libgslcblas0 libhts2 libhts-dev libsqlite3-0 libsqlite3-dev make zlib1g-dev

  git clone https://github.com/LynchLab/MAPGD.git
  cd /MAPGD
  git checkout d3edee2
  ./configure
  make && make install

  ## Cleanup
  apt-get -y remove g++ git gettext libgsl-dev libhts-dev libsqlite3-dev make
  apt-get -y autoremove
  apt-get -y clean all
  rm -rf /MAPGD*

%runscript
 exec mapgd "$@"
```

## Collection

 - Name: [powerPlant/mapgd-srf](https://github.com/powerPlant/mapgd-srf)
 - License: None

