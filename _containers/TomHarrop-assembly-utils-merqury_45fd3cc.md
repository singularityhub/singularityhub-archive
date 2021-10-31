---
id: 12548
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "merqury_45fd3cc"
commit: "febe3aa52b78b7d6accf0561cc1183ebbf90a611"
version: "10afc6e7d8d127e8ea9d8f72d0303307074b099ad92b8c7b78a133de74a5fe65"
build_date: "2021-01-19T17:06:10.147Z"
size_mb: 534.5703125
size: 560537600
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/merqury_45fd3cc/2021-01-19-febe3aa5-10afc6e7/10afc6e7d8d127e8ea9d8f72d0303307074b099ad92b8c7b78a133de74a5fe65.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/merqury_45fd3cc/2021-01-19-febe3aa5-10afc6e7/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/merqury_45fd3cc/2021-01-19-febe3aa5-10afc6e7/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:merqury_45fd3cc

```bash
$ singularity pull shub://TomHarrop/assembly-utils:merqury_45fd3cc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Container for merqury 45fd3cc
    https://github.com/marbl/merqury

%labels
    MAINTAINER "Tom Harrop"
    VERSION "merqury 45fd3cc"

%environment
    export LC_ALL=C
    export PATH="${PATH}:/meryl/Linux-amd64/bin:/IGV_2.8.0:/merqury"
    export MERQURY="/merqury"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    export PATH="${PATH}:/meryl/Linux-amd64/bin:/IGV_2.8.0:/merqury"
    export MERQURY="/merqury"

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
        bedtools \
        build-essential \
        default-jre \
        git \
        r-cran-ggplot2 \
        r-cran-scales \
        samtools \
        wget

    # install meryl
    git clone https://github.com/marbl/meryl.git /meryl
    cd /meryl || exit 1
    git checkout -f v1.0
    git submodule update --init --recursive
    cd /meryl/src || exit 1
    make

    # install igvtools
    wget -O /IGV.zip \
        --no-check-certificate \
        https://data.broadinstitute.org/igv/projects/downloads/2.8/IGV_2.8.0.zip
    unzip /IGV.zip
    rm /IGV.zip

    # install merqury
    git clone https://github.com/marbl/merqury.git /merqury
    cd /merqury || exit 1
    git checkout -f 45fd3cc
    git submodule update --init --recursive
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

