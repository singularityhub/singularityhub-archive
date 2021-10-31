---
id: 12777
name: "TomHarrop/align-utils"
branch: "master"
tag: "samtools_3389c09_htslib_42825b7"
commit: "9358daee1f219360f2060bf8a7693c22476ccc9c"
version: "e0bc15dc192ec3c806c99376689d74afc73b2f62fda68b988ea3641aa5055df4"
build_date: "2020-05-12T04:23:50.305Z"
size_mb: 147.2421875
size: 154394624
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_3389c09_htslib_42825b7/2020-05-12-9358daee-e0bc15dc/e0bc15dc192ec3c806c99376689d74afc73b2f62fda68b988ea3641aa5055df4.sif"
url: https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_3389c09_htslib_42825b7/2020-05-12-9358daee-e0bc15dc/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/samtools_3389c09_htslib_42825b7/2020-05-12-9358daee-e0bc15dc/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:samtools_3389c09_htslib_42825b7

```bash
$ singularity pull shub://TomHarrop/align-utils:samtools_3389c09_htslib_42825b7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help

    samtools 3389c09
    bcftools 034b466
    htslib 42825b7
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
    # git checkout -f 2e36fa6
    git fetch origin pull/1059/head:informative_vcf_errors
    git checkout -f informative_vcf_errors
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
    git checkout -f 034b466
    git submodule update --init --recursive
    make
    make install

    # tidy up
    rm -rf /htslib /samtools /bcftools
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

