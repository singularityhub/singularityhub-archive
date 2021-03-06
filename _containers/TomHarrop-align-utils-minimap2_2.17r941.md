---
id: 13996
name: "TomHarrop/align-utils"
branch: "master"
tag: "minimap2_2.17r941"
commit: "bcdabdc8d135f58d8d04baee8f3deca1045c69d6"
version: "819f2451236e17210cfb23c9289bfdc8751562ba88f4c46eca0a6b68709ae977"
build_date: "2020-12-17T22:19:31.066Z"
size_mb: 113.06640625
size: 118558720
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/minimap2_2.17r941/2020-12-17-bcdabdc8-819f2451/819f2451236e17210cfb23c9289bfdc8751562ba88f4c46eca0a6b68709ae977.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/minimap2_2.17r941/2020-12-17-bcdabdc8-819f2451/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/minimap2_2.17r941/2020-12-17-bcdabdc8-819f2451/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:minimap2_2.17r941

```bash
$ singularity pull shub://TomHarrop/align-utils:minimap2_2.17r941
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    minimap2 2.17 (r941)
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "minimap2 2.17 (r941)"

%environment
    export LC_ALL=C
    
%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    # reset apt
    apt-get clean
    rm -r /var/lib/apt/lists/*
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

    apt-get update
    apt-get upgrade -y --fix-missing

    # install dependencies
    apt-get install -y \
        build-essential wget zlib1g-dev

    # install k8
    wget -O "/k8.tar.gz" \
        --no-check-certificate \
        https://github.com/attractivechaos/k8/releases/download/0.2.5/k8-0.2.5.tar.bz2
    mkdir /k8
    tar -xjf /k8.tar.gz \
        -C /k8 \
        --strip-components 1
    mv /k8/k8-Linux /usr/local/bin/k8
    rm -r /k8 /k8.tar.gz

    # install minimap2
    wget -O "minimap2.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/minimap2/archive/v2.17.tar.gz
    mkdir minimap2
    tar -zxf minimap2.tar.gz \
        -C minimap2 \
        --strip-components 1

    cd minimap2 || exit 1
    make
    mv minimap2 /usr/local/bin/
    mv misc/paftools.js /usr/local/bin/

    cd .. || exit 1
    rm -rf minimap2 minimap2.tar.gz

%runscript
    exec /usr/local/bin/minimap2 "$@"
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

