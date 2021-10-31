---
id: 11936
name: "TomHarrop/misc-utils"
branch: "master"
tag: "borgbackup_1.1.10"
commit: "a47adc2bc5a49be077a4dfb225530a1d8d2583e2"
version: "a2cefe6ec9185d8251314e42930b4496328c7ed08ec98b1021ca01f4e3e29952"
build_date: "2020-01-05T22:05:42.022Z"
size_mb: 214.65234375
size: 225079296
sif: "https://datasets.datalad.org/shub/TomHarrop/misc-utils/borgbackup_1.1.10/2020-01-05-a47adc2b-a2cefe6e/a2cefe6ec9185d8251314e42930b4496328c7ed08ec98b1021ca01f4e3e29952.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/misc-utils/borgbackup_1.1.10/2020-01-05-a47adc2b-a2cefe6e/
recipe: https://datasets.datalad.org/shub/TomHarrop/misc-utils/borgbackup_1.1.10/2020-01-05-a47adc2b-a2cefe6e/Singularity
collection: TomHarrop/misc-utils
---

# TomHarrop/misc-utils:borgbackup_1.1.10

```bash
$ singularity pull shub://TomHarrop/misc-utils:borgbackup_1.1.10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help

    borgbackup 1.1.10

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "borgbackup 1.1.10"

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
        python-virtualenv \
        python3 \
        python3-dev \
        python3-pip \
        python3-virtualenv \
        wget 

    # download borg
    wget -O "borg.tar.gz" \
        --no-check-certificate \
https://github.com/borgbackup/borg/releases/download/1.1.10/borgbackup-1.1.10.tar.gz
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

