---
id: 15752
name: "rstreatercu/C-GLASS"
branch: "moving_otraps"
tag: "latest"
commit: "89dd8b3c9647a2f6b9de2c14192fb67e8fb8551b"
version: "4cd2633c47d00f3686104be151c060f5"
build_date: "2021-04-07T17:03:46.180Z"
size_mb: 795.0
size: 236478495
sif: "https://datasets.datalad.org/shub/rstreatercu/C-GLASS/latest/2021-04-07-89dd8b3c-4cd2633c/4cd2633c47d00f3686104be151c060f5.sif"
url: https://datasets.datalad.org/shub/rstreatercu/C-GLASS/latest/2021-04-07-89dd8b3c-4cd2633c/
recipe: https://datasets.datalad.org/shub/rstreatercu/C-GLASS/latest/2021-04-07-89dd8b3c-4cd2633c/Singularity
collection: rstreatercu/C-GLASS
---

# rstreatercu/C-GLASS:latest

```bash
$ singularity pull shub://rstreatercu/C-GLASS:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:10.2-slim

%post
    apt-get update -qq
    apt-get install -qqy --no-install-recommends \
        build-essential \
        ca-certificates \
        vim \
        git \
        cmake \
        wget \
        curl \
        htop \
        pkg-config \
        doxygen \
        libyaml-cpp-dev \
        libgsl-dev \
        libfftw3-dev \
        libopenmpi-dev \
        libboost-math1.67-dev
    rm -rf ~/.cache
    mkdir /build
    cd /build
    git clone --recursive --single-branch --branch moving_otraps https://github.com/rstreatercu/C-GLASS.git .
    ./install.sh -otI
    rm -rf /build

%runscript
    cglass.exe $*

%test
    cglass.exe --version

%help
    Usage: `singularity run <C-GLASS container> [flags...] <parameter file>`
```

## Collection

 - Name: [rstreatercu/C-GLASS](https://github.com/rstreatercu/C-GLASS)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

