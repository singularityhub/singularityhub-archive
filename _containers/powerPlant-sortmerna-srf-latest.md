---
id: 15910
name: "powerPlant/sortmerna-srf"
branch: "master"
tag: "latest"
commit: "ecd4c3dbbf67116694f5036cb35f891cc80038e2"
version: "fa2732802bc387604be7d093ee41f23fe4684f0887132c02908dffbed3f9172c"
build_date: "2021-04-16T03:05:38.662Z"
size_mb: 55.55859375
size: 58257408
sif: "https://datasets.datalad.org/shub/powerPlant/sortmerna-srf/latest/2021-04-16-ecd4c3db-fa273280/fa2732802bc387604be7d093ee41f23fe4684f0887132c02908dffbed3f9172c.sif"
url: https://datasets.datalad.org/shub/powerPlant/sortmerna-srf/latest/2021-04-16-ecd4c3db-fa273280/
recipe: https://datasets.datalad.org/shub/powerPlant/sortmerna-srf/latest/2021-04-16-ecd4c3db-fa273280/Singularity
collection: powerPlant/sortmerna-srf
---

# powerPlant/sortmerna-srf:latest

```bash
$ singularity pull shub://powerPlant/sortmerna-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 4.3.2

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install wget

  cd /opt
  wget https://github.com/biocore/sortmerna/releases/download/v4.3.2/sortmerna-4.3.2-Linux.sh
  mkdir sortmerna-4.3.2-Linux
  bash sortmerna-4.3.2-Linux.sh --skip-license --prefix=sortmerna-4.3.2-Linux

## Cleanup
  rm -rf /opt/sortmerna-4.3.2-Linux.sh
  apt-get -y remove wget
  apt-get -y autoremove
  apt-get -y clean all

%runscript
  exec /opt/sortmerna-4.3.2-Linux/bin/sortmerna "$@"
```

## Collection

 - Name: [powerPlant/sortmerna-srf](https://github.com/powerPlant/sortmerna-srf)
 - License: None

