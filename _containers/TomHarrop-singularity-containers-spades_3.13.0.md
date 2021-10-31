---
id: 6572
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "spades_3.13.0"
commit: "bc268f2329322fd56ab9d71822e5aed96435fc57"
version: "085bb4c8715dc01fc291c70966ee5c4a"
build_date: "2019-01-25T08:49:35.358Z"
size_mb: 457
size: 160931871
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/spades_3.13.0/2019-01-25-bc268f23-085bb4c8/085bb4c8715dc01fc291c70966ee5c4a.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/spades_3.13.0/2019-01-25-bc268f23-085bb4c8/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/spades_3.13.0/2019-01-25-bc268f23-085bb4c8/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:spades_3.13.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:spades_3.13.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    Spades 3.13.0
    http://cab.spbu.ru/software/spades/

%labels

    MAINTAINER "Tom Harrop"
    VERSION "Spades 3.13.0"

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
        http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0.tar.gz
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

