---
id: 9045
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "guppy_3.0.3"
commit: "011bb5e7e97c2262985b8fe9fdbc8b5553917499"
version: "a5310df4549d757236df790acb60d6d2"
build_date: "2019-05-13T10:27:26.595Z"
size_mb: 2093
size: 686620703
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_3.0.3/2019-05-13-011bb5e7-a5310df4/a5310df4549d757236df790acb60d6d2.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_3.0.3/2019-05-13-011bb5e7-a5310df4/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_3.0.3/2019-05-13-011bb5e7-a5310df4/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:guppy_3.0.3

```bash
$ singularity pull shub://TomHarrop/singularity-containers:guppy_3.0.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 3.0.3

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 3.0.3"

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
        ont-guppy=3.0.3-1~xenial \
        nvidia-modprobe

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

