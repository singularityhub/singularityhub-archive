---
id: 4667
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "blobtools_1.0.1"
commit: "ec5fffa2069e1657ee57d416828956f3f0c34eb9"
version: "1dc1c2840f48580aead2f3093c28541b"
build_date: "2018-09-04T22:24:14.652Z"
size_mb: 723
size: 294252575
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/blobtools_1.0.1/2018-09-04-ec5fffa2-1dc1c284/1dc1c2840f48580aead2f3093c28541b.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/blobtools_1.0.1/2018-09-04-ec5fffa2-1dc1c284/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/blobtools_1.0.1/2018-09-04-ec5fffa2-1dc1c284/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:blobtools_1.0.1

```bash
$ singularity pull shub://TomHarrop/singularity-containers:blobtools_1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    BlobTools 1.0.1
    https://github.com/DRL/blobtools/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "BlobTools 1.0.1"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        autoconf \
        automake \
        build-essential \
        libbz2-dev \
        libcurl4-gnutls-dev \
        liblzma-dev \
        libncurses5-dev \
        libssl-dev \
        python \
        python-pip \
        wget \
        zlib1g-dev

    # downgrade pip for compatibility
    pip install pip==9.0.3

    # download blobtools
    wget -O "blobtools.tar.gz" \
        --no-check-certificate \
        https://github.com/DRL/blobtools/archive/v1.0.1.tar.gz 
    mkdir blobtools
    tar -zxf blobtools.tar.gz \
        -C blobtools \
        --strip-components 1
    rm -rf blobtools.tar.gz

    # install blobtools
    cd blobtools || exit 1
    (
    export PATH="/usr/local/bin:${PATH}"
    ./install
    )  
    ln -s /blobtools/blobtools /usr/local/bin

%environment

    export PATH="${PATH}:/blobtools/samtools/bin"

%runscript

    exec /usr/local/bin/blobtools "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

