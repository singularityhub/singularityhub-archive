---
id: 7081
name: "powerPlant/diamond-srf"
branch: "master"
tag: "v0.9.17"
commit: "b857eddc55a38b76b994c02365e7f2eac3ebfb91"
version: "94cf3ad63949e019cc916fc9c3989d73"
build_date: "2019-02-11T09:20:46.072Z"
size_mb: 109
size: 50520095
sif: "https://datasets.datalad.org/shub/powerPlant/diamond-srf/v0.9.17/2019-02-11-b857eddc-94cf3ad6/94cf3ad63949e019cc916fc9c3989d73.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/diamond-srf/v0.9.17/2019-02-11-b857eddc-94cf3ad6/
recipe: https://datasets.datalad.org/shub/powerPlant/diamond-srf/v0.9.17/2019-02-11-b857eddc-94cf3ad6/Singularity
collection: powerPlant/diamond-srf
---

# powerPlant/diamond-srf:v0.9.17

```bash
$ singularity pull shub://powerPlant/diamond-srf:v0.9.17
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version v0.9.17

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install wget
  cd /opt
  wget http://github.com/bbuchfink/diamond/releases/download/v0.9.17/diamond-linux64.tar.gz
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

