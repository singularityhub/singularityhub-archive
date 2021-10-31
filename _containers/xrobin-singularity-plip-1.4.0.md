---
id: 2016
name: "xrobin/singularity-plip"
branch: "master"
tag: "1.4.0"
commit: "f8fa64b8281c1ca7c22d6a981ba66de78cd3c00f"
version: "4de6e5732cc2d4f4c1619c3ee8d012f3"
build_date: "2018-03-10T00:08:48.442Z"
size_mb: 594
size: 213725215
sif: "https://datasets.datalad.org/shub/xrobin/singularity-plip/1.4.0/2018-03-10-f8fa64b8-4de6e573/4de6e5732cc2d4f4c1619c3ee8d012f3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xrobin/singularity-plip/1.4.0/2018-03-10-f8fa64b8-4de6e573/
recipe: https://datasets.datalad.org/shub/xrobin/singularity-plip/1.4.0/2018-03-10-f8fa64b8-4de6e573/Singularity
collection: xrobin/singularity-plip
---

# xrobin/singularity-plip:1.4.0

```bash
$ singularity pull shub://xrobin/singularity-plip:1.4.0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    # install some system deps
    apt-get -y update
    apt-get -y install locales
    locale-gen en_US.UTF-8

    # Generic build dependencies
    apt-get -y install git mdm cmake build-essential wget
    # PLIP dependencies
    apt-get -y install python-future python-numpy python-lxml pymol
    # OpenBabel dependencies:
    apt-get -y install libxml2
    apt-get -y install libpython$(python -c 'import sys; print("%s.%s" % (sys.version_info.major, sys.version_info.minor))')
    # OpenBabel build dependencies
    apt-get -y install libxml2-dev libeigen3-dev zlib1g-dev python-dev

    # Install PLIP in /opt
    if [ -d /opt/pliptool ]; then rm -rf /opt/pliptool; fi
    git clone https://github.com/ssalentin/plip.git /opt/pliptool
    cd /opt/pliptool
    git checkout tags/v1.4.0
    cd

    # Install OpenBabel
    if [ -d openbabel ]; then rm -rf openbabel; fi
    mkdir openbabel
    cd openbabel
    wget https://sourceforge.net/projects/openbabel/files/openbabel/2.4.1/openbabel-2.4.1.tar.gz
    tar -xf openbabel-2.4.1.tar.gz
    cd openbabel-2.4.1
    mkdir build
    cd build
    cmake .. -DPYTHON_BINDINGS=ON 
    make -j$(ncpus)
    make install

    # Cleanup OpenBabel
    cd ../../..
    rm -rf openbabel

    # Cleanup system build deps
    apt-get -y remove git mdm cmake build-essential wget
    # Cleanup OpenBabel build deps
    apt-get -y remove libxml2-dev libeigen3-dev zlib1g-dev python-dev
    # Cleanup apt 
    apt-get -y autoremove
    apt-get clean

%runscript

   exec /opt/pliptool/plip/plipcmd "$@"

%environment
    export PYTHONPATH=/opt/pliptool/plip
```

## Collection

 - Name: [xrobin/singularity-plip](https://github.com/xrobin/singularity-plip)
 - License: None

