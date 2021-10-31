---
id: 459
name: "michael-tn/mpi-hello-world"
branch: "master"
tag: "ompi2"
commit: "5509fd88a753dcd625499be29435ffe9c35998bb"
version: "12a5387d0cb34b263846d55c76076a16"
build_date: "2019-08-13T07:11:05.146Z"
size_mb: 686
size: 197201951
sif: "https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi2/2019-08-13-5509fd88-12a5387d/12a5387d0cb34b263846d55c76076a16.simg"
url: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi2/2019-08-13-5509fd88-12a5387d/
recipe: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi2/2019-08-13-5509fd88-12a5387d/Singularity
collection: michael-tn/mpi-hello-world
---

# michael-tn/mpi-hello-world:ompi2

```bash
$ singularity pull shub://michael-tn/mpi-hello-world:ompi2
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
    wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.2.tar.bz2 
    tar -xjf openmpi-2.1.2.tar.bz2
    cd openmpi-2.1.2
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

