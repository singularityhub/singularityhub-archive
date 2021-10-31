---
id: 2993
name: "xrobin/singularity-plip"
branch: "master"
tag: "1.4.2"
commit: "50dec0fa978a28a08e2d04c816dffd5b52bc4f54"
version: "b985a3ac2248d5d5eca621cff6f99db2"
build_date: "2018-05-30T12:30:55.403Z"
size_mb: 594
size: 213999647
sif: "https://datasets.datalad.org/shub/xrobin/singularity-plip/1.4.2/2018-05-30-50dec0fa-b985a3ac/b985a3ac2248d5d5eca621cff6f99db2.simg"
url: https://datasets.datalad.org/shub/xrobin/singularity-plip/1.4.2/2018-05-30-50dec0fa-b985a3ac/
recipe: https://datasets.datalad.org/shub/xrobin/singularity-plip/1.4.2/2018-05-30-50dec0fa-b985a3ac/Singularity
collection: xrobin/singularity-plip
---

# xrobin/singularity-plip:1.4.2

```bash
$ singularity pull shub://xrobin/singularity-plip:1.4.2
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
    git checkout tags/v1.4.2
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
    export PYTHONPATH=/opt/pliptool
```

## Collection

 - Name: [xrobin/singularity-plip](https://github.com/xrobin/singularity-plip)
 - License: None

