---
id: 3386
name: "ozanarkancan/r2r-navi"
branch: "master"
tag: "latest"
commit: "1c6befe4fb54f827d757678fbd42e4f2ccb23e5e"
version: "3d532c3b03c2ea6e4e3ad481526a957a"
build_date: "2020-05-03T18:13:35.346Z"
size_mb: 4002.0
size: 2086826015
sif: "https://datasets.datalad.org/shub/ozanarkancan/r2r-navi/latest/2020-05-03-1c6befe4-3d532c3b/3d532c3b03c2ea6e4e3ad481526a957a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ozanarkancan/r2r-navi/latest/2020-05-03-1c6befe4-3d532c3b/
recipe: https://datasets.datalad.org/shub/ozanarkancan/r2r-navi/latest/2020-05-03-1c6befe4-3d532c3b/Singularity
collection: ozanarkancan/r2r-navi
---

# ozanarkancan/r2r-navi:latest

```bash
$ singularity pull shub://ozanarkancan/r2r-navi:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%runscript
    echo "Run script"

%environment
    LANG=C.UTF-8
    LC_ALL=C.UTF-8
    export LANG LC_ALL
    export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/local/cuda/lib64:/usr/local/cuda/lib:/opt/cudnn/lib64:/usr/lib/x86_64-linux-gnu/mesa:$LD_LIBRARY_PATH
%post
    apt-get update && apt-get install -q -y --no-install-recommends \
        software-properties-common
    add-apt-repository -y ppa:ubuntu-x-swat/updates
    apt-get -y dist-upgrade

    export DEBIAN_FRONTEND=noninteractive
    
    apt-get update && apt-get install -q -y --no-install-recommends \
        sudo \
        less \
        xorg \
        xserver-xorg \
        x-window-system \
        xinit \
        binutils \
        dirmngr \
        gnupg2 \
        build-essential \
        libzmq3-dev \
        pkg-config \
        python3.7 \
        python3-dev \
        python3-pip \
        git \
        vim \
        libxml2 \
        wget \
        curl \
        unzip \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libgtest-dev \
        cmake \
        xserver-xorg \
        libx11-dev \
        xorg-dev \
        libopencv-dev \
        python-opencv \
        libjsoncpp-dev \
        doxygen \
        mesa-utils \
        freeglut3 \
        freeglut3-dev \
        libglm-dev \
        libosmesa6-dev \
        libosmesa6\
        libglew-dev\
        && rm -rf /var/lib/apt/lists/*

    pip3 install setuptools
    pip3 install numpy pandas opencv-python networkx h5py tqdm vocab revtok Pillow constants torch==1.1.0 torchvision==0.3.0 tensorboardX==1.8 ai2thor==2.1.0

    mkdir -p /opt/cudnn
    mkdir -p /usr/local/cuda
```

## Collection

 - Name: [ozanarkancan/r2r-navi](https://github.com/ozanarkancan/r2r-navi)
 - License: None

