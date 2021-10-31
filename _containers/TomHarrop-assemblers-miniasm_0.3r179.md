---
id: 13622
name: "TomHarrop/assemblers"
branch: "master"
tag: "miniasm_0.3r179"
commit: "38e1bf3e2c9ab2ff5e01b6ba819bfb75d38912d3"
version: "06fb8b88f65e44724f75c98f639c08feee8e4dca1b3515c387427c3504794e24"
build_date: "2021-03-11T22:28:21.991Z"
size_mb: 110.97265625
size: 116363264
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/miniasm_0.3r179/2021-03-11-38e1bf3e-06fb8b88/06fb8b88f65e44724f75c98f639c08feee8e4dca1b3515c387427c3504794e24.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assemblers/miniasm_0.3r179/2021-03-11-38e1bf3e-06fb8b88/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/miniasm_0.3r179/2021-03-11-38e1bf3e-06fb8b88/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:miniasm_0.3r179

```bash
$ singularity pull shub://TomHarrop/assemblers:miniasm_0.3r179
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    miniasm 0.3 (r179)
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "miniasm 0.3 (r179)"

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
    wget -O "miniasm.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/miniasm/archive/v0.3.tar.gz
    mkdir miniasm
    tar -zxf miniasm.tar.gz \
        -C miniasm \
        --strip-components 1

    cd miniasm || exit 1
    make
    mv miniasm /usr/local/bin/

    cd .. || exit 1
    rm -rf miniasm miniasm.tar.gz

%runscript
    exec /usr/local/bin/miniasm "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

