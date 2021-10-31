---
id: 14615
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_4.2.2"
commit: "edb09ec794640b802a2a2058b3b1aee32606c252"
version: "09f565f94ae176548f04e0f316cdb31138d08c2e3a7657b722dae4c2d8faef96"
build_date: "2021-01-24T22:24:40.000Z"
size_mb: 563.33203125
size: 590696448
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.2.2/2021-01-24-edb09ec7-09f565f9/09f565f94ae176548f04e0f316cdb31138d08c2e3a7657b722dae4c2d8faef96.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.2.2/2021-01-24-edb09ec7-09f565f9/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.2.2/2021-01-24-edb09ec7-09f565f9/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_4.2.2

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_4.2.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    Guppy 4.2.2 without nvidia drivers

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
        ont-guppy=4.2.2-1~bionic

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

