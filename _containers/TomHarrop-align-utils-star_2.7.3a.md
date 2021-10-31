---
id: 12916
name: "TomHarrop/align-utils"
branch: "master"
tag: "star_2.7.3a"
commit: "729b6018f27cdc5dde533fabc431b834bbb2bc52"
version: "e78f03a9c3f8d7deb74dc78c06a66cc5fdbea32eac4792885165b4df90bc1488"
build_date: "2020-05-06T22:08:28.842Z"
size_mb: 111.02734375
size: 116420608
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/star_2.7.3a/2020-05-06-729b6018-e78f03a9/e78f03a9c3f8d7deb74dc78c06a66cc5fdbea32eac4792885165b4df90bc1488.sif"
url: https://datasets.datalad.org/shub/TomHarrop/align-utils/star_2.7.3a/2020-05-06-729b6018-e78f03a9/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/star_2.7.3a/2020-05-06-729b6018-e78f03a9/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:star_2.7.3a

```bash
$ singularity pull shub://TomHarrop/align-utils:star_2.7.3a
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help

    Container for STAR 2.7.3a
    https://github.com/alexdobin/STAR/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "STAR 2.7.3a"

%runscript

    exec /usr/local/bin/STAR "$@"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
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
        https://github.com/alexdobin/STAR/archive/2.7.3a.tar.gz
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

