---
id: 7172
name: "powerPlant/ragoo-srf"
branch: "master"
tag: "latest"
commit: "0b8f2b4f6cbe5ada832ae6fe8bbca04c3a03e83e"
version: "47fcba155d1a65487f8849f5b7c08d4a"
build_date: "2019-02-21T20:57:18.326Z"
size_mb: 216
size: 79208479
sif: "https://datasets.datalad.org/shub/powerPlant/ragoo-srf/latest/2019-02-21-0b8f2b4f-47fcba15/47fcba155d1a65487f8849f5b7c08d4a.simg"
url: https://datasets.datalad.org/shub/powerPlant/ragoo-srf/latest/2019-02-21-0b8f2b4f-47fcba15/
recipe: https://datasets.datalad.org/shub/powerPlant/ragoo-srf/latest/2019-02-21-0b8f2b4f-47fcba15/Singularity
collection: powerPlant/ragoo-srf
---

# powerPlant/ragoo-srf:latest

```bash
$ singularity pull shub://powerPlant/ragoo-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.02

%environment
PATH=/opt/minimap2-2.15_x64-linux:$PATH
export PATH

%post
  ## Download build prerequisites
  apt-get -y update
  apt-get -y install python3 wget python3-pip python3-setuptools

  cd /opt
  wget https://github.com/lh3/minimap2/releases/download/v2.15/minimap2-2.15_x64-linux.tar.bz2
  tar -xvf minimap2-2.15_x64-linux.tar.bz2
  
  wget https://github.com/malonge/RaGOO/archive/v1.02.tar.gz
  tar -xvf v1.02.tar.gz
  cd RaGOO-1.02/
  python3 setup.py install
  chmod +x ragoo.py

  ## Cleanup
  rm -rf /opt/v1.02.tar.gz /opt/minimap2-2.15_x64-linux.tar.bz2
  apt-get remove wget python3-pip -y
  apt-get autoremove -y
  apt-get -y clean all

%runscript
  exec python3 /opt/RaGOO-1.02/ragoo.py "$@"
```

## Collection

 - Name: [powerPlant/ragoo-srf](https://github.com/powerPlant/ragoo-srf)
 - License: None

