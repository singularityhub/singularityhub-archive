---
id: 13962
name: "TomHarrop/variant-utils"
branch: "master"
tag: "sniffles_1.0.12a"
commit: "960d14d0140c4b14bd27bd8ca6aef0cac957896f"
version: "89d90a7f7d9e87209edcbbec821f83f51672cc74cfa064fd0b444005ba36f1aa"
build_date: "2020-08-17T21:39:32.166Z"
size_mb: 169.7890625
size: 178036736
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_1.0.12a/2020-08-17-960d14d0-89d90a7f/89d90a7f7d9e87209edcbbec821f83f51672cc74cfa064fd0b444005ba36f1aa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/sniffles_1.0.12a/2020-08-17-960d14d0-89d90a7f/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/sniffles_1.0.12a/2020-08-17-960d14d0-89d90a7f/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:sniffles_1.0.12a

```bash
$ singularity pull shub://TomHarrop/variant-utils:sniffles_1.0.12a
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    Sniffles 1.0.12a
    https://github.com/fritzsedlazeck/Sniffles

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Sniffles 1.0.12a"

%environment
    export PATH="${PATH}:/sniffles/bin/sniffles-core-1.0.12"
    export LC_ALL=C

%runscript
    exec /sniffles/bin/sniffles-core-1.0.12/sniffles "$@"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    # reset apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
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

    apt-get update
    apt-get upgrade -y --fix-missing

    # dependencies
    apt-get install -y \
        build-essential \
        cmake \
        wget \
        zlib1g-dev

    # sniffles
    wget -O "/sniffles.tar.gz" \
        --no-check-certificate \
        https://github.com/fritzsedlazeck/Sniffles/archive/v1.0.12a.tar.gz

    mkdir /sniffles
    tar -zxf /sniffles.tar.gz \
        -C /sniffles \
        --strip-components 1
    (
    cd /sniffles || exit 1
    mkdir build
    cd build || exit 1
    cmake ..
    make && make install
    )

    rm /sniffles.tar.gz
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

