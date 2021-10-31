---
id: 460
name: "michael-tn/mpi-hello-world"
branch: "master"
tag: "ompi212"
commit: "a0b6b583c42deb7aa583c064867bf9f0883aebc7"
version: "1d917ac4a26c45f0e5ffdc7d79fdd1c9"
build_date: "2017-10-20T18:53:21.561Z"
size_mb: 687
size: 197201951
sif: "https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi212/2017-10-20-a0b6b583-1d917ac4/1d917ac4a26c45f0e5ffdc7d79fdd1c9.simg"
url: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi212/2017-10-20-a0b6b583-1d917ac4/
recipe: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/ompi212/2017-10-20-a0b6b583-1d917ac4/Singularity
collection: michael-tn/mpi-hello-world
---

# michael-tn/mpi-hello-world:ompi212

```bash
$ singularity pull shub://michael-tn/mpi-hello-world:ompi212
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

