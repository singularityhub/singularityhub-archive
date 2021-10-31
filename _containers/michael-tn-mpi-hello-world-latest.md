---
id: 462
name: "michael-tn/mpi-hello-world"
branch: "master"
tag: "latest"
commit: "87b313a3caa5231e64a73c8c902a39e0ef629a00"
version: "c59fae0048895204dcf1df163e33ac93"
build_date: "2021-02-26T15:31:55.452Z"
size_mb: 717
size: 203882527
sif: "https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/latest/2021-02-26-87b313a3-c59fae00/c59fae0048895204dcf1df163e33ac93.simg"
url: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/latest/2021-02-26-87b313a3-c59fae00/
recipe: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/latest/2021-02-26-87b313a3-c59fae00/Singularity
collection: michael-tn/mpi-hello-world
---

# michael-tn/mpi-hello-world:latest

```bash
$ singularity pull shub://michael-tn/mpi-hello-world:latest
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

