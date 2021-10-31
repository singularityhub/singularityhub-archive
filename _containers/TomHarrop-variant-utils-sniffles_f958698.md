---
id: 14547
name: "TomHarrop/variant-utils"
branch: "master"
tag: "sniffles_f958698"
commit: "56857e2f4b807c5aaad56ce621e214fb7e0e9f61"
version: "71a0c206aefdd1ebb6630eb08d8300c87e238794733cf83e5d62737c4906a927"
build_date: "2020-10-05T03:06:48.095Z"
size_mb: 194.74609375
size: 204206080
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_f958698/2020-10-05-56857e2f-71a0c206/71a0c206aefdd1ebb6630eb08d8300c87e238794733cf83e5d62737c4906a927.sif"
url: https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_f958698/2020-10-05-56857e2f-71a0c206/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_f958698/2020-10-05-56857e2f-71a0c206/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:sniffles_f958698

```bash
$ singularity pull shub://TomHarrop/variant-utils:sniffles_f958698
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    Sniffles f958698
    https://github.com/fritzsedlazeck/Sniffles

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Sniffles f958698"

%environment
    export PATH="${PATH}:/sniffles/bin/sniffles-core-1.0.12"
    export LC_ALL=C

%runscript
    exec /sniffles/bin/sniffles-core-1.0.12/sniffles "$@"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    # reset apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
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

    apt-get update
    apt-get upgrade -y --fix-missing

    # dependencies
    apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        zlib1g-dev

    #############################
    # CHECK PATH ON NEW COMMITS #
    #############################
    # install Sniffles from git branch
    git clone \
        https://github.com/fritzsedlazeck/Sniffles \
        /sniffles

    (
    cd /sniffles || exit 1
    git checkout -f f958698
    git submodule update --init --recursive
    mkdir build
    cd build || exit 1
    cmake ..
    make && make install
    )
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

