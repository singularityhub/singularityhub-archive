---
id: 8898
name: "JCSDA/singularity"
branch: "feature/hpccm"
tag: "hpccm"
commit: "98e424de65bcd59f68c232819de481a42b37d301"
version: "d957670f7620f4e4137cc1dd8c9354c3"
build_date: "2019-07-29T17:08:28.203Z"
size_mb: 2655
size: 904749087
sif: "https://datasets.datalad.org/shub/JCSDA/singularity/hpccm/2019-07-29-98e424de-d957670f/d957670f7620f4e4137cc1dd8c9354c3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JCSDA/singularity/hpccm/2019-07-29-98e424de-d957670f/
recipe: https://datasets.datalad.org/shub/JCSDA/singularity/hpccm/2019-07-29-98e424de-d957670f/Singularity
collection: JCSDA/singularity
---

# JCSDA/singularity:hpccm

```bash
$ singularity pull shub://JCSDA/singularity:hpccm
```

## Singularity Recipe

```singularity
BootStrap: docker
From: jcsda/docker:hpccm

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
    CC=mpicc
    export CC
    CXX=mpicxx
    export CXX
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

