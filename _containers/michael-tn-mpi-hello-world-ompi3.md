---
id: 602
name: "michael-tn/mpi-hello-world"
branch: "master"
tag: "ompi3"
commit: "1d32048a085a1f3b1b9a82cc2d3db5b69ac43cc2"
version: "fcda3bf4b5ae1cc58ce213545fdf4e5a"
build_date: "2017-10-30T00:04:56.565Z"
size_mb: 716
size: 203894815
sif: "https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi3/2017-10-30-1d32048a-fcda3bf4/fcda3bf4b5ae1cc58ce213545fdf4e5a.simg"
url: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi3/2017-10-30-1d32048a-fcda3bf4/
recipe: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi3/2017-10-30-1d32048a-fcda3bf4/Singularity
collection: michael-tn/mpi-hello-world
---

# michael-tn/mpi-hello-world:ompi3

```bash
$ singularity pull shub://michael-tn/mpi-hello-world:ompi3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    apt-get -y update
    apt-get -y install make build-essential zlib1g-dev libncurses5-dev wget git
    echo "Get and Build openmpi"
    cd /usr/local/src 
    wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.bz2 
    tar -xjf openmpi-3.0.0.tar.bz2
    cd openmpi-3.0.0  
    ./configure --prefix=/usr/local --with-hwloc
    make -j4 
    make install
    ldconfig
    echo "Get and Build mpi_hello_world"
    mkdir /usr/local/src/git 
    cd /usr/local/src/git  
    git clone https://github.com/wesleykendall/mpitutorial 
    cd mpitutorial/tutorials/mpi-hello-world/code 
    make 
    cp mpi_hello_world /usr/local/bin
```

## Collection

 - Name: [michael-tn/mpi-hello-world](https://github.com/michael-tn/mpi-hello-world)
 - License: None

