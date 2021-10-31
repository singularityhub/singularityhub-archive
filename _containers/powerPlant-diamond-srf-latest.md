---
id: 7078
name: "powerPlant/diamond-srf"
branch: "master"
tag: "latest"
commit: "b857eddc55a38b76b994c02365e7f2eac3ebfb91"
version: "29123ad352dccebc03bd04bd1c9d7298"
build_date: "2019-02-11T09:20:46.089Z"
size_mb: 112
size: 50950175
sif: "https://datasets.datalad.org/shub/powerPlant/diamond-srf/latest/2019-02-11-b857eddc-29123ad3/29123ad352dccebc03bd04bd1c9d7298.simg"
url: https://datasets.datalad.org/shub/powerPlant/diamond-srf/latest/2019-02-11-b857eddc-29123ad3/
recipe: https://datasets.datalad.org/shub/powerPlant/diamond-srf/latest/2019-02-11-b857eddc-29123ad3/Singularity
collection: powerPlant/diamond-srf
---

# powerPlant/diamond-srf:latest

```bash
$ singularity pull shub://powerPlant/diamond-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version v0.9.24

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install wget
  cd /opt
  wget http://github.com/bbuchfink/diamond/releases/download/v0.9.24/diamond-linux64.tar.gz
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

