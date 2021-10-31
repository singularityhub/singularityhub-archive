---
id: 461
name: "michael-tn/mpi-hello-world"
branch: "master"
tag: "1.2/singularity.ompi212"
commit: "7f9c97a5f8c8597df3065cc9ad3c87770aaef9ea"
version: "885f99169e148dd83668546775f44e7b"
build_date: "2017-10-20T18:53:21.553Z"
size_mb: 686
size: 197201951
sif: "https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/1.2/singularity.ompi212/2017-10-20-7f9c97a5-885f9916/885f99169e148dd83668546775f44e7b.simg"
url: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/1.2/singularity.ompi212/2017-10-20-7f9c97a5-885f9916/
recipe: https://datasets.datalad.org/shub/michael-tn/mpi-hello-world/1.2/singularity.ompi212/2017-10-20-7f9c97a5-885f9916/Singularity
collection: michael-tn/mpi-hello-world
---

# michael-tn/mpi-hello-world:1.2/singularity.ompi212

```bash
$ singularity pull shub://michael-tn/mpi-hello-world:1.2/singularity.ompi212
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

