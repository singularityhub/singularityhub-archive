---
id: 12741
name: "TomHarrop/variant-utils"
branch: "master"
tag: "stacks_2.53"
commit: "8db1d9fc7b03e546d78bced3d4a45521b61086df"
version: "b84c259bbd7bb1879235700fef44f31e5640282cd9ad5f56309a6879c05115e8"
build_date: "2020-04-20T01:04:53.788Z"
size_mb: 216.65234375
size: 227176448
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.53/2020-04-20-8db1d9fc-b84c259b/b84c259bbd7bb1879235700fef44f31e5640282cd9ad5f56309a6879c05115e8.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/stacks_2.53/2020-04-20-8db1d9fc-b84c259b/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.53/2020-04-20-8db1d9fc-b84c259b/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:stacks_2.53

```bash
$ singularity pull shub://TomHarrop/variant-utils:stacks_2.53
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help

    Container for stacks 2.53
    http://catchenlab.life.illinois.edu/stacks

%labels

    MAINTAINER "Tom Harrop"
    VERSION "stacks 2.53"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    # set up apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
    apt-get update
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
    wget -O "/stacks.tar.gz" \
        http://catchenlab.life.illinois.edu/stacks/source/stacks-2.53.tar.gz
    mkdir /stacks-install
    tar -zxf /stacks.tar.gz \
        -C /stacks-install \
        --strip-components 1
    rm /stacks.tar.gz

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

