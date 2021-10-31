---
id: 3770
name: "pescobar/singularity-pymol"
branch: "master"
tag: "latest"
commit: "7237b844f1796eafa8d3f03a5d7b5b6a12c93f35"
version: "d3307a92d1c0dcd0c9cedb9d924c78f5"
build_date: "2020-12-21T05:14:18.015Z"
size_mb: 911
size: 321073183
sif: "https://datasets.datalad.org/shub/pescobar/singularity-pymol/latest/2020-12-21-7237b844-d3307a92/d3307a92d1c0dcd0c9cedb9d924c78f5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/singularity-pymol/latest/2020-12-21-7237b844-d3307a92/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-pymol/latest/2020-12-21-7237b844-d3307a92/Singularity
collection: pescobar/singularity-pymol
---

# pescobar/singularity-pymol:latest

```bash
$ singularity pull shub://pescobar/singularity-pymol:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%runscript
   pymol "$@"

%post
    
    export PYMON_VERSION="2.2.0"

    # install build dependencies for PyMOL
    apt-get update
    apt-get -y install build-essential python-dev python-pmw libglew-dev \
      freeglut3-dev libpng-dev libfreetype6-dev libxml2-dev \
        libmsgpack-dev python-pyqt5.qtopengl libglm-dev curl
    apt-get clean

    # download pymol code
    cd /usr/local/src
    curl -sSL -O https://github.com/schrodinger/pymol-open-source/archive/v2.2.0.tar.gz
    tar xf v${PYMON_VERSION}.tar.gz
    cd pymol-open-source-${PYMON_VERSION}
    python setup.py build install


%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""

%apphelp PyMOL
    "PyMOL version 2.2.0"

%apprun PyMOL
    pymol
```

## Collection

 - Name: [pescobar/singularity-pymol](https://github.com/pescobar/singularity-pymol)
 - License: None

