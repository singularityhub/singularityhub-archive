---
id: 3044
name: "alejandrox1/singularity-test"
branch: "master"
tag: "latest"
commit: "ba084cbed20c18448ee088a4e983b2a702b4b4ee"
version: "54533242296bd3cc5669af585906ac8b"
build_date: "2018-06-05T07:53:14.364Z"
size_mb: 874
size: 146878495
sif: "https://datasets.datalad.org/shub/alejandrox1/singularity-test/latest/2018-06-05-ba084cbe-54533242/54533242296bd3cc5669af585906ac8b.simg"
url: https://datasets.datalad.org/shub/alejandrox1/singularity-test/latest/2018-06-05-ba084cbe-54533242/
recipe: https://datasets.datalad.org/shub/alejandrox1/singularity-test/latest/2018-06-05-ba084cbe-54533242/Singularity
collection: alejandrox1/singularity-test
---

# alejandrox1/singularity-test:latest

```bash
$ singularity pull shub://alejandrox1/singularity-test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
    AUTHOR alarcj137@gmail.com
    VERSION v1.0

%help
    Singularity test - running a containarized MPI executable.

%files
    ./mpi_hello_world.c
    ./Makefile

%post
    mkdir -p /tmp/git
    cd /tmp/git
    apt-get update -y && apt-get install -y git build-essential autoconf libtool-bin flex
    [ -d ompi ] && rm -rf ompi
    git clone https://github.com/open-mpi/ompi.git
    cd ompi
    ./autogen.pl
    ./configure --prefix=/usr/local
    make -j 10
    make install
    ldconfig

    /usr/local/bin/mpicc examples/ring_c.c -o /usr/bin/mpi_ring

%test
    /usr/local/bin/mpirun --allow-run-as-root /usr/bin/mpi_ring

%environment
    # export PATH="$PATH:$PWD"

%runscript
    cat /etc/*release
    cd src/
    make
    cd ../
    cp src/mpi_hello_world /usr/bin/
    exec /usr/local/bin/mpirun --version
```

## Collection

 - Name: [alejandrox1/singularity-test](https://github.com/alejandrox1/singularity-test)
 - License: None

