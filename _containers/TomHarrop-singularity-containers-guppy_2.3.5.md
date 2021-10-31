---
id: 7479
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "guppy_2.3.5"
commit: "0f6a9e66f884eeeaee2b3a8b9a9e32423d625c64"
version: "08709be3f471785206c84dd2eaba0a6a"
build_date: "2019-02-27T08:08:59.301Z"
size_mb: 1880
size: 643211295
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_2.3.5/2019-02-27-0f6a9e66-08709be3/08709be3f471785206c84dd2eaba0a6a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/guppy_2.3.5/2019-02-27-0f6a9e66-08709be3/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/guppy_2.3.5/2019-02-27-0f6a9e66-08709be3/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:guppy_2.3.5

```bash
$ singularity pull shub://TomHarrop/singularity-containers:guppy_2.3.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
    Guppy 2.3.5

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Guppy 2.3.5"

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
        ont-guppy=2.3.5-1~xenial

%runscript
    exec /usr/bin/guppy_basecaller "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

