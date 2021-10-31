---
id: 7173
name: "powerPlant/ragoo-srf"
branch: "master"
tag: "1.01"
commit: "0b8f2b4f6cbe5ada832ae6fe8bbca04c3a03e83e"
version: "55822a487d48a4aa2b005dd9a505d9aa"
build_date: "2019-02-21T20:57:18.319Z"
size_mb: 216
size: 79204383
sif: "https://datasets.datalad.org/shub/powerPlant/ragoo-srf/1.01/2019-02-21-0b8f2b4f-55822a48/55822a487d48a4aa2b005dd9a505d9aa.simg"
url: https://datasets.datalad.org/shub/powerPlant/ragoo-srf/1.01/2019-02-21-0b8f2b4f-55822a48/
recipe: https://datasets.datalad.org/shub/powerPlant/ragoo-srf/1.01/2019-02-21-0b8f2b4f-55822a48/Singularity
collection: powerPlant/ragoo-srf
---

# powerPlant/ragoo-srf:1.01

```bash
$ singularity pull shub://powerPlant/ragoo-srf:1.01
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.01

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
  
  wget https://github.com/malonge/RaGOO/archive/v1.01.tar.gz
  tar -xvf v1.01.tar.gz
  cd RaGOO-1.01/
  python3 setup.py install
  chmod +x ragoo.py

  ## Cleanup
  rm -rf /opt/v1.01.tar.gz /opt/minimap2-2.15_x64-linux.tar.bz2
  apt-get remove wget python3-pip -y
  apt-get autoremove -y
  apt-get -y clean all

%runscript
  exec python3 /opt/RaGOO-1.01/ragoo.py "$@"
```

## Collection

 - Name: [powerPlant/ragoo-srf](https://github.com/powerPlant/ragoo-srf)
 - License: None

