---
id: 14230
name: "TomHarrop/misc-utils"
branch: "master"
tag: "borgbackup_1.1.13"
commit: "e3e3cf63db725b128e2366f6b742422260db69cb"
version: "4241d1f1d11fa4c8bd30ed14254314c046c28c5a671593a92abb55ef3d4af49a"
build_date: "2020-09-15T05:11:12.991Z"
size_mb: 212.6328125
size: 222961664
sif: "https://datasets.datalad.org/shub/TomHarrop/misc-utils/borgbackup_1.1.13/2020-09-15-e3e3cf63-4241d1f1/4241d1f1d11fa4c8bd30ed14254314c046c28c5a671593a92abb55ef3d4af49a.sif"
url: https://datasets.datalad.org/shub/TomHarrop/misc-utils/borgbackup_1.1.13/2020-09-15-e3e3cf63-4241d1f1/
recipe: https://datasets.datalad.org/shub/TomHarrop/misc-utils/borgbackup_1.1.13/2020-09-15-e3e3cf63-4241d1f1/Singularity
collection: TomHarrop/misc-utils
---

# TomHarrop/misc-utils:borgbackup_1.1.13

```bash
$ singularity pull shub://TomHarrop/misc-utils:borgbackup_1.1.13
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help

    borgbackup 1.1.13

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "borgbackup 1.1.13"

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

    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        fuse \
        libacl1 \
        libacl1-dev \
        libfuse-dev \
        libssl-dev \
        openssl \
        pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        python3-virtualenv \
        wget 

    # download borg
    wget -O "borg.tar.gz" \
        --no-check-certificate \
https://github.com/borgbackup/borg/releases/download/1.1.13/borgbackup-1.1.13.tar.gz
    mkdir borg
    tar -zxf borg.tar.gz \
        -C borg \
        --strip-components 1

    # install
    cd borg || exit 1
    pip3 install -r requirements.d/development.txt
    pip3 install -r requirements.d/docs.txt
    pip3 install -r requirements.d/fuse.txt
    pip3 install .

    cd .. || exit 1
    rm -rf borg borg.tar.gz

%runscript
    exec /usr/local/bin/borg "$@"
```

## Collection

 - Name: [TomHarrop/misc-utils](https://github.com/TomHarrop/misc-utils)
 - License: None

