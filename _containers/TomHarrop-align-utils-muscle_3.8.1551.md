---
id: 11829
name: "TomHarrop/align-utils"
branch: "master"
tag: "muscle_3.8.1551"
commit: "176c70e0af275f48027fc69466fbc27e7a0af42d"
version: "7c29d097f9db75aba6f929425352ddbb7f27c4dd166cc29a62a8b58538cd00aa"
build_date: "2020-02-19T02:07:09.149Z"
size_mb: 115.5234375
size: 121135104
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/muscle_3.8.1551/2020-02-19-176c70e0-7c29d097/7c29d097f9db75aba6f929425352ddbb7f27c4dd166cc29a62a8b58538cd00aa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/muscle_3.8.1551/2020-02-19-176c70e0-7c29d097/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/muscle_3.8.1551/2020-02-19-176c70e0-7c29d097/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:muscle_3.8.1551

```bash
$ singularity pull shub://TomHarrop/align-utils:muscle_3.8.1551
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    MUSCLE 3.8.1551
    http://www.drive5.com/muscle/downloads.htm
    

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MUSCLE 3.8.1551"

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
        build-essential \
        wget

    # muscle
    wget -O muscle.tar.gz \
        http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_src.tar.gz
    mkdir muscle
    tar -zxf muscle.tar.gz \
        -C muscle \
        --strip-components 1
    cd muscle/src || exit 1
    make
    mv muscle /usr/local/bin/
    cd ../../ || exit 1
    rm -r muscle muscle.tar.gz

%runscript
    exec /usr/local/bin/muscle "$@"

%environment
    export LC_ALL="C"
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

