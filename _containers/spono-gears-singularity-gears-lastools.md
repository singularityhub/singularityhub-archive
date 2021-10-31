---
id: 9979
name: "spono/gears-singularity"
branch: "master"
tag: "gears-lastools"
commit: "c60e58e7f2ca1bf21f2614569ca41ac1283544ae"
version: "5985eef75021026428aa99a50b18071a"
build_date: "2019-06-23T23:32:49.228Z"
size_mb: 2016
size: 685105183
sif: "https://datasets.datalad.org/shub/spono/gears-singularity/gears-lastools/2019-06-23-c60e58e7-5985eef7/5985eef75021026428aa99a50b18071a.simg"
url: https://datasets.datalad.org/shub/spono/gears-singularity/gears-lastools/2019-06-23-c60e58e7-5985eef7/
recipe: https://datasets.datalad.org/shub/spono/gears-singularity/gears-lastools/2019-06-23-c60e58e7-5985eef7/Singularity
collection: spono/gears-singularity
---

# spono/gears-singularity:gears-lastools

```bash
$ singularity pull shub://spono/gears-singularity:gears-lastools
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

#### LASTools via WINE #### 
# Singularity container developed by Jonathan Greenberg (jgreenberg@unr.edu)

%environment
    PATH=$PATH:/APPS/LAStools/bin/
    export PATH

%post
  locale-gen en_US.UTF-8
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
  gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
  gpg -a --export E084DAB9 | apt-key add -
  apt-get update

  # Install misc. utilities:
  apt-get install -y libopenblas-dev libcurl4-openssl-dev \
  libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server \
  libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf bzip2 \
  libtool libtool-bin libxml2-dev 

  # wine:
  mkdir -p /APPS /PROFILES
  chmod 0777 /APPS /PROFILES
  dpkg --add-architecture i386
  apt-get update && apt-get -y install wget less vim software-properties-common python3-software-properties apt-transport-https winbind
  wget -nc https://dl.winehq.org/wine-builds/winehq.key
  apt-key add winehq.key
  apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/
  apt-get update && apt-get install -y winehq-stable winetricks # this installs Wine2
  apt-get clean
  
  # lastools
  cd ~
  wget https://lastools.github.io/download/LAStools.zip
  unzip LAStools.zip
  mv LAStools /APPS/
  
# Lastools shortcuts:  
for filename in /APPS/LAStools/bin/*.exe; do
basename=`basename $filename .exe`
  echo '#!/bin/bash
WINEDEBUG=-all wine '$filename '"$@"' >> /usr/local/bin/$basename
chmod 755 /usr/local/bin/$basename
done
```

## Collection

 - Name: [spono/gears-singularity](https://github.com/spono/gears-singularity)
 - License: None

