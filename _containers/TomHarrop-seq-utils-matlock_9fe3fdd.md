---
id: 12352
name: "TomHarrop/seq-utils"
branch: "master"
tag: "matlock_9fe3fdd"
commit: "96b30d44ab85218a76a8a890d1499139f4229843"
version: "ccafc433a4538f37686c2d454f5813aa42c49e7fd89176226ed5fa302a0fe560"
build_date: "2020-03-02T01:17:11.401Z"
size_mb: 164.1484375
size: 172122112
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/matlock_9fe3fdd/2020-03-02-96b30d44-ccafc433/ccafc433a4538f37686c2d454f5813aa42c49e7fd89176226ed5fa302a0fe560.sif"
url: https://datasets.datalad.org/shub/TomHarrop/seq-utils/matlock_9fe3fdd/2020-03-02-96b30d44-ccafc433/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/matlock_9fe3fdd/2020-03-02-96b30d44-ccafc433/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:matlock_9fe3fdd

```bash
$ singularity pull shub://TomHarrop/seq-utils:matlock_9fe3fdd
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Matlock
    https://github.com/phasegenomics/matlock

%labels
    VERSION "Matlock 9fe3fdd"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
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

    # apt dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        git \
        libbz2-dev \
        libgsl-dev \
        liblzma-dev \
        wget \
        zlib1g-dev

    # install matlock
    git clone https://github.com/phasegenomics/matlock.git /matlock
    cd /matlock || exit 1
    git checkout -f 9fe3fdd
    git submodule update --init --recursive
    make

%environment
    export LC_ALL=C
    export PATH="${PATH}:/matlock/bin"

%runscript
    exec /matlock/bin/matlock "$@"
```

## Collection

 - Name: [TomHarrop/seq-utils](https://github.com/TomHarrop/seq-utils)
 - License: None

