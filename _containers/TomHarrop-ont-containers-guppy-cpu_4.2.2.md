---
id: 14614
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy-cpu_4.2.2"
commit: "7bbe30651bb0bb5506cff3412840685b8a7702c6"
version: "e2805f85d4fc7e6ca13ec057300e2355994390b4d6c98b2e42edb3cdaf61e394"
build_date: "2021-03-31T22:10:30.258Z"
size_mb: 499.51171875
size: 523776000
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.2.2/2021-03-31-7bbe3065-e2805f85/e2805f85d4fc7e6ca13ec057300e2355994390b4d6c98b2e42edb3cdaf61e394.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.2.2/2021-03-31-7bbe3065-e2805f85/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.2.2/2021-03-31-7bbe3065-e2805f85/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy-cpu_4.2.2

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy-cpu_4.2.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    Guppy 4.2.2 CPU version

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 4.2.2"

%post
    export DEBIAN_FRONTEND=noninteractive
    
    # set up apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
    apt-get  update
    apt-get upgrade -y --fix-missing


    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # deps
    apt-get update
    apt-get install -y \
        apt-transport-https \
        lsb-release \
        software-properties-common \
        wget 

    # install guppy from ONT repo
    export PLATFORM=$(lsb_release -cs) 
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add - 
    echo \
        "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list 
    apt-get update

    apt-get install -y \
        ont-guppy-cpu=4.2.2-1~bionic

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

