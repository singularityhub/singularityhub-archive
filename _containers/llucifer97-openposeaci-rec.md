---
id: 9820
name: "llucifer97/openposeaci"
branch: "master"
tag: "rec"
commit: "e1413e9a4b892778a0796ccbd68a3218c3764ecb"
version: "694d87712021f8af136a22e3b3955dea"
build_date: "2019-06-16T11:06:35.442Z"
size_mb: 5009
size: 2614460447
sif: "https://datasets.datalad.org/shub/llucifer97/openposeaci/rec/2019-06-16-e1413e9a-694d8771/694d87712021f8af136a22e3b3955dea.simg"
url: https://datasets.datalad.org/shub/llucifer97/openposeaci/rec/2019-06-16-e1413e9a-694d8771/
recipe: https://datasets.datalad.org/shub/llucifer97/openposeaci/rec/2019-06-16-e1413e9a-694d8771/Singularity
collection: llucifer97/openposeaci
---

# llucifer97/openposeaci:rec

```bash
$ singularity pull shub://llucifer97/openposeaci:rec
```

## Singularity Recipe

```singularity
BootStrap: docker
From: garyfeng/docker-openpose


%runscript
    cd /openpose-master
    exec /build/examples/openpose/openpose.bin "$@"
%environment

%post
    #need to install correct gpu drivers
    apt-get update
    apt-get install -y --no-install-recommends \
    build-essential \
    apt-utils \
    gcc-multilib \
    wget \
    unzip \
    python-dev \
    python3-dev \
    python-pip \
    python3-pip \
    pkg-config \
    python-setuptools \
    python3-setuptools \
    g++ \
    libqt4-dev \
    libqt4-opengl-dev \
    qt4-qmake \
    qt4-qtconfig \
    libglew-dev \
    cimg-dev \
    libgsl0-dev \
    libtiff5-dev \
    cmake \
    cmake-gui \
    doxygen \
    software-properties-common \
    python-software-properties \
    nux-tools \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    mesa-utils \
    
    # install nvidia driver (current system version: 390.30)
    add-apt-repository -y ppa:graphics-drivers/ppa
    apt-get install -y nvidia-390-dev

    #------------------------------------------------------------------------------
    # Create local binding points for our ICS-ACI
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [llucifer97/openposeaci](https://github.com/llucifer97/openposeaci)
 - License: None

