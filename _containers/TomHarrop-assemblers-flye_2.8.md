---
id: 13953
name: "TomHarrop/assemblers"
branch: "master"
tag: "flye_2.8"
commit: "e3b37fe19cad1a14ad97299dd0d6389f1e51fb02"
version: "c278cd1200bf7a187d6c6c65a37aac9bebaf84cda46b498d8b506e0900e9e37f"
build_date: "2021-03-15T01:28:36.982Z"
size_mb: 218.375
size: 228982784
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.8/2021-03-15-e3b37fe1-c278cd12/c278cd1200bf7a187d6c6c65a37aac9bebaf84cda46b498d8b506e0900e9e37f.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.8/2021-03-15-e3b37fe1-c278cd12/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.8/2021-03-15-e3b37fe1-c278cd12/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:flye_2.8

```bash
$ singularity pull shub://TomHarrop/assemblers:flye_2.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    Flye 2.8
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.8"

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

    # deps
    apt-get install -y \
        build-essential \
        git \
        python3 \
        python3-setuptools \
        wget \
        zlib1g-dev

    # install flye from release
    # mkdir Flye
    # wget -O "Flye.tar.gz" \
    #     --no-check-certificate \
    #     https://github.com/fenderglass/Flye/archive/2.6.tar.gz
    # tar -zxf Flye.tar.gz \
    #     -C Flye \
    #     --strip-components 1
    # cd Flye || exit 1

    # install Flye from git branch
    git clone https://github.com/fenderglass/Flye
    cd Flye || exit 1
    git checkout -f 2.8
    git submodule update --init --recursive

    # build and install flye
    make

    # python3 setup.py install
    # cd .. || exit 1
    # rm -r Flye.tar.gz Flye

%environment
    export LC_ALL="C"
    export PATH="${PATH}:/Flye/bin"

%runscript
    exec /Flye/bin/flye "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

