---
id: 11686
name: "powerPlant/open-mpi-srf"
branch: "master"
tag: "latest"
commit: "2fb7561abd1037d313fa8c9ab50412caadcb9f6a"
version: "32c04ef83b48c8cfde2b810b31bd22232db6c536b9a7bb7b8331509b70989335"
build_date: "2019-11-22T23:29:23.949Z"
size_mb: 50.5
size: 52953088
sif: "https://datasets.datalad.org/shub/powerPlant/open-mpi-srf/latest/2019-11-22-2fb7561a-32c04ef8/32c04ef83b48c8cfde2b810b31bd22232db6c536b9a7bb7b8331509b70989335.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/open-mpi-srf/latest/2019-11-22-2fb7561a-32c04ef8/
recipe: https://datasets.datalad.org/shub/powerPlant/open-mpi-srf/latest/2019-11-22-2fb7561a-32c04ef8/Singularity
collection: powerPlant/open-mpi-srf
---

# powerPlant/open-mpi-srf:latest

```bash
$ singularity pull shub://powerPlant/open-mpi-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%help
This container provides Open MPI and is meant to be used as a build base for other containers that require it

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 4.0.2

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
  export OMPI_VERSION=4.0.2
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

