---
id: 14625
name: "TomHarrop/ont-containers"
branch: "master"
tag: "readfish_0.0.5a3"
commit: "a4158d02ce125f80141fceff1bb46167af81971e"
version: "5b72413a1db09b851ba28ad6a321a6fb38972ce07f78ded45081f76a9f99bbca"
build_date: "2020-10-20T20:25:03.799Z"
size_mb: 1476.66796875
size: 1548398592
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/readfish_0.0.5a3/2020-10-20-a4158d02-5b72413a/5b72413a1db09b851ba28ad6a321a6fb38972ce07f78ded45081f76a9f99bbca.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/readfish_0.0.5a3/2020-10-20-a4158d02-5b72413a/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/readfish_0.0.5a3/2020-10-20-a4158d02-5b72413a/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:readfish_0.0.5a3

```bash
$ singularity pull shub://TomHarrop/ont-containers:readfish_0.0.5a3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    readfish 0.0.5a3 from pip
    MinKNOW (minion-nc) 20.06.5-1~bionic
    Guppy (ont-guppy) 4.2.2-1~bionic

%labels
    MAINTAINER "Tom Harrop"
    VERSION "readfish 0.0.5a3"

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

    # install dependencies
    # (needs pip)
    apt update
    apt install -y \
        apt-transport-https \
        git \
        libasound2 \
        libcanberra-gtk-module \
        libcanberra-gtk3-module \
        libgconf-2-4 \
        libgtk-3-dev \
        libnss3 \
        libxss1 \
        lsb-release \
        nvidia-modprobe \
        python3-pip \
        python3.7 \
        python3.7-dev \
        software-properties-common \
        wget 

    # install minknow and guppy
    wget \
        -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add -
    echo "deb http://mirror.oxfordnanoportal.com/apt bionic-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list

    apt-get update
    apt-get install -y \
        --no-install-recommends \
        minion-nc=20.06.5-1~bionic \
        ont-guppy=4.2.2-1~bionic

    # setup python and install readfish
    /usr/bin/python3.7 -m pip install --upgrade pip setuptools wheel
    /usr/bin/python3.7 -m pip install \
        git+https://github.com/nanoporetech/read_until_api@v3.0.0

    # install readfish from wheel on pypi
    # this is a bit of a hack but it's set to python==3.7 
    # so it won't install on 3.7.5 (maybe a mistake?)
    /usr/bin/python3.7 -m pip install \
        --ignore-requires-python \
        readfish==0.0.5a3

%runscript
    exec /usr/local/bin/readfish "@$"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

