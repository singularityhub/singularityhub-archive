---
id: 11558
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_3.3.3-nvidia418"
commit: "6c92a77f3ef40cfbffe3b6dabddf4bc450afebab"
version: "cb2097c93a5f549bfaa74248bfef0ed594c2728e673b6a0451b00cbc00b510c1"
build_date: "2019-12-03T02:50:25.163Z"
size_mb: 579.48828125
size: 607637504
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.3-nvidia418/2019-12-03-6c92a77f-cb2097c9/cb2097c93a5f549bfaa74248bfef0ed594c2728e673b6a0451b00cbc00b510c1.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.3-nvidia418/2019-12-03-6c92a77f-cb2097c9/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.3-nvidia418/2019-12-03-6c92a77f-cb2097c9/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_3.3.3-nvidia418

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_3.3.3-nvidia418
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.3.3 with nvidia-410

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 3.3.3"

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
        libcuda1-418 \
        nvidia-418

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
        ont-guppy=3.3.3-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

