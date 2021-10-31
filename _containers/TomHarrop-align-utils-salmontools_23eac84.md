---
id: 13093
name: "TomHarrop/align-utils"
branch: "master"
tag: "salmontools_23eac84"
commit: "2b5b9827d1e469b5468ec0a10d67474a9817dea2"
version: "485bd81250128259665ee3c198954204d3a4318d0499dd1090034c692b9aca9e"
build_date: "2020-09-29T22:01:57.926Z"
size_mb: 290.92578125
size: 305057792
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/salmontools_23eac84/2020-09-29-2b5b9827-485bd812/485bd81250128259665ee3c198954204d3a4318d0499dd1090034c692b9aca9e.sif"
url: https://datasets.datalad.org/shub/TomHarrop/align-utils/salmontools_23eac84/2020-09-29-2b5b9827-485bd812/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/salmontools_23eac84/2020-09-29-2b5b9827-485bd812/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:salmontools_23eac84

```bash
$ singularity pull shub://TomHarrop/align-utils:salmontools_23eac84
```

## Singularity Recipe

```singularity
Bootstrap: library
From: ubuntu:20.04

%help

    Salmon 0.14.1
    https://github.com/COMBINE-lab/salmon/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "salmon 0.14.1"

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

    apt-get update
    apt-get install -y \
        build-essential \
        bedtools \
        cmake \
        curl \
        git \
        language-pack-en \
        wget \
        zlib1g-dev

    # install mashmap
    wget -O "mashmap.tar.gz" \
        --no-check-certificate \
        https://github.com/marbl/MashMap/releases/download/v2.0/mashmap-Linux64-v2.0.tar.gz
    mkdir mashmap
    tar -zxf mashmap.tar.gz \
        -C mashmap \
        --strip-components 1
    cp mashmap/mashmap /usr/local/bin/

    # build salmontools
    git clone https://github.com/COMBINE-lab/SalmonTools
    cd SalmonTools || exit 1
    git checkout 23eac84
    chmod -R 755 scripts
    mkdir build
    cd build || exit 1
    cmake ..
    make
    make install

%environment
    export PATH="${PATH}:/SalmonTools/scripts"

%runscript
    exec /usr/local/bin/salmontools "$@"
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

