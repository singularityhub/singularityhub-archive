---
id: 11427
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minknow_19.10.1"
commit: "eb197fd3557f58da373046c59dcfb6f2920b06ef"
version: "5760ace66714eae89826ff5dcc983c365f4bf14df154e7fe2e860d5119ac0ba3"
build_date: "2019-10-30T00:48:21.253Z"
size_mb: 611.4140625
size: 641114112
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_19.10.1/2019-10-30-eb197fd3-5760ace6/5760ace66714eae89826ff5dcc983c365f4bf14df154e7fe2e860d5119ac0ba3.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_19.10.1/2019-10-30-eb197fd3-5760ace6/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_19.10.1/2019-10-30-eb197fd3-5760ace6/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minknow_19.10.1

```bash
$ singularity pull shub://TomHarrop/ont-containers:minknow_19.10.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    ONT MinKNOW 19.10.1-1 GUI in a container

    Run as follows:

    singularity instance start \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_19.10.1.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 19.10.1-1"

%post
    # faster apt downloads, will it break?
    export DEBIAN_FRONTEND=noninteractive
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
    apt install -y minknow-nc=19.10.1-1~bionic

%startscript
    /opt/ONT/MinKNOW/bin/mk_manager_svc &
    nohup /opt/ui/MinKNOW > /dev/null 2>&1 < /dev/null &
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

