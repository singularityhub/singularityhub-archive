---
id: 11918
name: "TomHarrop/assemblers"
branch: "master"
tag: "flye_2.6-g47548b8"
commit: "465564b815a42cccf059c84d244fb65e8ede57ef"
version: "f65d3753912ecc90f2f84433c113203573b78b3daf9a0395364658368d64c035"
build_date: "2020-06-17T07:25:16.524Z"
size_mb: 206.62109375
size: 216657920
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.6-g47548b8/2020-06-17-465564b8-f65d3753/f65d3753912ecc90f2f84433c113203573b78b3daf9a0395364658368d64c035.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.6-g47548b8/2020-06-17-465564b8-f65d3753/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.6-g47548b8/2020-06-17-465564b8-f65d3753/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:flye_2.6-g47548b8

```bash
$ singularity pull shub://TomHarrop/assemblers:flye_2.6-g47548b8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Flye 2.6-g47548b8
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.6-g47548b8"

%post

    # deps
    apt-get clean
    apt-get update
    apt-get install -y \
        build-essential \
        git \
        python3 \
        python3-setuptools \
        wget \
        zlib1g-dev

    # install flye from release
    # mkdir Flye
    # wget -O "Flye.tar.gz" \
    #     --no-check-certificate \
    #     https://github.com/fenderglass/Flye/archive/2.6.tar.gz
    # tar -zxf Flye.tar.gz \
    #     -C Flye \
    #     --strip-components 1
    # cd Flye || exit 1

    # install Flye from git branch
    git clone https://github.com/fenderglass/Flye
    cd Flye || exit 1
    git checkout -f 47548b8
    git submodule update --init --recursive

    # build and install flye
    make

    # python3 setup.py install
    # cd .. || exit 1
    # rm -r Flye.tar.gz Flye

%environment
    export LC_ALL="C"
    export PATH="${PATH}:/Flye/bin"

%runscript
    exec /Flye/bin/flye "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

