---
id: 14492
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "gffread_0.12.3"
commit: "11b816cd13e0830a80fc5b780981c2f48656e3fa"
version: "3cbe505f9f6db977fea5eadc818dc84ab538081698588f5d3e2bf997d7227045"
build_date: "2021-03-02T04:40:47.355Z"
size_mb: 134.3203125
size: 140845056
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/gffread_0.12.3/2021-03-02-11b816cd-3cbe505f/3cbe505f9f6db977fea5eadc818dc84ab538081698588f5d3e2bf997d7227045.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/gffread_0.12.3/2021-03-02-11b816cd-3cbe505f/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/gffread_0.12.3/2021-03-02-11b816cd-3cbe505f/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:gffread_0.12.3

```bash
$ singularity pull shub://TomHarrop/assembly-utils:gffread_0.12.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    gffread 0.12.3
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "gffread 0.12.3"

%environment
    export LC_ALL=C
    export PATH="${PATH}:/gffread"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    
    # set up apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
    apt-get update
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

    # install dependencies
    apt-get update
    apt-get install -y \
        git \
        build-essential \
        wget \
        zlib1g-dev

    # install gffread
    git clone https://github.com/gpertea/gffread /gffread
    (
    cd /gffread
    git checkout -f v0.12.3
    git submodule update --init --recursive
    make release
    )

%runscript
    exec /gffread/gffread "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

