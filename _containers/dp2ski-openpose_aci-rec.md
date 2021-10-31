---
id: 6484
name: "dp2ski/openpose_aci"
branch: "master"
tag: "rec"
commit: "1e2dc4e439e8ea7c63d70c1a2b94f056a654ca71"
version: "8e201cc7078eda0b7114c83108090305"
build_date: "2019-12-23T19:18:40.088Z"
size_mb: 4998
size: 2609901599
sif: "https://datasets.datalad.org/shub/dp2ski/openpose_aci/rec/2019-12-23-1e2dc4e4-8e201cc7/8e201cc7078eda0b7114c83108090305.simg"
url: https://datasets.datalad.org/shub/dp2ski/openpose_aci/rec/2019-12-23-1e2dc4e4-8e201cc7/
recipe: https://datasets.datalad.org/shub/dp2ski/openpose_aci/rec/2019-12-23-1e2dc4e4-8e201cc7/Singularity
collection: dp2ski/openpose_aci
---

# dp2ski/openpose_aci:rec

```bash
$ singularity pull shub://dp2ski/openpose_aci:rec
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

 - Name: [dp2ski/openpose_aci](https://github.com/dp2ski/openpose_aci)
 - License: None

