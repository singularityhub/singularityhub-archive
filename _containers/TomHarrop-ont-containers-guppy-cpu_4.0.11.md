---
id: 13533
name: "TomHarrop/ont-containers"
branch: "master"
tag: "guppy-cpu_4.0.11"
commit: "cdcdc86f631d80df269652ea75acba166256ebd7"
version: "a7362a23ca7f0393da8b81a124a2395cd7f784e1259c2457532d34271d55a1ca"
build_date: "2020-07-14T21:27:15.954Z"
size_mb: 497.43359375
size: 521596928
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.0.11/2020-07-14-cdcdc86f-a7362a23/a7362a23ca7f0393da8b81a124a2395cd7f784e1259c2457532d34271d55a1ca.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/guppy-cpu_4.0.11/2020-07-14-cdcdc86f-a7362a23/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/guppy-cpu_4.0.11/2020-07-14-cdcdc86f-a7362a23/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:guppy-cpu_4.0.11

```bash
$ singularity pull shub://TomHarrop/ont-containers:guppy-cpu_4.0.11
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    Guppy 4.0.11 without nvidia drivers

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 4.0.11"

%post
    export DEBIAN_FRONTEND=noninteractive
    
    # set up apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
    apt-get  update
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
        ont-guppy-cpu=4.0.11-1~bionic

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

