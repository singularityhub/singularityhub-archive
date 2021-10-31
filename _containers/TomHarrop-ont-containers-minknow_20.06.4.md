---
id: 13931
name: "TomHarrop/ont-containers"
branch: "master"
tag: "minknow_20.06.4"
commit: "7bf57979d724a9d434835bd3e81ecf2cb5eccb22"
version: "288c55cb52eb1f1d37376ec2c53ab625e6cd213888ef4b6d0f7ef1ce64e714c8"
build_date: "2020-10-14T22:31:52.913Z"
size_mb: 945.88671875
size: 991834112
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.06.4/2020-10-14-7bf57979-288c55cb/288c55cb52eb1f1d37376ec2c53ab625e6cd213888ef4b6d0f7ef1ce64e714c8.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.06.4/2020-10-14-7bf57979-288c55cb/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/minknow_20.06.4/2020-10-14-7bf57979-288c55cb/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:minknow_20.06.4

```bash
$ singularity pull shub://TomHarrop/ont-containers:minknow_20.06.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    ONT MinKNOW 20.06.4 GUI in a container

    Run as follows:

    singularity instance start \
        -B output/dir/run:/run,output/dir/var:/var \
        minknow_20.06.4.sif \
        minknow

%labels
    MAINTAINER "Tom Harrop"
    VERSION "MinKNOW 20.06.4"

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
    apt install -y minknow-nc=20.06.4-1~bionic

%startscript
    /opt/ont/minknow/bin/mk_manager_svc & /opt/ont/ui/kingfisher/MinKNOW
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

