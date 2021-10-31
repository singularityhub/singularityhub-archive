---
id: 7406
name: "gearslaboratory/gears-singularity"
branch: "master"
tag: "gears-taudem"
commit: "69071dc1d70a87bb7151ff1ce24b1e7d476d14f5"
version: "c09d97d3e9c5412ec8c56d578c500ce0"
build_date: "2019-02-24T08:38:35.001Z"
size_mb: 2782
size: 1708470303
sif: "https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-taudem/2019-02-24-69071dc1-c09d97d3/c09d97d3e9c5412ec8c56d578c500ce0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gearslaboratory/gears-singularity/gears-taudem/2019-02-24-69071dc1-c09d97d3/
recipe: https://datasets.datalad.org/shub/gearslaboratory/gears-singularity/gears-taudem/2019-02-24-69071dc1-c09d97d3/Singularity
collection: gearslaboratory/gears-singularity
---

# gearslaboratory/gears-singularity:gears-taudem

```bash
$ singularity pull shub://gearslaboratory/gears-singularity:gears-taudem
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

# TauDEM ## 
# https://github.com/dtarb/TauDEM #

%environment
    PATH=$PATH:/usr/local/taudem/
    export PATH

%post
  apt-get clean && apt-get -y update && apt-get install -y locales && locale-gen en_US.UTF-8
	
  # Add to sources list:
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  apt-get -y update

  # Latest R
  apt-get install -y software-properties-common
  # add-apt-repository ppa:edd/r-3.5
  # apt-get update

  # Install misc. utilities:
  apt-get install -y libopenblas-dev r-base-core r-base-dev libcurl4-openssl-dev \
  	libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server \
  	libssh-dev wget vim git nano git cmake gfortran g++ curl wget python autoconf \
  	bzip2 libtool libtool-bin libxml2-dev unzip
  
  # taudem dependencies
  apt-get install -y libgdal-dev libproj-dev python-gdal python3-gdal unzip libibverbs-dev mpich 
  git clone -b Develop https://github.com/dtarb/TauDEM.git
  cd TauDEM
  cd src && mkdir build && cd build
  cmake ..
  make && make install
```

## Collection

 - Name: [gearslaboratory/gears-singularity](https://github.com/gearslaboratory/gears-singularity)
 - License: None

