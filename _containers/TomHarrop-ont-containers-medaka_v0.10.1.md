---
id: 11652
name: "TomHarrop/ont-containers"
branch: "master"
tag: "medaka_v0.10.1"
commit: "616f9abba91d1271dbba2ef245f97c59b65e68c5"
version: "e0e5af11bf7d1bdcc92b94f4102aa482933abebd42a174579b1e748227a89061"
build_date: "2019-12-03T23:40:17.073Z"
size_mb: 2146.98046875
size: 2251272192
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/medaka_v0.10.1/2019-12-03-616f9abb-e0e5af11/e0e5af11bf7d1bdcc92b94f4102aa482933abebd42a174579b1e748227a89061.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/medaka_v0.10.1/2019-12-03-616f9abb-e0e5af11/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/medaka_v0.10.1/2019-12-03-616f9abb-e0e5af11/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:medaka_v0.10.1

```bash
$ singularity pull shub://TomHarrop/ont-containers:medaka_v0.10.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.14.0-gpu-py3

%help
    medaka 7574cf1
    https://github.com/nanoporetech/medaka

%labels
    MAINTAINER "Tom Harrop"
    VERSION "medaka v0.10.1"

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

    # dependencies
    apt update
    apt install -y \
        cmake \
        file \
        git-lfs \
        libbz2-dev \
        libcurl4-openssl-dev \
        liblzma-dev \
        libncurses-dev  \
        libssl-dev \
        virtualenv \
        wget \
        zlib1g-dev 

    # medaka gpu
    GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/nanoporetech/medaka.git
    cd medaka || exit 1
    git checkout \
        --recurse-submodules --force \
        v0.10.1
    git lfs pull
    sed -i 's/tensorflow/tensorflow-gpu/' requirements.txt
    make install # this builds the binaries in bincache and installs into venv

    # now install system-wide
    /usr/local/bin/pip3 install -r requirements.txt
    MEDAKA_BINARIES=1 python3 setup.py install

    # tidy up
    rm -r /medaka

%runscript
    exec /usr/local/bin/medaka "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

