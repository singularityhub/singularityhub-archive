---
id: 13495
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minknow_19.12.5"
commit: "827051a1e37d196c81d49d142073e252044005fc"
version: "b956ae28fc03f55ba4157e80c4e53cfe3196eea8d4b116c63b1cf96e7a58e998"
build_date: "2020-10-20T02:17:49.395Z"
size_mb: 723.7734375
size: 758931456
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_19.12.5/2020-10-20-827051a1-b956ae28/b956ae28fc03f55ba4157e80c4e53cfe3196eea8d4b116c63b1cf96e7a58e998.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_19.12.5/2020-10-20-827051a1-b956ae28/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_19.12.5/2020-10-20-827051a1-b956ae28/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minknow_19.12.5

```bash
$ singularity pull shub://TomHarrop/ont-containers:minknow_19.12.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    ONT MinKNOW 19.12.5 GUI in a container

    Run as follows:

    singularity instance start \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_19.10.1.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 19.12.5"

%post
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

    # install dependencies
    apt update
    apt install -y \
        apt-transport-https \
        libasound2 \
        libcanberra-gtk-module \
        libgconf-2-4 \
        libgtk-3-dev \
        libnss3 \
        libxss1 \
        wget

    # install minknow
    wget \
        -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add -
    echo "deb http://mirror.oxfordnanoportal.com/apt bionic-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list
    apt update
    apt install -y minknow-nc=19.12.5-1~bionic

%startscript
    /opt/ont/minknow/bin/mk_manager_svc &
    nohup /opt/ont/minknow-ui/MinKNOW > /dev/null 2>&1 < /dev/null &
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

