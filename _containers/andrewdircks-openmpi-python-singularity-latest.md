---
id: 15392
name: "andrewdircks/openmpi-python-singularity"
branch: "main"
tag: "latest"
commit: "d9642271d32d245436b543f5d10916897dd8b35f"
version: "b93a78c7cede0f155405bce96cce16bd"
build_date: "2021-01-26T17:33:24.282Z"
size_mb: 812.0
size: 175624223
sif: "https://datasets.datalad.org/shub/andrewdircks/openmpi-python-singularity/latest/2021-01-26-d9642271-b93a78c7/b93a78c7cede0f155405bce96cce16bd.sif"
url: https://datasets.datalad.org/shub/andrewdircks/openmpi-python-singularity/latest/2021-01-26-d9642271-b93a78c7/
recipe: https://datasets.datalad.org/shub/andrewdircks/openmpi-python-singularity/latest/2021-01-26-d9642271-b93a78c7/Singularity
collection: andrewdircks/openmpi-python-singularity
---

# andrewdircks/openmpi-python-singularity:latest

```bash
$ singularity pull shub://andrewdircks/openmpi-python-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
    export OMPI_DIR=/opt/ompi
    export SINGULARITY_OMPI_DIR=$OMPI_DIR
    export SINGULARITYENV_APPEND_PATH=$OMPI_DIR/bin
    export SINGULAIRTYENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%post
    apt-get update && apt-get install -y wget git bash gcc gfortran g++ make file

    # install MPI version 3.1.4
    export OMPI_DIR=/opt/ompi
    export OMPI_VERSION=3.1.4
    export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.4.tar.bz2"
    mkdir -p /tmp/ompi
    mkdir -p /opt
    cd /tmp/ompi && wget -O openmpi-$OMPI_VERSION.tar.bz2 $OMPI_URL && tar -xjf openmpi-$OMPI_VERSION.tar.bz2
    cd /tmp/ompi/openmpi-$OMPI_VERSION && ./configure --prefix=$OMPI_DIR && make install
    export PATH=$OMPI_DIR/bin:$PATH
    export LD_LIBRARY_PATH=$OMPI_DIR/lib:$LD_LIBRARY_PATH
    export MANPATH=$OMPI_DIR/share/man:$MANPATH

    # install python
    apt-get install -y python3 python3-pip
```

## Collection

 - Name: [andrewdircks/openmpi-python-singularity](https://github.com/andrewdircks/openmpi-python-singularity)
 - License: None

