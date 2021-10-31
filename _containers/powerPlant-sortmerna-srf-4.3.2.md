---
id: 15911
name: "powerPlant/sortmerna-srf"
branch: "master"
tag: "4.3.2"
commit: "ecd4c3dbbf67116694f5036cb35f891cc80038e2"
version: "9015cd0249e61b94567b2caadca48920874b9915d2959bbee54821133429fa1e"
build_date: "2021-04-16T03:08:04.099Z"
size_mb: 55.55859375
size: 58257408
sif: "https://datasets.datalad.org/shub/powerPlant/sortmerna-srf/4.3.2/2021-04-16-ecd4c3db-9015cd02/9015cd0249e61b94567b2caadca48920874b9915d2959bbee54821133429fa1e.sif"
url: https://datasets.datalad.org/shub/powerPlant/sortmerna-srf/4.3.2/2021-04-16-ecd4c3db-9015cd02/
recipe: https://datasets.datalad.org/shub/powerPlant/sortmerna-srf/4.3.2/2021-04-16-ecd4c3db-9015cd02/Singularity
collection: powerPlant/sortmerna-srf
---

# powerPlant/sortmerna-srf:4.3.2

```bash
$ singularity pull shub://powerPlant/sortmerna-srf:4.3.2
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

