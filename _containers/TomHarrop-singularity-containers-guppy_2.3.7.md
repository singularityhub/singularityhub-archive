---
id: 7999
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "guppy_2.3.7"
commit: "5caf19924809888ab97f2590c14d2ff39fccd318"
version: "af44c34b4a780360112b7d87aa47e852"
build_date: "2019-03-29T01:29:22.079Z"
size_mb: 1876
size: 642306079
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_2.3.7/2019-03-29-5caf1992-af44c34b/af44c34b4a780360112b7d87aa47e852.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_2.3.7/2019-03-29-5caf1992-af44c34b/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_2.3.7/2019-03-29-5caf1992-af44c34b/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:guppy_2.3.7

```bash
$ singularity pull shub://TomHarrop/singularity-containers:guppy_2.3.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 2.3.7

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 2.3.7"

%post
    # deps
    apt-get update
    apt-get install -y \
        apt-transport-https \
        lsb-release \
        wget 

    # install guppy from ONT repo
    export PLATFORM=$(lsb_release -cs) 
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub \
        | apt-key add - 
    echo \
        "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" \
        | tee /etc/apt/sources.list.d/nanoporetech.sources.list 
    apt-get update
    DEBIAN_FRONTEND=noninteractive \
        apt-get install -y \
        ont-guppy=2.3.7-1~xenial \
        nvidia-modprobe

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

