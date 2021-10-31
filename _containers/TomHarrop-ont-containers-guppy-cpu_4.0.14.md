---
id: 13928
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy-cpu_4.0.14"
commit: "38cee2a2fafa1a322ba1e8dfe408d1c766d6d73c"
version: "7cbe1903c195e32ea0841c1225b265b5d37dfda988812a48841368e8be29394b"
build_date: "2020-08-13T04:40:15.773Z"
size_mb: 496.5625
size: 520683520
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.0.14/2020-08-13-38cee2a2-7cbe1903/7cbe1903c195e32ea0841c1225b265b5d37dfda988812a48841368e8be29394b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/guppy-cpu_4.0.14/2020-08-13-38cee2a2-7cbe1903/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.0.14/2020-08-13-38cee2a2-7cbe1903/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy-cpu_4.0.14

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy-cpu_4.0.14
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    Guppy 4.0.14 CPU version

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 4.0.14"

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
        ont-guppy-cpu=4.0.14-1~bionic

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

