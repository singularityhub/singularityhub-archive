---
id: 12740
name: "TomHarrop/align-utils"
branch: "master"
tag: "samtools_3389c09"
commit: "c874bc83c7148d34cb602932c67548d843540d4b"
version: "370eb531d983aa59704e25c4fa91873e755319b4c2ea6e7e908dfb39f5beb4d4"
build_date: "2020-04-22T20:13:54.970Z"
size_mb: 147.7109375
size: 154886144
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_3389c09/2020-04-22-c874bc83-370eb531/370eb531d983aa59704e25c4fa91873e755319b4c2ea6e7e908dfb39f5beb4d4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/samtools_3389c09/2020-04-22-c874bc83-370eb531/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_3389c09/2020-04-22-c874bc83-370eb531/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:samtools_3389c09

```bash
$ singularity pull shub://TomHarrop/align-utils:samtools_3389c09
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help

    samtools 3389c09
    bcftools d6d1ca6
    htslib 2e36fa6
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
    git checkout -f 2e36fa6
    git submodule update --init --recursive
    make
    make install

    git clone \
        https://github.com/samtools/samtools.git \
        /samtools
    cd /samtools || exit 1
    git checkout -f 3389c09
    git submodule update --init --recursive
    make
    make install

    git clone \
        https://github.com/samtools/bcftools.git \
        /bcftools
    cd /bcftools || exit 1
    git checkout -f d6d1ca6
    git submodule update --init --recursive
    make
    make install

    # tidy up
    rm -rf /htslib /samtools /bcftools
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

