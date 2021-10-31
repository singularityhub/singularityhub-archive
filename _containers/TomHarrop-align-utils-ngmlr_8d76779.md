---
id: 11669
name: "TomHarrop/align-utils"
branch: "master"
tag: "ngmlr_8d76779"
commit: "68c5d996516af3c9250fdde263bd8711f04f6b7f"
version: "aad6421f78b13b21a29665e775b2e8b94d97b67fe9fc8b2edd90686dcb0216d7"
build_date: "2019-12-09T01:38:42.722Z"
size_mb: 154.71875
size: 162234368
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/ngmlr_8d76779/2019-12-09-68c5d996-aad6421f/aad6421f78b13b21a29665e775b2e8b94d97b67fe9fc8b2edd90686dcb0216d7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/ngmlr_8d76779/2019-12-09-68c5d996-aad6421f/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/ngmlr_8d76779/2019-12-09-68c5d996-aad6421f/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:ngmlr_8d76779

```bash
$ singularity pull shub://TomHarrop/align-utils:ngmlr_8d76779
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    NGMLR 8d76779
    https://github.com/philres/ngmlr

%labels
    MAINTAINER "Tom Harrop"
    VERSION "NGMLR 8d76779"

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
        cmake \
        git \
        wget \
        zlib1g-dev

    # download 
    git clone https://github.com/philres/ngmlr.git
    cd ngmlr || exit 1
    git checkout \
        --recurse-submodules --force \
        8d76779

    # build
    mkdir -p build
    cd build || exit 1
    cmake ..
    make
    make install

    # tidy up
    cd ../../ || exit 1
    rm -fr ngmlr

%runscript
    exec /usr/local/bin/ngmlr "$@"
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

