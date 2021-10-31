---
id: 13965
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "circos_0.69-9"
commit: "82aca4651f3f159f1d39e3f60f09cdac9fbd79bd"
version: "f53a6033cd04780615dc9554c09a02bc2c96c23aed6c01e2803a7bcbbabf41f1"
build_date: "2020-08-18T00:07:16.582Z"
size_mb: 144.24609375
size: 151252992
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/circos_0.69-9/2020-08-18-82aca465-f53a6033/f53a6033cd04780615dc9554c09a02bc2c96c23aed6c01e2803a7bcbbabf41f1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assembly-utils/circos_0.69-9/2020-08-18-82aca465-f53a6033/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/circos_0.69-9/2020-08-18-82aca465-f53a6033/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:circos_0.69-9

```bash
$ singularity pull shub://TomHarrop/assembly-utils:circos_0.69-9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    Circos 0.69-9
    http://circos.ca/software/download/circos/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Circos 0.69-9"

%environment
    export PATH="${PATH}:/circos/bin"
    export LC_ALL=C

%runscript
    exec /circos/bin/circos "$@"

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

    # dependencies
    apt-get install -y \
        build-essential \
        libclone-perl \
        libconfig-general-perl \
        libfont-ttf-perl \
        libgd-perl \
        liblist-moreutils-perl \
        libmath-bezier-perl \
        libmath-round-perl \
        libmath-vecstat-perl \
        libparams-validate-perl \
        libreadonly-perl \
        libregexp-common-perl \
        libset-intspan-perl \
        libstatistics-basic-perl \
        libsvg-perl \
        libtext-format-perl \
        perl \
        wget 

    # circos
    wget -O "/circos.tar.gz" \
        --no-check-certificate \
        http://circos.ca/distribution/circos-0.69-9.tgz
    mkdir /circos
    tar -zxf /circos.tar.gz \
        -C /circos \
        --strip-components 1
    rm /circos.tar.gz
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

