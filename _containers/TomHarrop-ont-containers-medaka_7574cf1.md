---
id: 11431
name: "TomHarrop/ont-containers"
branch: "master"
tag: "medaka_7574cf1"
commit: "0a7f4c632e78b4c99afbe5b52a6838d01a0cabf3"
version: "2e10ba7f142261a1e87c66e4361b5ab6bb9088e2076037fd36111741be357ec3"
build_date: "2019-12-02T10:29:55.330Z"
size_mb: 2146.4921875
size: 2250760192
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/medaka_7574cf1/2019-12-02-0a7f4c63-2e10ba7f/2e10ba7f142261a1e87c66e4361b5ab6bb9088e2076037fd36111741be357ec3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/medaka_7574cf1/2019-12-02-0a7f4c63-2e10ba7f/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/medaka_7574cf1/2019-12-02-0a7f4c63-2e10ba7f/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:medaka_7574cf1

```bash
$ singularity pull shub://TomHarrop/ont-containers:medaka_7574cf1
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
    VERSION "medaka 7574cf1"

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
        7574cf1
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

