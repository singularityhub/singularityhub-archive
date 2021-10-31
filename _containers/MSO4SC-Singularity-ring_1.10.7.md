---
id: 2798
name: "MSO4SC/Singularity"
branch: "master"
tag: "ring_1.10.7"
commit: "abb6dda6b4bd3c3cf400e51224be4548d18a46fe"
version: "e671695857ce9a9f0333eeebe2844fd3"
build_date: "2019-11-20T17:45:28.956Z"
size_mb: 261
size: 99262495
sif: "https://datasets.datalad.org/shub/MSO4SC/Singularity/ring_1.10.7/2019-11-20-abb6dda6-e6716958/e671695857ce9a9f0333eeebe2844fd3.simg"
url: https://datasets.datalad.org/shub/MSO4SC/Singularity/ring_1.10.7/2019-11-20-abb6dda6-e6716958/
recipe: https://datasets.datalad.org/shub/MSO4SC/Singularity/ring_1.10.7/2019-11-20-abb6dda6-e6716958/Singularity
collection: MSO4SC/Singularity
---

# MSO4SC/Singularity:ring_1.10.7

```bash
$ singularity pull shub://MSO4SC/Singularity:ring_1.10.7
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial

%setup

%help
    OpenMPI 1.10.7 Ring test application in Ubuntu Xenial OS

%labels
    App ring
    MPI_Family OpenMPI
    MPI_Version v1.10.7
    OS Ubuntu
    OS_Version Xenial
    Maintainer Víctor Sande

%files

%environment

%post
    #------------------
    # REQUERIMENTS
    #------------------

    REQUERIMENTS="wget \
                  gcc \
                  openmpi-bin \
                  openmpi-common \
                  libopenmpi-dev \
                  dapl2-utils \
                  libdapl-dev \
                  libdapl2 \
                  libibverbs1 \
                  librdmacm1 \
                  libcxgb3-1 \
                  libipathverbs1 \
                  libmlx4-1 \
                  libmlx5-1 \
                  libmthca1 \
                  libnes1 \
                  libpmi0 \
                  libpmi0-dev"


    echo "Installing $REQUERIMENTS ..."
    apt-get update
    apt -y --allow-unauthenticated install $REQUERIMENTS

    mkdir -p /mnt
    mkdir -p /scratch

    #------------------
    # USER INSTALL
    #------------------

    cd /tmp
    wget https://raw.githubusercontent.com/open-mpi/ompi/master/examples/ring_c.c -O ring_c.c
    mpicc ring_c.c -o /usr/bin/ring

    #------------------
    # CLEAN APT files
    #------------------
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    rm -rf /var/tmp/*

%runscript
    exec echo "Running ring"
    exec ring

%test
    exec echo "Testing ring"
    exec ring

##############################
# Ring App
##############################

%apphelp ring
    OpenMPI 1.10.7 Ring test application in Ubuntu Xenial OS

%applabels ring
    App ring
    MPI_Family OpenMPI
    MPI_Version v1.10.7

%appenv ring

%appfiles foo

%appinstall ring

%apprun ring
    exec echo "Running ring app"
    exec ring
```

## Collection

 - Name: [MSO4SC/Singularity](https://github.com/MSO4SC/Singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

