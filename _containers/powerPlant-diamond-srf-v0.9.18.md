---
id: 7082
name: "powerPlant/diamond-srf"
branch: "master"
tag: "v0.9.18"
commit: "b857eddc55a38b76b994c02365e7f2eac3ebfb91"
version: "9b6016a1f067dcad8141f5b1374986fe"
build_date: "2019-02-11T09:20:46.067Z"
size_mb: 109
size: 50524191
sif: "https://datasets.datalad.org/shub/powerPlant/diamond-srf/v0.9.18/2019-02-11-b857eddc-9b6016a1/9b6016a1f067dcad8141f5b1374986fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/diamond-srf/v0.9.18/2019-02-11-b857eddc-9b6016a1/
recipe: https://datasets.datalad.org/shub/powerPlant/diamond-srf/v0.9.18/2019-02-11-b857eddc-9b6016a1/Singularity
collection: powerPlant/diamond-srf
---

# powerPlant/diamond-srf:v0.9.18

```bash
$ singularity pull shub://powerPlant/diamond-srf:v0.9.18
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version v0.9.18

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install wget
  cd /opt
  wget http://github.com/bbuchfink/diamond/releases/download/v0.9.18/diamond-linux64.tar.gz
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

