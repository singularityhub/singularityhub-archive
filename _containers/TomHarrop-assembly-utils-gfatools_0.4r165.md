---
id: 13657
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "gfatools_0.4r165"
commit: "3b5f3b78a530b023c4f0d62a0e272e81842f861c"
version: "e841ed8a3030214c9f7682f383e4e2aef047ae0b6aae887c47e79e72231af705"
build_date: "2020-09-29T02:54:33.039Z"
size_mb: 110.76953125
size: 116150272
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/gfatools_0.4r165/2020-09-29-3b5f3b78-e841ed8a/e841ed8a3030214c9f7682f383e4e2aef047ae0b6aae887c47e79e72231af705.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assembly-utils/gfatools_0.4r165/2020-09-29-3b5f3b78-e841ed8a/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/gfatools_0.4r165/2020-09-29-3b5f3b78-e841ed8a/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:gfatools_0.4r165

```bash
$ singularity pull shub://TomHarrop/assembly-utils:gfatools_0.4r165
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    gfatools 0.4 (r165)
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "gfatools 0.4 (r165)"

%environment
    export LC_ALL=C

%post
    # faster apt downloads
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

    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential wget zlib1g-dev

    # install minimap2
    wget -O "gfatools.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/gfatools/archive/v0.4.tar.gz
    mkdir gfatools
    tar -zxf gfatools.tar.gz \
        -C gfatools \
        --strip-components 1

    cd gfatools || exit 1
    make
    mv gfatools /usr/local/bin/

    cd .. || exit 1
    rm -rf gfatools gfatools.tar.gz

%runscript
    exec /usr/local/bin/gfatools "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

