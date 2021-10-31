---
id: 7256
name: "powerPlant/survivor-srf"
branch: "master"
tag: "latest"
commit: "0cb9c5e43178a3e21e065c130587cab2989111fa"
version: "d1fe39c213a6b4bba3a0b131b9ac7ca0"
build_date: "2019-02-15T05:11:19.345Z"
size_mb: 175
size: 65699871
sif: "https://datasets.datalad.org/shub/powerPlant/survivor-srf/latest/2019-02-15-0cb9c5e4-d1fe39c2/d1fe39c213a6b4bba3a0b131b9ac7ca0.simg"
url: https://datasets.datalad.org/shub/powerPlant/survivor-srf/latest/2019-02-15-0cb9c5e4-d1fe39c2/
recipe: https://datasets.datalad.org/shub/powerPlant/survivor-srf/latest/2019-02-15-0cb9c5e4-d1fe39c2/Singularity
collection: powerPlant/survivor-srf
---

# powerPlant/survivor-srf:latest

```bash
$ singularity pull shub://powerPlant/survivor-srf:latest
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

