---
id: 12880
name: "OSC/sa_singularity_molgfx"
branch: "master"
tag: "latest"
commit: "93e3b7c2c9c252f92799bba3393639b7f482b6e2"
version: "78f863d7627f6678a7c1e386787355b8"
build_date: "2020-08-11T10:55:27.958Z"
size_mb: 1693.0
size: 541397023
sif: "https://datasets.datalad.org/shub/OSC/sa_singularity_molgfx/latest/2020-08-11-93e3b7c2-78f863d7/78f863d7627f6678a7c1e386787355b8.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/OSC/sa_singularity_molgfx/latest/2020-08-11-93e3b7c2-78f863d7/
recipe: https://datasets.datalad.org/shub/OSC/sa_singularity_molgfx/latest/2020-08-11-93e3b7c2-78f863d7/Singularity
collection: OSC/sa_singularity_molgfx
---

# OSC/sa_singularity_molgfx:latest

```bash
$ singularity pull shub://OSC/sa_singularity_molgfx:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer zyou@osc.edu

%help

    Container with following molecular graphics systems for Ubuntu 18.04
    - OpenChemistry 1.93.0
    - Gabedit 2.4.8
    - Jmol 14.6.4

%environment
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/openchemistry/lib
    export PATH=$PATH:/usr/local/openchemistry/bin

%post
    export LC_ALL=C
    apt update
    apt upgrade -y
    DEBIAN_FRONTEND=noninteractive apt install -y \
        build-essential git cmake qtbase5-dev libxml2-dev python

    # Gabedit & Jmol
    DEBIAN_FRONTEND=noninteractive apt install -y gabedit
    DEBIAN_FRONTEND=noninteractive apt install -y jmol

    # OpenChemistry
    OSC_BUILD=/osc_build
    mkdir -p $OSC_BUILD
    cd $OSC_BUILD
    git clone --recursive git://github.com/OpenChemistry/openchemistry.git
    cd openchemistry
    git checkout 1.93.0
    git submodule update --init
    cd avogadrogenerators
    git checkout master

    cd $OSC_BUILD
    mkdir -p build && cd build
    cmake ../openchemistry
    cmake --build . --config Release
    mv prefix /usr/local/openchemistry 
    test -d $OSC_BUILD && rm -rf $OSC_BUILD

    # Clean up
    apt autoclean
    apt autoremove --purge -y
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [OSC/sa_singularity_molgfx](https://github.com/OSC/sa_singularity_molgfx)
 - License: [MIT License](https://api.github.com/licenses/mit)

