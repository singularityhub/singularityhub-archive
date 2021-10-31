---
id: 11644
name: "powerPlant/open-mpi-srf"
branch: "master"
tag: "4.0.1"
commit: "2fb7561abd1037d313fa8c9ab50412caadcb9f6a"
version: "1d39499dd58db6a6aaedb747e976eed56bcf635a134c2a6d0214364e8f1bd832"
build_date: "2019-11-22T23:02:49.920Z"
size_mb: 50.53125
size: 52985856
sif: "https://datasets.datalad.org/shub/powerPlant/open-mpi-srf/4.0.1/2019-11-22-2fb7561a-1d39499d/1d39499dd58db6a6aaedb747e976eed56bcf635a134c2a6d0214364e8f1bd832.sif"
url: https://datasets.datalad.org/shub/powerPlant/open-mpi-srf/4.0.1/2019-11-22-2fb7561a-1d39499d/
recipe: https://datasets.datalad.org/shub/powerPlant/open-mpi-srf/4.0.1/2019-11-22-2fb7561a-1d39499d/Singularity
collection: powerPlant/open-mpi-srf
---

# powerPlant/open-mpi-srf:4.0.1

```bash
$ singularity pull shub://powerPlant/open-mpi-srf:4.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%help
This container provides Open MPI and is meant to be used as a build base for other containers that require it

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 4.0.1

%environment
  export OMPI_DIR=/usr/local
  export SINGULARITY_OMPI_DIR=$OMPI_DIR
  export SINGULARITYENV_APPEND_PATH=$OMPI_DIR/bin
  export SINGULAIRTYENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%post
  ## Download prerequisites
  apt-get update
  apt-get -y install g++ make wget
  
  ## OpenMPI
  cd /opt
  export OMPI_VERSION=4.0.1
  export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-$OMPI_VERSION.tar.bz2"

  wget -O openmpi-$OMPI_VERSION.tar.bz2 $OMPI_URL
  tar -xjf openmpi-$OMPI_VERSION.tar.bz2
  cd openmpi-$OMPI_VERSION
  ./configure
  make -j`nproc` install
  ldconfig

  ## Cleanup
  apt-get -y remove g++ make wget
  apt-get -y autoremove
  rm -rf /opt/*
```

## Collection

 - Name: [powerPlant/open-mpi-srf](https://github.com/powerPlant/open-mpi-srf)
 - License: None

