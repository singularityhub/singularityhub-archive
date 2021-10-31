---
id: 10171
name: "jmhays/singularity-brer"
branch: "master"
tag: "brer-cuda-10.0-ubuntu-18.04"
commit: "d27e6fbcc3f306277a84fd882d95284745e86267"
version: "65e5fa98cb2c17ae6ff20d672b9c7ea6"
build_date: "2019-07-02T23:19:18.802Z"
size_mb: 3419
size: 1791115295
sif: "https://datasets.datalad.org/shub/jmhays/singularity-brer/brer-cuda-10.0-ubuntu-18.04/2019-07-02-d27e6fbc-65e5fa98/65e5fa98cb2c17ae6ff20d672b9c7ea6.simg"
url: https://datasets.datalad.org/shub/jmhays/singularity-brer/brer-cuda-10.0-ubuntu-18.04/2019-07-02-d27e6fbc-65e5fa98/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-brer/brer-cuda-10.0-ubuntu-18.04/2019-07-02-d27e6fbc-65e5fa98/Singularity
collection: jmhays/singularity-brer
---

# jmhays/singularity-brer:brer-cuda-10.0-ubuntu-18.04

```bash
$ singularity pull shub://jmhays/singularity-brer:brer-cuda-10.0-ubuntu-18.04
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-devel-ubuntu18.04 


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
    git checkout release-2019 
    mkdir build
    cd build
    cmake ../ -DGMX_MPI=OFF -DGMX_GPU=ON -DGMX_OPENMP=ON -DGMX_USE_NVML=OFF -DGMXAPI=ON
    make -j8; make install
    cd /builds

    # gmxapi
    git clone https://github.com/kassonlab/gmxapi.git
    cd gmxapi
    git checkout release-0_0_7 
    mkdir build; cd build
    cmake ../ -Dgmxapi_DIR=/usr/local/gromacs/share/cmake/gmxapi
    make -j8; make install
    cd /builds

    # Get BRER plugin
    git clone https://github.com/jmhays/sample_restraint.git
    cd sample_restraint
    git checkout corr-struct
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

