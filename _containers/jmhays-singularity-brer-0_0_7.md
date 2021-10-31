---
id: 9772
name: "jmhays/singularity-brer"
branch: "master"
tag: "0_0_7"
commit: "7506febfee03135192d124dd9c1c77dee0cbbf15"
version: "e8c5503accd47564a8f8cd9d6ec4e01b"
build_date: "2019-06-13T14:46:41.006Z"
size_mb: 2707
size: 1449046047
sif: "https://datasets.datalad.org/shub/jmhays/singularity-brer/0_0_7/2019-06-13-7506febf-e8c5503a/e8c5503accd47564a8f8cd9d6ec4e01b.simg"
url: https://datasets.datalad.org/shub/jmhays/singularity-brer/0_0_7/2019-06-13-7506febf-e8c5503a/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-brer/0_0_7/2019-06-13-7506febf-e8c5503a/Singularity
collection: jmhays/singularity-brer
---

# jmhays/singularity-brer:0_0_7

```bash
$ singularity pull shub://jmhays/singularity-brer:0_0_7
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

