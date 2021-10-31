---
id: 11913
name: "TomHarrop/assemblers"
branch: "master"
tag: "flye_2.6"
commit: "2070831169299e5fdd4f2d3f434f2c6719a8311f"
version: "f40eecf4a42e6b904cc99ee7499931b44e999b889acc6db98e699ec3b72995a8"
build_date: "2019-12-23T23:39:43.255Z"
size_mb: 150.578125
size: 157892608
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.6/2019-12-23-20708311-f40eecf4/f40eecf4a42e6b904cc99ee7499931b44e999b889acc6db98e699ec3b72995a8.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.6/2019-12-23-20708311-f40eecf4/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.6/2019-12-23-20708311-f40eecf4/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:flye_2.6

```bash
$ singularity pull shub://TomHarrop/assemblers:flye_2.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Flye 2.6
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.6"

%post

    # deps
    apt-get clean
    apt-get update
    apt-get install -y \
        build-essential \
        python3 \
        python3-setuptools \
        wget \
        zlib1g-dev

    # install flye
    mkdir Flye
    wget -O "Flye.tar.gz" \
        --no-check-certificate \
        https://github.com/fenderglass/Flye/archive/2.6.tar.gz
    tar -zxf Flye.tar.gz \
        -C Flye \
        --strip-components 1

    cd Flye || exit 1
    python3 setup.py install
    cd .. || exit 1
    rm -r Flye.tar.gz Flye

%environment
    export LC_ALL="C"

%runscript
    exec /usr/local/bin/flye "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

