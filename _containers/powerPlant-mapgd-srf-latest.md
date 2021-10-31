---
id: 7076
name: "powerPlant/mapgd-srf"
branch: "master"
tag: "latest"
commit: "daddeab2e9e5bac7c6f815d8e05d300276eb3bc3"
version: "10bd732bcf7d3f22c92cd28fcd757e75"
build_date: "2019-02-11T09:20:46.034Z"
size_mb: 161
size: 64966687
sif: "https://datasets.datalad.org/shub/powerPlant/mapgd-srf/latest/2019-02-11-daddeab2-10bd732b/10bd732bcf7d3f22c92cd28fcd757e75.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/mapgd-srf/latest/2019-02-11-daddeab2-10bd732b/
recipe: https://datasets.datalad.org/shub/powerPlant/mapgd-srf/latest/2019-02-11-daddeab2-10bd732b/Singularity
collection: powerPlant/mapgd-srf
---

# powerPlant/mapgd-srf:latest

```bash
$ singularity pull shub://powerPlant/mapgd-srf:latest
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

