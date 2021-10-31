---
id: 6160
name: "jmhays/singularity-ebmetad"
branch: "master"
tag: "latest"
commit: "b45cb7a27ad7d4053c707f84b3ee6c0266ec28d0"
version: "b59bbd427a8d5123bef0a0ff037f5311"
build_date: "2019-01-18T22:38:49.366Z"
size_mb: 2704
size: 1458905119
sif: "https://datasets.datalad.org/shub/jmhays/singularity-ebmetad/latest/2019-01-18-b45cb7a2-b59bbd42/b59bbd427a8d5123bef0a0ff037f5311.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jmhays/singularity-ebmetad/latest/2019-01-18-b45cb7a2-b59bbd42/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-ebmetad/latest/2019-01-18-b45cb7a2-b59bbd42/Singularity
collection: jmhays/singularity-ebmetad
---

# jmhays/singularity-ebmetad:latest

```bash
$ singularity pull shub://jmhays/singularity-ebmetad:latest
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

    # EBMetaD plugin
    git clone https://github.com/jmhays/sample_restraint.git
    cd sample_restraint
    git checkout deer
    mkdir build; cd build
    cmake ../ -Dgmxapi_DIR=/usr/local/gromacs/share/cmake/gmxapi -DGROMACS_DIR=/usr/local/gromacs/share/cmake/gromacs
    make -j8
    cd /builds

    # EBMetaD run scripts
    git clone https://github.com/jmhays/run_ebmetad.git
    cd run_ebmetad/
    git checkout devel
    python3 setup.py install
```

## Collection

 - Name: [jmhays/singularity-ebmetad](https://github.com/jmhays/singularity-ebmetad)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

