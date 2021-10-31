---
id: 7257
name: "powerPlant/survivor-srf"
branch: "master"
tag: "1.0.5"
commit: "0cb9c5e43178a3e21e065c130587cab2989111fa"
version: "4d3e362b224c447bd275f5139caec023"
build_date: "2019-02-15T05:11:19.338Z"
size_mb: 175
size: 65699871
sif: "https://datasets.datalad.org/shub/powerPlant/survivor-srf/1.0.5/2019-02-15-0cb9c5e4-4d3e362b/4d3e362b224c447bd275f5139caec023.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/survivor-srf/1.0.5/2019-02-15-0cb9c5e4-4d3e362b/
recipe: https://datasets.datalad.org/shub/powerPlant/survivor-srf/1.0.5/2019-02-15-0cb9c5e4-4d3e362b/Singularity
collection: powerPlant/survivor-srf
---

# powerPlant/survivor-srf:1.0.5

```bash
$ singularity pull shub://powerPlant/survivor-srf:1.0.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.0.5

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install build-essential wget 

 cd /opt
 wget https://github.com/fritzsedlazeck/SURVIVOR/archive/v1.0.5.tar.gz
 tar -xvf v1.0.5.tar.gz
 cd SURVIVOR-1.0.5/Debug
 make

 ## Cleanup
  rm -rf /opt/v1.0.5.tar.gz
  apt-get remove build-essential wget -y
  apt-get autoremove -y
  apt-get -y clean all

%runscript
  exec /opt/SURVIVOR-1.0.5/Debug/SURVIVOR "$@"
```

## Collection

 - Name: [powerPlant/survivor-srf](https://github.com/powerPlant/survivor-srf)
 - License: None

