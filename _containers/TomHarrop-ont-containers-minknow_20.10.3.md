---
id: 14980
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minknow_20.10.3"
commit: "f462361c1d75a84ef28ccdb42ca1569f13dd18ab"
version: "38244e8b9d28462bde1f3509dcc9d50994c462df3dff00164b8f460071896d46"
build_date: "2020-11-27T03:24:10.196Z"
size_mb: 941.93359375
size: 987688960
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.10.3/2020-11-27-f462361c-38244e8b/38244e8b9d28462bde1f3509dcc9d50994c462df3dff00164b8f460071896d46.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/minknow_20.10.3/2020-11-27-f462361c-38244e8b/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.10.3/2020-11-27-f462361c-38244e8b/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minknow_20.10.3

```bash
$ singularity pull shub://TomHarrop/ont-containers:minknow_20.10.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    ONT MinKNOW 20.10.3 GUI in a container

    Run as follows:

    singularity instance start \
        --nv \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_20.10.3.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 20.10.3"

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
        software-properties-common \
        wget

    # install ONT repo
    export PLATFORM=$(lsb_release -cs) 
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add - 
    echo \
        "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list 
    apt-get update


    apt update
    apt install -y minion-nc=20.10.3-1~bionic

%startscript
    /opt/ont/minknow/bin/mk_manager_svc & /opt/ont/ui/kingfisher/MinKNOW
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

