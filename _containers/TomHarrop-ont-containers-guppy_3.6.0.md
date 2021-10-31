---
id: 12812
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_3.6.0"
commit: "2fa3f3986ad17d8e15ac888dce5dc21c7817c500"
version: "None"
build_date: "2020-06-29T03:18:06.381Z"
size_mb: None
size: 568725504
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.6.0/2020-06-29-2fa3f398-87c4b979/87c4b979478c254e2cafc937d41d4a3d055d363f61875c5121300be394dc99c2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/guppy_3.6.0/2020-06-29-2fa3f398-87c4b979/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.6.0/2020-06-29-2fa3f398-87c4b979/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_3.6.0

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_3.6.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.6.0 without nvidia drivers

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 3.6.0"

%post
    # faster apt downloads
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
        ont-guppy=3.6.0-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

