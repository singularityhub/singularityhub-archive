---
id: 10802
name: "rkalyanapurdue/mpitest"
branch: "master"
tag: "latest"
commit: "5d9ff455d1402f2e99717c22c8830905870c2e8c"
version: "48713617ba9c87d34f538a823c3ce274"
build_date: "2019-09-04T16:56:11.394Z"
size_mb: 701.0
size: 142221343
sif: "https://datasets.datalad.org/shub/rkalyanapurdue/mpitest/latest/2019-09-04-5d9ff455-48713617/48713617ba9c87d34f538a823c3ce274.sif"
url: https://datasets.datalad.org/shub/rkalyanapurdue/mpitest/latest/2019-09-04-5d9ff455-48713617/
recipe: https://datasets.datalad.org/shub/rkalyanapurdue/mpitest/latest/2019-09-04-5d9ff455-48713617/Singularity
collection: rkalyanapurdue/mpitest
---

# rkalyanapurdue/mpitest:latest

```bash
$ singularity pull shub://rkalyanapurdue/mpitest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%files
    mpitest.c /opt

%environment
    export OMPI_DIR=/opt/ompi
    export SINGULARITY_OMPI_DIR=$OMPI_DIR
    export SINGULARITYENV_APPEND_PATH=$OMPI_DIR/bin
    export SINGULAIRTYENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%post
    echo "Installing required packages..."
    apt-get update && apt-get install -y wget git bash gcc gfortran g++ make file

    echo "Installing Open MPI"
    export OMPI_DIR=/opt/ompi
    export OMPI_VERSION=4.0.1
    export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-$OMPI_VERSION.tar.bz2"
    mkdir -p /tmp/ompi
    mkdir -p /opt
    # Download
    cd /tmp/ompi && wget -O openmpi-$OMPI_VERSION.tar.bz2 $OMPI_URL && tar -xjf openmpi-$OMPI_VERSION.tar.bz2
    # Compile and install
    cd /tmp/ompi/openmpi-$OMPI_VERSION && ./configure --prefix=$OMPI_DIR && make install
    # Set env variables so we can compile our application
    export PATH=$OMPI_DIR/bin:$PATH
    export LD_LIBRARY_PATH=$OMPI_DIR/lib:$LD_LIBRARY_PATH
    export MANPATH=$OMPI_DIR/share/man:$MANPATH

    echo "Compiling the MPI application..."
    cd /opt && mpicc -o mpitest mpitest.c
```

## Collection

 - Name: [rkalyanapurdue/mpitest](https://github.com/rkalyanapurdue/mpitest)
 - License: None

