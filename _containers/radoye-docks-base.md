---
id: 9100
name: "radoye/docks"
branch: "master"
tag: "base"
commit: "e12bd32ce2aae2b3f427ab7ca5d4c3f0ca95615a"
version: "e78bc227e23c065f9819e494ca907398"
build_date: "2019-05-16T02:35:09.602Z"
size_mb: 3640
size: 2098573343
sif: "https://datasets.datalad.org/shub/radoye/docks/base/2019-05-16-e12bd32c-e78bc227/e78bc227e23c065f9819e494ca907398.simg"
url: https://datasets.datalad.org/shub/radoye/docks/base/2019-05-16-e12bd32c-e78bc227/
recipe: https://datasets.datalad.org/shub/radoye/docks/base/2019-05-16-e12bd32c-e78bc227/Singularity
collection: radoye/docks
---

# radoye/docks:base

```bash
$ singularity pull shub://radoye/docks:base
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%labels
  # metadata
  AUTHOR rrs
  VERSION v0.0.5

%help
  Numericcal Dev Container 0: Numericcal Database Service Container. 
  Builds on top of Ubuntu18.04 with NVidia CUDA stack.

  Assumptions: None.

%environment
  # in the container; set up variables
  export CUDA_VER=10.1

%post
  # in the container; post OS install

  # 0. COPY-PASTE (!?!) relevant environment
  #    Unfortunately, this seems to be the only way. No shared params across
  #    sections of Singularity Definition File seem possible.

  # 1. update & install OS level stuff
  apt update -y
  apt install -y --no-install-recommends software-properties-common
  apt-add-repository ppa:neovim-ppa/stable
  apt update -y && apt upgrade -y 
  apt install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    wget \
    gnupg \
    neovim \
    sudo \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    redis-server

%files

%startscript
  # in the container; on the instance creation

%runscript
  # in the container; on the run command

%test
  # run some code for testing
```

## Collection

 - Name: [radoye/docks](https://github.com/radoye/docks)
 - License: None

