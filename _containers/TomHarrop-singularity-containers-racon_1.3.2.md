---
id: 6669
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "racon_1.3.2"
commit: "368c865905bac2d760a5f395a488540b93ae3e40"
version: "aa95b7b3a1752fa935ad567351ce9b17"
build_date: "2021-03-15T10:16:03.797Z"
size_mb: 543
size: 232730655
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/racon_1.3.2/2021-03-15-368c8659-aa95b7b3/aa95b7b3a1752fa935ad567351ce9b17.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/racon_1.3.2/2021-03-15-368c8659-aa95b7b3/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/racon_1.3.2/2021-03-15-368c8659-aa95b7b3/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:racon_1.3.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:racon_1.3.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Racon v1.3.2
    https://github.com/isovic/racon

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Racon v1.3.2"

%post
    # deps
    apt-get clean
    apt-get update
    apt-get install -y \
        build-essential \
        cmake \
        language-pack-en \
        python \
        wget 

    # install racon
    mkdir racon
    wget -O "racon.tar.gz" \
        --no-check-certificate \
        https://github.com/isovic/racon/releases/download/1.3.2/racon-v1.3.2.tar.gz
    tar -zxf racon.tar.gz \
        -C racon \
        --strip-components 1

    cd racon || exit 1
    mkdir build && cd build || exit 1
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -Dracon_build_tests=ON \
        -Dracon_build_wrapper=ON \
        ..
    make && make install

%runscript
    exec /usr/local/bin/racon "$@"

%environment
    export PATH="${PATH}:/racon/build/bin"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

