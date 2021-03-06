---
id: 14757
name: "TomHarrop/align-utils"
branch: "master"
tag: "star_2.7.6a"
commit: "fbf82ef8faee28fb0dd9f17e94b510e5b801c314"
version: "7935068d6de9f39d17eb2cebb569db7e0a4b4d8516e8c99affc23239efb4f00d"
build_date: "2020-12-17T22:19:33.521Z"
size_mb: 115.12109375
size: 120713216
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/star_2.7.6a/2020-12-17-fbf82ef8-7935068d/7935068d6de9f39d17eb2cebb569db7e0a4b4d8516e8c99affc23239efb4f00d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/star_2.7.6a/2020-12-17-fbf82ef8-7935068d/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/star_2.7.6a/2020-12-17-fbf82ef8-7935068d/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:star_2.7.6a

```bash
$ singularity pull shub://TomHarrop/align-utils:star_2.7.6a
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help

    Container for STAR 2.7.6a
    https://github.com/alexdobin/STAR/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "STAR 2.7.6a"

%runscript

    exec /usr/local/bin/STAR "$@"

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
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe>
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted >
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricte>
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted>

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    apt-get update
    apt-get install -y \
        build-essential \
        wget \
        zlib1g-dev

    # install STAR
    wget -O "star.tar.gz" \
        --no-check-certificate \
        https://github.com/alexdobin/STAR/archive/2.7.6a.tar.gz
    mkdir star
    tar -zxf star.tar.gz \
        -C star \
        --strip-components 1
    cd star/source || exit 1
    make
    cp STAR /usr/local/bin
    cd ../../ || exit 1
    rm -rf star.tar.gz star
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

