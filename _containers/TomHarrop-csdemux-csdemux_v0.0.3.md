---
id: 13883
name: "TomHarrop/csdemux"
branch: "master"
tag: "csdemux_v0.0.3"
commit: "58d3d77971a7126ab55351f9c5b8397f5d8d6209"
version: "d0e2ef2a17c46b29b053849e1716bd288fdc472201ecd3da86dc7eb38e2f5f2d"
build_date: "2020-08-06T23:19:07.452Z"
size_mb: 1380.140625
size: 1447182336
sif: "https://datasets.datalad.org/shub/TomHarrop/csdemux/csdemux_v0.0.3/2020-08-06-58d3d779-d0e2ef2a/d0e2ef2a17c46b29b053849e1716bd288fdc472201ecd3da86dc7eb38e2f5f2d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/csdemux/csdemux_v0.0.3/2020-08-06-58d3d779-d0e2ef2a/
recipe: https://datasets.datalad.org/shub/TomHarrop/csdemux/csdemux_v0.0.3/2020-08-06-58d3d779-d0e2ef2a/Singularity
collection: TomHarrop/csdemux
---

# TomHarrop/csdemux:csdemux_v0.0.3

```bash
$ singularity pull shub://TomHarrop/csdemux:csdemux_v0.0.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/bioconductor_docker:bioc2020.1

%help
    Container for csdemux v0.0.3
    https://github.com/tomharrop/csdemux

    bbmap 38.73
    python 3.7.5
    R 4.0.0 with data.table 1.13.0 and ggplot2 3.3.2
    
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
        python3.7-venv \
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
        git+git://github.com/tomharrop/csdemux.git@v0.0.3
```

## Collection

 - Name: [TomHarrop/csdemux](https://github.com/TomHarrop/csdemux)
 - License: None

