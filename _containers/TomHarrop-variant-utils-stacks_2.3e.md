---
id: 12499
name: "TomHarrop/variant-utils"
branch: "master"
tag: "stacks_2.3e"
commit: "f86d9f8611d4657d553d4b265c18cb33c50c136d"
version: "968b1affdadacdc125901940eca252f683d4cfb1fa5f66859f0e4156c7cb5af4"
build_date: "2020-03-11T23:20:26.878Z"
size_mb: 196.140625
size: 205668352
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.3e/2020-03-11-f86d9f86-968b1aff/968b1affdadacdc125901940eca252f683d4cfb1fa5f66859f0e4156c7cb5af4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/stacks_2.3e/2020-03-11-f86d9f86-968b1aff/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.3e/2020-03-11-f86d9f86-968b1aff/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:stacks_2.3e

```bash
$ singularity pull shub://TomHarrop/variant-utils:stacks_2.3e
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.04

%help

    Container for stacks 2.3e
    http://catchenlab.life.illinois.edu/stacks

%labels

    MAINTAINER "Tom Harrop"
    VERSION "stacks 2.3e"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

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
    apt update
    apt install -y \
        build-essential \
        python3 \
        samtools \
        wget \
        zlib1g-dev 

    # set up python
    update-alternatives \
        --install /usr/bin/python \
        python \
        /usr/bin/python3 \
        1

    # download stacks
    wget -O "stacks.tar.gz" \
        http://catchenlab.life.illinois.edu/stacks/source/stacks-2.3e.tar.gz
    mkdir /stacks-install
    tar -zxf stacks.tar.gz \
        -C /stacks-install \
        --strip-components 1
    rm stacks.tar.gz

    (
    cd /stacks-install || exit 1
    # fix the tab-matching error in stacks-integrate-alignments
    sed -i \
        's/grep -oE/grep -oP/g' \
        scripts/stacks-integrate-alignments
    # install
    ./configure \
    && make \
    && make install
    )
    rm -rf /stacks-install

%environment
    export LC_ALL=C

%runscript
    exec perl /usr/local/bin/denovo_map.pl "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

