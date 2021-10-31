---
id: 11475
name: "TomHarrop/ont-containers"
branch: "master"
tag: "porechop_0.2.3"
commit: "7a3a689ffea8ea81d69d04fe13ee050cd1bab69b"
version: "5e7059dca498b79cb11ecfbf48d14e4603eb2ed6a58a000976125164fd6e8afa"
build_date: "2020-12-10T00:20:00.111Z"
size_mb: 316.4921875
size: 331866112
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/porechop_0.2.3/2020-12-10-7a3a689f-5e7059dc/5e7059dca498b79cb11ecfbf48d14e4603eb2ed6a58a000976125164fd6e8afa.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/porechop_0.2.3/2020-12-10-7a3a689f-5e7059dc/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/porechop_0.2.3/2020-12-10-7a3a689f-5e7059dc/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:porechop_0.2.3

```bash
$ singularity pull shub://TomHarrop/ont-containers:porechop_0.2.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.6.6-stretch

%help
    Porechop 0.2.3
    https://github.com/rrwick/Porechop

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Porechop 0.2.3"

%post
    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential

    # install porechop
    wget -O "porechop.tar.gz" \
        --no-check-certificate \
        https://github.com/rrwick/Porechop/archive/v0.2.3.tar.gz
    mkdir porechop
    tar -zxf porechop.tar.gz \
        -C porechop \
        --strip-components 1
    cd porechop || exit 1
    python3 setup.py install
    cd .. || exit 1
    rm -rf porechop porechop.tar.gz

%runscript
    exec /usr/local/bin/porechop "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

