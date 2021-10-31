---
id: 11960
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy_3.4.4"
commit: "c18076eb766c3823b9b0fa500bcb5bc4eafdc125"
version: "9df30f57c8b7928c6923989ae4df8e965fc39aaa5a23c5ba4739194c033f45f4"
build_date: "2020-06-29T03:18:13.367Z"
size_mb: 376.57421875
size: 394866688
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.4.4/2020-06-29-c18076eb-9df30f57/9df30f57c8b7928c6923989ae4df8e965fc39aaa5a23c5ba4739194c033f45f4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/guppy_3.4.4/2020-06-29-c18076eb-9df30f57/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy_3.4.4/2020-06-29-c18076eb-9df30f57/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy_3.4.4

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy_3.4.4
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
        ont-guppy=3.4.4-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

