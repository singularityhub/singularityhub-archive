---
id: 13472
name: "TomHarrop/assemblers"
branch: "master"
tag: "spades_3.14.1"
commit: "80ba97c68ac5bc276d1adb011712dfe367acc6ab"
version: "9230ca941a8ee6fbaad5dab4e16c68de390b479b431cc5668a62f55bb0b9eeac"
build_date: "2020-08-16T22:25:06.457Z"
size_mb: 162.49609375
size: 170389504
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/spades_3.14.1/2020-08-16-80ba97c6-9230ca94/9230ca941a8ee6fbaad5dab4e16c68de390b479b431cc5668a62f55bb0b9eeac.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assemblers/spades_3.14.1/2020-08-16-80ba97c6-9230ca94/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/spades_3.14.1/2020-08-16-80ba97c6-9230ca94/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:spades_3.14.1

```bash
$ singularity pull shub://TomHarrop/assemblers:spades_3.14.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
    Spades 3.14.1
    http://cab.spbu.ru/software/spades/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Spades 3.14.1"

%environment
    export LC_ALL=C

%post
    # variable
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive

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
        build-essential \
        cmake \
        libbz2-dev \
        python \
        wget \
        zlib1g-dev
        
    # install Spades
    wget -O "spades.tar.gz" \
        --no-check-certificate \
        http://cab.spbu.ru/files/release3.14.1/SPAdes-3.14.1.tar.gz
    mkdir spades
    tar -zxf spades.tar.gz \
        -C spades \
        --strip-components 1
    cd spades || exit 1
    PREFIX=/usr/local ./spades_compile.sh
    cd .. || exit 1
    rm -rf spades spades.tar.gz

%runscript

    exec /usr/local/bin/spades.py "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

