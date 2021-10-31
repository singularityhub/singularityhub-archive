---
id: 12416
name: "TomHarrop/assemblers"
branch: "master"
tag: "flye_2.7b-cf8c288"
commit: "81c28101b971b06c1e135823d50ba5a2a120ac38"
version: "145f7c216cf46b05c0ce4cb00466b89a4e72c8e981e881d623a39f79a9bd94a9"
build_date: "2020-03-02T21:04:18.907Z"
size_mb: 209.48046875
size: 219656192
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.7b-cf8c288/2020-03-02-81c28101-145f7c21/145f7c216cf46b05c0ce4cb00466b89a4e72c8e981e881d623a39f79a9bd94a9.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.7b-cf8c288/2020-03-02-81c28101-145f7c21/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.7b-cf8c288/2020-03-02-81c28101-145f7c21/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:flye_2.7b-cf8c288

```bash
$ singularity pull shub://TomHarrop/assemblers:flye_2.7b-cf8c288
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Flye 2.7b-cf8c288
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.7b-cf8c288"

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
    git checkout -f cf8c288
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

