---
id: 9371
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "guppy_3.1.5-nvidia410"
commit: "5cc8496183d02d1d177f2493ff5e5ba4a288edb9"
version: "6714272c67be1708605468fb999b99a6"
build_date: "2019-10-30T01:27:28.685Z"
size_mb: 2213
size: 727466015
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_3.1.5-nvidia410/2019-10-30-5cc84961-6714272c/6714272c67be1708605468fb999b99a6.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_3.1.5-nvidia410/2019-10-30-5cc84961-6714272c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_3.1.5-nvidia410/2019-10-30-5cc84961-6714272c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:guppy_3.1.5-nvidia410

```bash
$ singularity pull shub://TomHarrop/singularity-containers:guppy_3.1.5-nvidia410
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.1.5 with nvidia-410

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 3.1.5"

%post
    export DEBIAN_FRONTEND=noninteractive

    # deps
    apt-get update
    apt-get install -y \
        apt-transport-https \
        lsb-release \
        nvidia-modprobe \
        software-properties-common \
        wget 

    # byo nvidia driver
    add-apt-repository -y ppa:graphics-drivers/ppa
    apt update
    apt install -y nvidia-410 libcuda1-410

    # install guppy from ONT repo
    export PLATFORM=$(lsb_release -cs) 
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add - 
    echo \
        "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list 
    apt-get update
    apt-get install -y \
        --no-install-recommends \
        ont-guppy=3.1.5-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

