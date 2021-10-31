---
id: 11961
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "racon_1.4.10"
commit: "14e0c6686dcca20c6e4520051ac0da218a666ad0"
version: "0dafde90a2af52a94860ff9c001267ac92b71f9b6adf09fe331f7040c4aa4092"
build_date: "2020-01-08T02:11:02.729Z"
size_mb: 1938.73828125
size: 2032914432
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/racon_1.4.10/2020-01-08-14e0c668-0dafde90/0dafde90a2af52a94860ff9c001267ac92b71f9b6adf09fe331f7040c4aa4092.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/racon_1.4.10/2020-01-08-14e0c668-0dafde90/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/racon_1.4.10/2020-01-08-14e0c668-0dafde90/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:racon_1.4.10

```bash
$ singularity pull shub://TomHarrop/assembly-utils:racon_1.4.10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.04

%help
    Racon v1.4.10
    https://github.com/isovic/racon

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Racon v1.4.10"

%environment
    export PATH="${PATH}:/racon/build/bin"
    export LC_ALL=C

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    # faster apt downloads
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
        apt-transport-https \
        build-essential \
        cmake \
        git \
        lsb-release \
        nvidia-modprobe \
        python \
        software-properties-common \
        wget

    # nvidia libraries
    add-apt-repository -y ppa:graphics-drivers/ppa
    apt-get update
    apt-get upgrade -y
    apt-get install -y \
        nvidia-cuda-toolkit 

    # download master
    git clone \
        https://github.com/lbcb-sci/racon.git \
        /racon
    cd /racon || exit 1
    git checkout 1.4.10
    git submodule update --init --recursive || true     # have to allow fail

    # build with cuda support
    # for older versions of CUDA
    # -DCMAKE_C_COMPILER=/usr/bin/gcc-6 \
    mkdir build && cd build || exit 1
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -Dracon_build_tests=ON \
        -Dracon_build_wrapper=ON \
        -D CUDA_TOOLKIT_ROOT_DIR=/usr/lib/cuda \
        -Dracon_enable_cuda=ON \
        ..
    make

%runscript
    exec /racon/build/bin/racon "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

