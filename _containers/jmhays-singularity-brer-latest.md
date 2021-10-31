---
id: 5148
name: "jmhays/singularity-brer"
branch: "devel"
tag: "latest"
commit: "87b01a51be400ca6fdee85dfb48821e4ed07129c"
version: "0797ea6555bc976a64127029dd9176ca"
build_date: "2018-10-25T20:56:45.017Z"
size_mb: 2722
size: 1449627679
sif: "https://datasets.datalad.org/shub/jmhays/singularity-brer/latest/2018-10-25-87b01a51-0797ea65/0797ea6555bc976a64127029dd9176ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jmhays/singularity-brer/latest/2018-10-25-87b01a51-0797ea65/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-brer/latest/2018-10-25-87b01a51-0797ea65/Singularity
collection: jmhays/singularity-brer
---

# jmhays/singularity-brer:latest

```bash
$ singularity pull shub://jmhays/singularity-brer:latest
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
    git checkout tags/v0.0.6 -b v0.0.6
    mkdir build; cd build
    cmake ../ -Dgmxapi_DIR=/usr/local/gromacs/share/cmake/gmxapi
    make -j8; make install
    cd /builds

    # Get BRER plugin
    git clone https://github.com/jmhays/sample_restraint.git
    cd sample_restraint
    git checkout deer
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

