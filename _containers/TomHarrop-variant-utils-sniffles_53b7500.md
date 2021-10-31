---
id: 13963
name: "TomHarrop/variant-utils"
branch: "master"
tag: "sniffles_53b7500"
commit: "e221244cc112a929d41a9622fb8e3f835e72a4f6"
version: "44e06b7f5789ebcc73b19326bcf7bc10d947d63ad71a2e660407b4234b90ee1b"
build_date: "2020-08-17T22:14:49.748Z"
size_mb: 193.42578125
size: 202821632
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_53b7500/2020-08-17-e221244c-44e06b7f/44e06b7f5789ebcc73b19326bcf7bc10d947d63ad71a2e660407b4234b90ee1b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/sniffles_53b7500/2020-08-17-e221244c-44e06b7f/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_53b7500/2020-08-17-e221244c-44e06b7f/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:sniffles_53b7500

```bash
$ singularity pull shub://TomHarrop/variant-utils:sniffles_53b7500
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    Sniffles 53b7500
    https://github.com/fritzsedlazeck/Sniffles

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Sniffles 53b7500"

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
    git checkout -f 53b7500
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

