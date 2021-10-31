---
id: 6880
name: "willgpaik/MorphoGraphX_aci"
branch: "master"
tag: "latest"
commit: "a096818a34da9b72d7f927629df462e711691426"
version: "2ab045d7df6a61f53a1689346fe2d88c"
build_date: "2019-11-08T14:03:35.561Z"
size_mb: 3840.0
size: 1786650655
sif: "https://datasets.datalad.org/shub/willgpaik/MorphoGraphX_aci/latest/2019-11-08-a096818a-2ab045d7/2ab045d7df6a61f53a1689346fe2d88c.sif"
url: https://datasets.datalad.org/shub/willgpaik/MorphoGraphX_aci/latest/2019-11-08-a096818a-2ab045d7/
recipe: https://datasets.datalad.org/shub/willgpaik/MorphoGraphX_aci/latest/2019-11-08-a096818a-2ab045d7/Singularity
collection: willgpaik/MorphoGraphX_aci
---

# willgpaik/MorphoGraphX_aci:latest

```bash
$ singularity pull shub://willgpaik/MorphoGraphX_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.1-devel-ubuntu16.04

%runscript

%environment
    # nvidia driver libs specific cuda version libs are mounted by --bind command at run
    # required for GPU enabled container
    SHELL=/bin/bash
    CPATH="/cuda/include:$CPATH"
    PATH="/cuda/bin:/nvidia:$PATH"
    LD_LIBRARY_PATH="/cuda/lib64:/nvidia:$LD_LIBRARY_PATH"
    CUDA_HOME="/cuda"
    export PATH LD_LIBRARY_PATH CPATH CUDA_HOME
    LD_PRELOAD="/opt/eod/lib/libopentextdlfaker.so.3:/opt/eod/lib/libopentextglfaker.so.3 \
        :/opt/eod/lib64/libopentextdlfaker.so.3:/opt/eod/lib64/libopentextglfaker.so.3"
    export LD_PRELOAD
    

%post
    apt-get -y update
    apt-get -y upgrade
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
    subversion \
    libinsighttoolkit4-dev
    
    
    # Download requires libraries for EoD:
    cd /opt/
    svn export https://github.com/willgpaik/MorphoGraphX_aci.git/trunk/eod_graphics_libraries
    mv eod_graphics_libraries eod
    
    
    # https://askubuntu.com/a/872397
    
    # install nvidia driver (current system version: 390.30)
    add-apt-repository -y ppa:graphics-drivers/ppa
    apt-get install -y nvidia-390-dev

    
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    
    apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
    
    cd /gpfs/scratch/
    
    wget https://www.mpipz.mpg.de/4607782/MGX-1_0_1280-LinuxMint18_1-CellAtlas-Cuda9_1.zip
    unzip MGX-1_0_1280-LinuxMint18_1-CellAtlas-Cuda9_1.zip
    dpkg -i MGX-1.0.1280-LinuxMint18.1-Cuda9.1-CellAtlas.deb || true
    apt-get install -y -f
    
    rm MGX-1_0_1280-LinuxMint18_1-CellAtlas-Cuda9_1.zip
    rm MGX-1.0.1280-LinuxMint18.1-Cuda9.1-CellAtlas.deb
```

## Collection

 - Name: [willgpaik/MorphoGraphX_aci](https://github.com/willgpaik/MorphoGraphX_aci)
 - License: None

