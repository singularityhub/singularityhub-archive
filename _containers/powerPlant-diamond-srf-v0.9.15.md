---
id: 7079
name: "powerPlant/diamond-srf"
branch: "master"
tag: "v0.9.15"
commit: "b857eddc55a38b76b994c02365e7f2eac3ebfb91"
version: "d630ef470b63f5f7e8f8535f69cdfb17"
build_date: "2019-02-11T09:20:46.083Z"
size_mb: 109
size: 50511903
sif: "https://datasets.datalad.org/shub/powerPlant/diamond-srf/v0.9.15/2019-02-11-b857eddc-d630ef47/d630ef470b63f5f7e8f8535f69cdfb17.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/diamond-srf/v0.9.15/2019-02-11-b857eddc-d630ef47/
recipe: https://datasets.datalad.org/shub/powerPlant/diamond-srf/v0.9.15/2019-02-11-b857eddc-d630ef47/Singularity
collection: powerPlant/diamond-srf
---

# powerPlant/diamond-srf:v0.9.15

```bash
$ singularity pull shub://powerPlant/diamond-srf:v0.9.15
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version v0.9.15

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install wget
  cd /opt
  wget http://github.com/bbuchfink/diamond/releases/download/v0.9.15/diamond-linux64.tar.gz
  tar -xzf diamond-linux64.tar.gz
  
 
  ## Cleanup
  rm -rf /opt/diamond-linux64.tar.gz
  apt-get -y remove wget
  apt-get -y autoremove
  apt-get -y clean all

%runscript
 exec /opt/diamond "$@"
```

## Collection

 - Name: [powerPlant/diamond-srf](https://github.com/powerPlant/diamond-srf)
 - License: None

