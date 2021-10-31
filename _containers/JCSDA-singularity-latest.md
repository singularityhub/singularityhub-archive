---
id: 5347
name: "JCSDA/singularity"
branch: "master"
tag: "latest"
commit: "c65f9145fb98266e03a3a49ee757b782cbce25ec"
version: "cc14d4405f8c119ab42ae5effcead576"
build_date: "2021-03-10T18:28:53.292Z"
size_mb: 2891.0
size: 1009127455
sif: "https://datasets.datalad.org/shub/JCSDA/singularity/latest/2021-03-10-c65f9145-cc14d440/cc14d4405f8c119ab42ae5effcead576.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/JCSDA/singularity/latest/2021-03-10-c65f9145-cc14d440/
recipe: https://datasets.datalad.org/shub/JCSDA/singularity/latest/2021-03-10-c65f9145-cc14d440/Singularity
collection: JCSDA/singularity
---

# JCSDA/singularity:latest

```bash
$ singularity pull shub://JCSDA/singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: jcsda/docker-gnu-openmpi-dev:latest

%labels
MAINTAINER Mark Miesch
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
    echo "Install additional software here"
    mkdir -p /var/go
```

## Collection

 - Name: [JCSDA/singularity](https://github.com/JCSDA/singularity)
 - License: None

