---
id: 13820
name: "TomHarrop/csdemux"
branch: "master"
tag: "csdemux_v0.0.2"
commit: "92ed0a5d88f7bbd65523727881d2fcffaa8b84a3"
version: "518993f1b6b705ff92bcb152fb4f7a078b14a0717031963757578a1b330a8c77"
build_date: "2020-08-02T20:52:26.397Z"
size_mb: 1380.078125
size: 1447116800
sif: "https://datasets.datalad.org/shub/TomHarrop/csdemux/csdemux_v0.0.2/2020-08-02-92ed0a5d-518993f1/518993f1b6b705ff92bcb152fb4f7a078b14a0717031963757578a1b330a8c77.sif"
url: https://datasets.datalad.org/shub/TomHarrop/csdemux/csdemux_v0.0.2/2020-08-02-92ed0a5d-518993f1/
recipe: https://datasets.datalad.org/shub/TomHarrop/csdemux/csdemux_v0.0.2/2020-08-02-92ed0a5d-518993f1/Singularity
collection: TomHarrop/csdemux
---

# TomHarrop/csdemux:csdemux_v0.0.2

```bash
$ singularity pull shub://TomHarrop/csdemux:csdemux_v0.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/bioconductor_docker:bioc2020.1

%help
    Container for csdemux v0.0.2
    https://github.com/tomharrop/csdemux

    bbmap 38.73
    python 3.7.5
    R 3.6.1 with data.table 1.12.6 and ggplot2 3.2.1

%labels
    MAINTAINER "Tom Harrop"

%runscript
    exec /usr/local/bin/csdemux "$@"

%environment
    export LC_ALL=C

%post
    export DEBIAN_FRONTEND=noninteractive
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
deb-src mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # packages
    apt-get update
    apt-get install -y \
        --no-install-recommends \
        build-essential \
        default-jre-headless \
        git \
        libpython3.7-dev \
        pigz \
        python3-pip \
        python3.7 \
        python3.7-dev \
        wget

    # re-build R packages
    Rscript -e "options(Ncpus=8); \
        BiocManager::install(c( \
            'bit64', \
            'Cairo', \
            'data.table', \
            'future.apply', \
            'ggplot2', \
            'scales', \
            'viridis' \
        ))"

    # bbmap
    wget -O "bbmap.tar.gz" \
        https://sourceforge.net/projects/bbmap/files/BBMap_38.73.tar.gz
    mkdir bbmap
    tar -zxf bbmap.tar.gz \
        -C bbmap \
        --strip-components 1
    cp -r bbmap/resources/* /
    cp -r bbmap/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap

    # install pipeline package
    # have to install python3.7 via apt and then upgrade pip, because
    # bioconductor is using ubuntu18.04 which ships with python3.6
    /usr/bin/python3.7 -m pip \
        install --upgrade pip
    /usr/bin/python3.7 -m pip \
        install --upgrade setuptools wheel
    /usr/bin/python3.7 -m pip \
        install \
        git+git://github.com/tomharrop/csdemux.git@v0.0.2
```

## Collection

 - Name: [TomHarrop/csdemux](https://github.com/TomHarrop/csdemux)
 - License: None

