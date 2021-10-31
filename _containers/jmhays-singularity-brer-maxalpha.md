---
id: 7122
name: "jmhays/singularity-brer"
branch: "master"
tag: "maxalpha"
commit: "5d65eef2b7214db23f0812d83545499a29253b15"
version: "2f83b6d26609486f510facfcd19452e9"
build_date: "2019-02-12T08:29:39.241Z"
size_mb: 2696
size: 1446711327
sif: "https://datasets.datalad.org/shub/jmhays/singularity-brer/maxalpha/2019-02-12-5d65eef2-2f83b6d2/2f83b6d26609486f510facfcd19452e9.simg"
url: https://datasets.datalad.org/shub/jmhays/singularity-brer/maxalpha/2019-02-12-5d65eef2-2f83b6d2/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-brer/maxalpha/2019-02-12-5d65eef2-2f83b6d2/Singularity
collection: jmhays/singularity-brer
---

# jmhays/singularity-brer:maxalpha

```bash
$ singularity pull shub://jmhays/singularity-brer:maxalpha
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-devel-ubuntu16.04 


%environment

    # use bash as default shell
    SHELL=/bin/bash

    PATH=/usr/local/gromacs/bin:${PATH}    
    PYTHONPATH="/builds/sample_restraint/build/src/pythonmodule:\
/usr/local/lib/python3.5/dist-packages:/builds/gmxapi/build:${PYTHONPATH}"

    export PATH PYTHONPATH


%labels

   AUTHOR jmh5sf@virginia.edu


%post

    apt-get update && apt-get -y install libopenmpi-dev libfftw3-dev cmake make git python3-dev python3-pip locales

    # Install python dependencies
    pip3 install setuptools networkx cmake mpi4py numpy scipy

    mkdir /builds
    cd /builds

    # gromacs-gmxapi
    git clone https://github.com/kassonlab/gromacs-gmxapi.git
    cd gromacs-gmxapi
    git checkout tags/v0.0.6 -b v0.0.6
    mkdir build
    cd build
    cmake ../ -DGMX_MPI=OFF -DGMX_GPU=ON -DGMX_OPENMP=ON -DGMX_USE_NVML=OFF
    make -j8; make install
    cd /builds

    # gmxapi
    git clone https://github.com/kassonlab/gmxapi.git
    cd gmxapi
    git checkout release-0_0_6 
    mkdir build; cd build
    cmake ../ -Dgmxapi_DIR=/usr/local/gromacs/share/cmake/gmxapi
    make -j8; make install
    cd /builds

    # Get BRER plugin
    git clone https://github.com/jmhays/sample_restraint.git
    cd sample_restraint
    git checkout max-alpha
    mkdir build; cd build
    cmake ../ -Dgmxapi_DIR=/usr/local/gromacs/share/cmake/gmxapi -DGROMACS_DIR=/usr/local/gromacs/share/cmake/gromacs
    make -j8; make install
    cd /builds

    # BRER run scripts
    git clone https://github.com/jmhays/run_brer.git
    cd run_brer/
    git checkout devel
    python3 setup.py install
```

## Collection

 - Name: [jmhays/singularity-brer](https://github.com/jmhays/singularity-brer)
 - License: [GNU Lesser General Public License v2.1](https://api.github.com/licenses/lgpl-2.1)

