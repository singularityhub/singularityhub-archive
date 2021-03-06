---
id: 14677
name: "TomHarrop/ont-containers"
branch: "master"
tag: "readfish_77c11e2"
commit: "80ce1888021d0175cbc4852fdf8dd74e6cba2347"
version: "bdbc5170eee08813fd9ce1b37bd070b06d922a5f4ddacb79ed725104de74fb16"
build_date: "2020-10-26T21:22:02.325Z"
size_mb: 1475.7734375
size: 1547460608
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/readfish_77c11e2/2020-10-26-80ce1888-bdbc5170/bdbc5170eee08813fd9ce1b37bd070b06d922a5f4ddacb79ed725104de74fb16.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/readfish_77c11e2/2020-10-26-80ce1888-bdbc5170/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/readfish_77c11e2/2020-10-26-80ce1888-bdbc5170/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:readfish_77c11e2

```bash
$ singularity pull shub://TomHarrop/ont-containers:readfish_77c11e2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    readfish 77c11e2 from github
    MinKNOW (minion-nc) 20.06.5-1~bionic
    Guppy (ont-guppy) 4.2.2-1~bionic

%labels
    MAINTAINER "Tom Harrop"
    VERSION "readfish 77c11e2"

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
    # (needs pip)
    apt update
    apt install -y \
        apt-transport-https \
        build-essential \
        git \
        libasound2 \
        libcanberra-gtk-module \
        libcanberra-gtk3-module \
        libgconf-2-4 \
        libgtk-3-dev \
        libnss3 \
        libxss1 \
        lsb-release \
        nvidia-modprobe \
        python3-pip \
        python3.7 \
        python3.7-dev \
        software-properties-common \
        wget \
        zlib1g-dev

    # install minimap2
    wget -O "/minimap2.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/minimap2/archive/v2.17.tar.gz
    mkdir /minimap2
    tar -zxf /minimap2.tar.gz \
        -C /minimap2 \
        --strip-components 1

    (
        cd /minimap2 || exit 1
        make
        mv minimap2 /usr/local/bin/
    )

    rm -rf /minimap2 /minimap2.tar.gz

    # install minknow and guppy
    wget \
        -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add -
    echo "deb http://mirror.oxfordnanoportal.com/apt bionic-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list

    apt-get update
    apt-get install -y \
        --no-install-recommends \
        minion-nc=20.06.5-1~bionic \
        ont-guppy=4.2.2-1~bionic

    # setup python and install readfish
    /usr/bin/python3.7 -m pip install --upgrade \
        pip \
        setuptools \
        wheel
    /usr/bin/python3.7 -m pip install \
        git+https://github.com/nanoporetech/read_until_api@v3.0.0

    # install readfish from wheel on pypi
    # this is a bit of a hack but it's set to python==3.7 
    # so it won't install on 3.7.5 (maybe a mistake?)
    # /usr/bin/python3.7 -m pip install \
    #     --ignore-requires-python \
    #     readfish==0.0.5a3

    # install readfish from github
    /usr/bin/python3.7 -m pip install \
        git+https://github.com/LooseLab/readfish@77c11e2

    # fix missing dep
    /usr/bin/python3.7 -m pip install \
        ont_pyguppy_client_lib

%runscript
    exec /usr/local/bin/readfish "@$"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

