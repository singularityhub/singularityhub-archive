---
id: 4206
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "clustalo_1.2.4"
commit: "5df9935516bcd67bcc70b6563f3046068e52b5df"
version: "bac9c3fddaae598c34169e16fde4e470"
build_date: "2019-12-16T02:12:16.308Z"
size_mb: 415
size: 153407519
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/clustalo_1.2.4/2019-12-16-5df99355-bac9c3fd/bac9c3fddaae598c34169e16fde4e470.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/clustalo_1.2.4/2019-12-16-5df99355-bac9c3fd/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/clustalo_1.2.4/2019-12-16-5df99355-bac9c3fd/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:clustalo_1.2.4

```bash
$ singularity pull shub://TomHarrop/singularity-containers:clustalo_1.2.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    Clustal Omega 1.2.4
    http://www.clustal.org/omega/
    trimAl 1.4.1
    https://github.com/scapella/trimal/releases

%labels

    MAINTAINER "Tom Harrop"
    VERSION "clustalo 1.2.4"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        language-pack-en \
        libargtable2-dev \
        libgomp1 \
        libopenmpi-dev \
        openmpi-bin \
        wget

    # install clustalo
    wget -O clustalo.tar.gz \
        --no-check-certificate \
        http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz
    mkdir clustalo
    tar -zxf clustalo.tar.gz \
        -C clustalo \
        --strip-components 1
    cd clustalo || exit 1
    ./configure
    make
    make install
    cd .. || exit 1
    rm -rf clustalo clustalo.tar.gz

    # install trimal
    wget -O trimal.tar.gz \
        --no-check-certificate \
        https://github.com/scapella/trimal/archive/v1.4.1.tar.gz
    mkdir trimal
    tar -zxf trimal.tar.gz \
        -C trimal \
        --strip-components 1
    cd trimal/source || exit 1
    make
    cp readal statal trimal /usr/local/bin/
    cd ../../ || exit 1
    rm -rf trimal trimal.tar.gz

%runscript

    exec /usr/local/bin/clustalo "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

