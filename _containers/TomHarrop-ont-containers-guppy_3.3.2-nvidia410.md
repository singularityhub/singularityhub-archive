---
id: 11430
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_3.3.2-nvidia410"
commit: "dbe918978c7315abff9c1c721eb87849443aea09"
version: "8e2fd88530f73c7d02cb3a9be5f500e920f2b41e033978b8b2aeaa02ae621a13"
build_date: "2019-11-08T02:00:23.430Z"
size_mb: 578.9609375
size: 607084544
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.2-nvidia410/2019-11-08-dbe91897-8e2fd885/8e2fd88530f73c7d02cb3a9be5f500e920f2b41e033978b8b2aeaa02ae621a13.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.2-nvidia410/2019-11-08-dbe91897-8e2fd885/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.2-nvidia410/2019-11-08-dbe91897-8e2fd885/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_3.3.2-nvidia410

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_3.3.2-nvidia410
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.3.2 with nvidia-410

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 3.3.2"

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
    add-apt-repository -y ppa:graphics-drivers/ppa
    apt update
    apt-get install -y \
        --no-install-recommends \
        libcuda1-410 \
        nvidia-410

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
        ont-guppy=3.3.2-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

