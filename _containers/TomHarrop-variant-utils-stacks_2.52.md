---
id: 12543
name: "TomHarrop/variant-utils"
branch: "master"
tag: "stacks_2.52"
commit: "0a8bea9daf23f496edf7e69619d0a10cbc0aa328"
version: "a932c9aa4f1ee9274277301665e7fa3c9f9c623c32fc6eab68ab80f617e6cc6b"
build_date: "2021-03-04T00:10:18.718Z"
size_mb: 216.0625
size: 226557952
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.52/2021-03-04-0a8bea9d-a932c9aa/a932c9aa4f1ee9274277301665e7fa3c9f9c623c32fc6eab68ab80f617e6cc6b.sif"
url: https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.52/2021-03-04-0a8bea9d-a932c9aa/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/stacks_2.52/2021-03-04-0a8bea9d-a932c9aa/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:stacks_2.52

```bash
$ singularity pull shub://TomHarrop/variant-utils:stacks_2.52
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help

    Container for stacks 2.52
    http://catchenlab.life.illinois.edu/stacks

%labels

    MAINTAINER "Tom Harrop"
    VERSION "stacks 2.52"

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
        http://catchenlab.life.illinois.edu/stacks/source/stacks-2.52.tar.gz
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

