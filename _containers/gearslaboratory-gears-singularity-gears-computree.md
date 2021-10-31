---
id: 7413
name: "gearslaboratory/gears-singularity"
branch: "master"
tag: "gears-computree"
commit: "9ad320fddfd1012377bbf79d82130a6836aa1493"
version: "1a0924826b467de27a6f88ff2676c578"
build_date: "2019-03-10T18:40:20.489Z"
size_mb: 2896
size: 1037856799
sif: "https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-computree/2019-03-10-9ad320fd-1a092482/1a0924826b467de27a6f88ff2676c578.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gearslaboratory/gears-singularity/gears-computree/2019-03-10-9ad320fd-1a092482/
recipe: https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-computree/2019-03-10-9ad320fd-1a092482/Singularity
collection: gearslaboratory/gears-singularity
---

# gearslaboratory/gears-singularity:gears-computree

```bash
$ singularity pull shub://gearslaboratory/gears-singularity:gears-computree
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

##### Computree via WINE #### 
# Singularity container developed by Jonathan Greenberg (jgreenberg@unr.edu)

%post
  apt-get clean
  apt-get -y update
    
  apt-get install -y locales
  locale-gen en_US.UTF-8
	
  apt-get install -y software-properties-common
	
  # Add to sources list:
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  apt-get -y update

  # Install misc. utilities:
  apt-get install -y libopenblas-dev libcurl4-openssl-dev \
  libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server \
  libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf bzip2 \
  libtool libtool-bin libxml2-dev unzip

  # wine:
  mkdir -p /APPS /PROFILES
  chmod 0777 /APPS /PROFILES
  dpkg --add-architecture i386
  wget -nc https://dl.winehq.org/wine-builds/winehq.key
  apt-key add winehq.key
  apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
  apt-get update
  apt-get install -y --install-recommends winehq-stable
  apt-get clean
  
  ## Headless:
  apt-get -y install xvfb  
  
  # computree via windows
  git clone https://github.com/gearslaboratory/gears-singularity.git
  cd gears-singularity/additional_data/computree
  unzip computree_v5.0.184e.zip
  mv computree_v5.0.184e /APPS/
  
  # computree via linux
  git clone https://github.com/gearslaboratory/gears-singularity.git
  cd gears-singularity/additional_data/computree
  tar -xvf computree_release.tar.xz
  mv computree_release /APPS/
  
  # Create computree batch shortcut
  # Lastools shortcuts:  
  echo '#!/bin/bash
WINEDEBUG=-all DISPLAY=:0.0 wine '/APPS/computree_v5.0.184e/CompuTreeBatch.exe '"$@"' >> /usr/local/bin/CompuTreeBatch
	chmod 755 /usr/local/bin/CompuTreeBatch
  
%runscript
	Xvfb :0 -screen 0 1024x768x16 &
	cd /APPS/computree_v5.0.184e
```

## Collection

 - Name: [gearslaboratory/gears-singularity](https://github.com/gearslaboratory/gears-singularity)
 - License: None

