---
id: 9538
name: "JCSDA/singularity"
branch: "feature/academy"
tag: "academy"
commit: "1dc081e08be1e8fd98e9ff14d25a2a74c714c802"
version: "1123ce0d51e62aeda7461bc714bcb528"
build_date: "2019-06-04T21:29:58.322Z"
size_mb: 2861
size: 1008840735
sif: "https://datasets.datalad.org/shub/JCSDA/singularity/academy/2019-06-04-1dc081e0-1123ce0d/1123ce0d51e62aeda7461bc714bcb528.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JCSDA/singularity/academy/2019-06-04-1dc081e0-1123ce0d/
recipe: https://datasets.datalad.org/shub/JCSDA/singularity/academy/2019-06-04-1dc081e0-1123ce0d/Singularity
collection: JCSDA/singularity
---

# JCSDA/singularity:academy

```bash
$ singularity pull shub://JCSDA/singularity:academy
```

## Singularity Recipe

```singularity
BootStrap: docker
From: jcsda/docker

%labels
MAINTAINER Xin Zhang
SPECIES JEDI

%runscript
    echo "Welcome, this is Singularity container for JEDI with GNU 7"

%environments
    DISPLAY=:0.0
    export DISPLAY
    TERM=xterm
    export TERM
    FC=mpifort
    export FC
    CXX=mpicxx
    export CXX
    CC=mpicc
    export CC
    GIT_MERGE_AUTOEDIT=no
    export GIT_MERGE_AUTOEDIT

%post
    echo "Hello from inside the container"
    mkdir -p /var/go
    apt-get update
    apt-get install -y --no-install-recommends default-jre default-jdk
    cd /opt
    wget https://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-4.10.7.tgz
    tar xvf PanoplyJ-4.10.7.tgz
    rm PanoplyJ-4.10.7.tgz
    echo 'export PATH=/opt/PanoplyJ:$PATH' >> /etc/bash.bashrc    
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [JCSDA/singularity](https://github.com/JCSDA/singularity)
 - License: None

