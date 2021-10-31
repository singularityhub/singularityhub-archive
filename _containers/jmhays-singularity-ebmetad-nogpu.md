---
id: 5830
name: "jmhays/singularity-ebmetad"
branch: "master"
tag: "nogpu"
commit: "8d36faaafa13a7bf7ef8d674e64f9d2dbd722a25"
version: "da66c07fc2f36eda8bdedf38668335f7"
build_date: "2018-12-17T16:03:52.158Z"
size_mb: 2643
size: 1445515295
sif: "https://datasets.datalad.org/shub/jmhays/singularity-ebmetad/nogpu/2018-12-17-8d36faaa-da66c07f/da66c07fc2f36eda8bdedf38668335f7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jmhays/singularity-ebmetad/nogpu/2018-12-17-8d36faaa-da66c07f/
recipe: https://datasets.datalad.org/shub/jmhays/singularity-ebmetad/nogpu/2018-12-17-8d36faaa-da66c07f/Singularity
collection: jmhays/singularity-ebmetad
---

# jmhays/singularity-ebmetad:nogpu

```bash
$ singularity pull shub://jmhays/singularity-ebmetad:nogpu
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
    cmake ../ -DGMX_MPI=OFF -DGMX_GPU=OFF -DGMX_OPENMP=ON -DGMX_USE_NVML=OFF
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

    # EBMetaD plugin
    git clone https://github.com/jmhays/sample_restraint.git
    cd sample_restraint
    git checkout ebmetad
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

