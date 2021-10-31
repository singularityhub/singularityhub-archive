---
id: 13494
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_4.0.11"
commit: "827051a1e37d196c81d49d142073e252044005fc"
version: "ee39c904fa778a25b456af37734a0f9ef935a8beebdb25a9d790fde0bf6216d7"
build_date: "2020-08-13T04:03:28.955Z"
size_mb: 596.4765625
size: 625451008
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.0.11/2020-08-13-827051a1-ee39c904/ee39c904fa778a25b456af37734a0f9ef935a8beebdb25a9d790fde0bf6216d7.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.0.11/2020-08-13-827051a1-ee39c904/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.0.11/2020-08-13-827051a1-ee39c904/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_4.0.11

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_4.0.11
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    Guppy 4.0.11 without nvidia drivers

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 4.0.11"

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
        nvidia-modprobe \
        software-properties-common \
        wget 

    # byo nvidia driver
    # add-apt-repository -y ppa:graphics-drivers/ppa
    # apt update
    # apt-get install -y \
    #     --no-install-recommends \
    #     libcuda1-430 \
    #     nvidia-430


    # install guppy from ONT repo
    export PLATFORM=$(lsb_release -cs) 
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add - 
    echo \
        "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list 
    apt-get update

    apt-get install -y \
        --no-install-recommends \
        ont-guppy=4.0.11-1~bionic

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

