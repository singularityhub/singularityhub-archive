---
id: 9792
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "kraken_2.0.8beta"
commit: "24881cf249321d9be12ca0f4f1acb70b04add6d3"
version: "8b25cc5f3b14c2dc7d2cb3b955efbaa0"
build_date: "2019-06-13T22:59:54.045Z"
size_mb: 483
size: 168136735
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/kraken_2.0.8beta/2019-06-13-24881cf2-8b25cc5f/8b25cc5f3b14c2dc7d2cb3b955efbaa0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/kraken_2.0.8beta/2019-06-13-24881cf2-8b25cc5f/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/kraken_2.0.8beta/2019-06-13-24881cf2-8b25cc5f/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:kraken_2.0.8beta

```bash
$ singularity pull shub://TomHarrop/singularity-containers:kraken_2.0.8beta
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    kraken2 2.0.8-beta
    https://github.com/DerrickWood/kraken2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "kraken2 2.0.8-beta"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        language-pack-en \
        libgomp1 \
        libopenmpi-dev \
        ncbi-blast+ \
        openmpi-bin \
        rsync \
        wget

    # install kraken
    wget -O kraken.tar.gz \
        --no-check-certificate \
        https://github.com/DerrickWood/kraken2/archive/v2.0.8-beta.tar.gz
    mkdir kraken
    tar -zxf kraken.tar.gz \
        -C kraken \
        --strip-components 1
    cd kraken || exit 1
    ./install_kraken2.sh /usr/local/bin
    cd .. || exit 1
    rm -rf kraken kraken.tar.gz

%runscript

    exec /usr/local/bin/kraken2 "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

