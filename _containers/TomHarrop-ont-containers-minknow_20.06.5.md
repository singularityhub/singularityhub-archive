---
id: 14623
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minknow_20.06.5"
commit: "430a4f7cc77719d2369137e1a98996385e1f634f"
version: "9e96e2c7f96e8cd8f8b271a349c456829be8245a38ba32e06510b2a5268dafb3"
build_date: "2020-11-18T22:58:27.477Z"
size_mb: 948.8515625
size: 994942976
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.06.5/2020-11-18-430a4f7c-9e96e2c7/9e96e2c7f96e8cd8f8b271a349c456829be8245a38ba32e06510b2a5268dafb3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/minknow_20.06.5/2020-11-18-430a4f7c-9e96e2c7/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.06.5/2020-11-18-430a4f7c-9e96e2c7/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minknow_20.06.5

```bash
$ singularity pull shub://TomHarrop/ont-containers:minknow_20.06.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    ONT MinKNOW 20.06.5 GUI in a container

    Run as follows:

    singularity instance start \
        --nv \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_20.06.5.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 20.06.5"

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
        libcanberra-gtk3-module \
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
    apt install -y minion-nc=20.06.5-1~bionic

%startscript
    /opt/ont/minknow/bin/mk_manager_svc & /opt/ont/ui/kingfisher/MinKNOW
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

