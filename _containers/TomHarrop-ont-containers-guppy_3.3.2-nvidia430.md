---
id: 11429
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_3.3.2-nvidia430"
commit: "dbe918978c7315abff9c1c721eb87849443aea09"
version: "3246a7298a9a59b94d0e6e13ea8e0f32c892943a131beedb5b3b3034730f2a1f"
build_date: "2019-11-08T02:05:58.636Z"
size_mb: 583.8125
size: 612171776
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.2-nvidia430/2019-11-08-dbe91897-3246a729/3246a7298a9a59b94d0e6e13ea8e0f32c892943a131beedb5b3b3034730f2a1f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/guppy_3.3.2-nvidia430/2019-11-08-dbe91897-3246a729/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.3.2-nvidia430/2019-11-08-dbe91897-3246a729/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_3.3.2-nvidia430

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_3.3.2-nvidia430
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.3.2 with nvidia-430

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
        libcuda1-430 \
        nvidia-430

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

