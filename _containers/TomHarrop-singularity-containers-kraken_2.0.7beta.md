---
id: 4844
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "kraken_2.0.7beta"
commit: "1916677c9d4c4904c83df13e63280dec25aff79a"
version: "4754a5150623f1991280351edf753921"
build_date: "2019-12-10T23:34:08.685Z"
size_mb: 496
size: 178880543
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/kraken_2.0.7beta/2019-12-10-1916677c-4754a515/4754a5150623f1991280351edf753921.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/kraken_2.0.7beta/2019-12-10-1916677c-4754a515/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/kraken_2.0.7beta/2019-12-10-1916677c-4754a515/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:kraken_2.0.7beta

```bash
$ singularity pull shub://TomHarrop/singularity-containers:kraken_2.0.7beta
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    kraken2 2.0.7-beta
    https://github.com/DerrickWood/kraken2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "kraken2 2.0.7-beta"

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
        https://github.com/DerrickWood/kraken2/archive/v2.0.7-beta.tar.gz
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

