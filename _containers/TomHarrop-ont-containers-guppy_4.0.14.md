---
id: 13929
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_4.0.14"
commit: "38cee2a2fafa1a322ba1e8dfe408d1c766d6d73c"
version: "76906fc36d7b24bf152092c2c968835a96142a1815b8a626f7b9a7dcdc67f143"
build_date: "2020-10-20T02:55:45.433Z"
size_mb: 591.56640625
size: 620302336
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.0.14/2020-10-20-38cee2a2-76906fc3/76906fc36d7b24bf152092c2c968835a96142a1815b8a626f7b9a7dcdc67f143.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.0.14/2020-10-20-38cee2a2-76906fc3/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_4.0.14/2020-10-20-38cee2a2-76906fc3/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_4.0.14

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_4.0.14
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    Guppy 4.0.14 without nvidia drivers

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
        ont-guppy=4.0.14-1~bionic

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

