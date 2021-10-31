---
id: 12736
name: "TomHarrop/align-utils"
branch: "master"
tag: "samtools_1.9"
commit: "d995c6f2a0d95ccf62e72f4426fda4eb152c5fdc"
version: "39ef1ed9ddff9ef668780def9ebbe0436219d45b285a9be9743fc2013e17eeed"
build_date: "2020-05-28T22:50:13.668Z"
size_mb: 144.9453125
size: 151986176
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_1.9/2020-05-28-d995c6f2-39ef1ed9/39ef1ed9ddff9ef668780def9ebbe0436219d45b285a9be9743fc2013e17eeed.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/samtools_1.9/2020-05-28-d995c6f2-39ef1ed9/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_1.9/2020-05-28-d995c6f2-39ef1ed9/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:samtools_1.9

```bash
$ singularity pull shub://TomHarrop/align-utils:samtools_1.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help

    samtools 1.9
    bcflib 1.9
    htslib 1.9
    http://www.htslib.org/

%labels

    VERSION "samtools 1.9"

%runscript
    exec /usr/local/bin/samtools "$@"

%environment
    export LC_ALL=C

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
        libcurl4-openssl-dev \
        liblzma-dev \
        libncurses-dev \
        wget \
        zlib1g-dev

    # install releases via github
    git clone \
        https://github.com/samtools/htslib.git \
        /htslib
    cd /htslib || exit 1
    git checkout -f  1.9
    git submodule update --init --recursive
    make
    make install

    git clone \
        https://github.com/samtools/samtools.git \
        /samtools
    cd /samtools || exit 1
    git checkout -f  1.9
    git submodule update --init --recursive
    make
    make install

    git clone \
        https://github.com/samtools/bcftools.git \
        /bcftools
    cd /bcftools || exit 1
    git checkout -f  1.9
    git submodule update --init --recursive
    make
    make install

    # tidy up
    rm -rf /htslib /samtools /bcftools
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

