---
id: 5374
name: "jmhays/singularity-restrained-ensemble"
branch: "devel"
tag: "latest"
commit: "3366290fe5f8cddb2a916a774fc820f60a30e8f8"
version: "32b90af2c13dfd993d498c655b408a47"
build_date: "2019-09-19T05:32:15.897Z"
size_mb: 2701
size: 1437704223
sif: "https://datasets.datalad.org/shub/jmhays/singularity-restrained-ensemble/latest/2019-09-19-3366290f-32b90af2/32b90af2c13dfd993d498c655b408a47.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jmhays/singularity-restrained-ensemble/latest/2019-09-19-3366290f-32b90af2/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-restrained-ensemble/latest/2019-09-19-3366290f-32b90af2/Singularity
collection: jmhays/singularity-restrained-ensemble
---

# jmhays/singularity-restrained-ensemble:latest

```bash
$ singularity pull shub://jmhays/singularity-restrained-ensemble:latest
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
    cmake ../ -DGMX_MPI=OFF -DGMX_GPU=ON -DGMX_OPENMP=ON -DGMX_USE_NVML=OFF -DGMX_CPU_ACCELERATION="AVX_128_FMA"
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

    # restrained-ensemble plugin
    git clone https://github.com/kassonlab/sample_restraint.git
    cd sample_restraint
    git checkout tags/v0.0.6 -b v0.0.6
    mkdir build; cd build
    cmake ../ -Dgmxapi_DIR=/usr/local/gromacs/share/cmake/gmxapi -DGROMACS_DIR=/usr/local/gromacs/share/cmake/gromacs
    make -j8
    cd /builds
```

## Collection

 - Name: [jmhays/singularity-restrained-ensemble](https://github.com/jmhays/singularity-restrained-ensemble)
 - License: [GNU Lesser General Public License v2.1](https://api.github.com/licenses/lgpl-2.1)

