---
id: 7825
name: "Chabrier/sSighma"
branch: "master"
tag: "latest"
commit: "da7792c3e960a7c4a1f992b29267bceaf5bfcda3"
version: "3d6652ef76303bb1cc5a2e17c04f02f8"
build_date: "2019-03-18T18:12:34.601Z"
size_mb: 1385
size: 1090166815
sif: "https://datasets.datalad.org/shub/Chabrier/sSighma/latest/2019-03-18-da7792c3-3d6652ef/3d6652ef76303bb1cc5a2e17c04f02f8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Chabrier/sSighma/latest/2019-03-18-da7792c3-3d6652ef/
recipe: https://datasets.datalad.org/shub/Chabrier/sSighma/latest/2019-03-18-da7792c3-3d6652ef/Singularity
collection: Chabrier/sSighma
---

# Chabrier/sSighma:latest

```bash
$ singularity pull shub://Chabrier/sSighma:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%environment
  LC_ALL=fr_FR.UTF-8
  export LC_ALL
%setup
  wget --no-check-certificate https://tentacule.be/fossil/py-sighma/zip/py-sighma.zip?uuid=trunk
  mv py-sighma.zip\?uuid\=trunk  ${SINGULARITY_ROOTFS}/py-sighma.zip

%post
  apt-get update && apt-get -y install wget build-essential
  apt-get install -y locales
  locale-gen fr_FR.UTF-8
  update-locale LANG=fr_FR.UTF-8
  apt-get install -y python3-dev libpython3-dev python3-mysqldb python3-pip
  pip3 install cython
  apt-get -y install zip
  apt-get -y install unzip
  unzip py-sighma.zip
  cd py-sighma/src
  python3 setup.py

%runscript
  export LC_ALL=fr_FR.UTF-8
  cat "$*"
  echo /usr/bin/python3 /py-sighma/src/main.py file "$*"
  /usr/bin/python3 /py-sighma/src/main.py file "$*"
```

## Collection

 - Name: [Chabrier/sSighma](https://github.com/Chabrier/sSighma)
 - License: None

