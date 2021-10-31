---
id: 4847
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "spades_3.12.0"
commit: "a73aea55dd49a241b31f6dde7b9433eb2d53df69"
version: "9e88557dfa52a678a01a20b2841230b1"
build_date: "2019-01-25T00:29:15.719Z"
size_mb: 478
size: 175157279
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/spades_3.12.0/2019-01-25-a73aea55-9e88557d/9e88557dfa52a678a01a20b2841230b1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/spades_3.12.0/2019-01-25-a73aea55-9e88557d/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/spades_3.12.0/2019-01-25-a73aea55-9e88557d/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:spades_3.12.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:spades_3.12.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    Spades 3.12.0
    http://cab.spbu.ru/software/spades/

%labels

    MAINTAINER "Tom Harrop"
    VERSION "Spades 3.12.0"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        cmake \
        language-pack-en \
        libbz2-dev \
        python \
        wget \
        zlib1g-dev
        
    # install Spades
    wget -O "spades.tar.gz" \
        --no-check-certificate \
        http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0.tar.gz
    mkdir spades
    tar -zxf spades.tar.gz \
        -C spades \
        --strip-components 1
    cd spades || exit 1
    PREFIX=/usr/local ./spades_compile.sh
    cd .. || exit 1
    rm -rf spades spades.tar.gz

%runscript

    exec /usr/local/bin/spades.py "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

