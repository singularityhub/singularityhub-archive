---
id: 11742
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_3.4.1"
commit: "79f06a37fb963cd424c379cece82c10ba68ef8da"
version: "103dff5215a1c9e8d20749e3c8b3b6984400bb1d06f32422323c250a111e9f78"
build_date: "2019-12-19T01:39:25.955Z"
size_mb: 355.9296875
size: 373219328
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.4.1/2019-12-19-79f06a37-103dff52/103dff5215a1c9e8d20749e3c8b3b6984400bb1d06f32422323c250a111e9f78.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/guppy_3.4.1/2019-12-19-79f06a37-103dff52/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.4.1/2019-12-19-79f06a37-103dff52/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_3.4.1

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_3.4.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.4.1 without nvidia drivers

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 3.4.1"

%post
    # faster apt downloads, will it break?
    export DEBIAN_FRONTEND=noninteractive
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
        ont-guppy=3.4.1-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

