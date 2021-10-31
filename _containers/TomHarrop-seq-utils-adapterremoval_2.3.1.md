---
id: 13473
name: "TomHarrop/seq-utils"
branch: "master"
tag: "adapterremoval_2.3.1"
commit: "e7ea0a09bb920e5e4750d287baca39f7d2f8e2d9"
version: "d9753cc0794729b7be4eee0d0733669a983d86fd6f18200872cf4af572c8b4a9"
build_date: "2021-01-03T09:48:05.237Z"
size_mb: 128.5859375
size: 134832128
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/adapterremoval_2.3.1/2021-01-03-e7ea0a09-d9753cc0/d9753cc0794729b7be4eee0d0733669a983d86fd6f18200872cf4af572c8b4a9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/seq-utils/adapterremoval_2.3.1/2021-01-03-e7ea0a09-d9753cc0/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/adapterremoval_2.3.1/2021-01-03-e7ea0a09-d9753cc0/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:adapterremoval_2.3.1

```bash
$ singularity pull shub://TomHarrop/seq-utils:adapterremoval_2.3.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    AdapterRemoval
    https://github.com/mikkelschubert/adapterremoval

%environment
    export LC_ALL=C

%post
    # variable
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive

    # set up apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
    apt-get  update
    apt-get upgrade -y --fix-missing
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
    apt-get update
    apt-get install -y \
        build-essential \
        git \
        libbz2-dev \
        wget \
        zlib1g-dev 

    # Download
    git clone \
        https://github.com/MikkelSchubert/adapterremoval.git \
        /adapterremoval
    (
    cd /adapterremoval || exit 1
    git checkout -f v2.3.1
    git submodule update --init --recursive
    make
    make install
    )

    rm -r /adapterremoval

%runscript
    exec /usr/local/bin/AdapterRemoval "$@"
```

## Collection

 - Name: [TomHarrop/seq-utils](https://github.com/TomHarrop/seq-utils)
 - License: None

