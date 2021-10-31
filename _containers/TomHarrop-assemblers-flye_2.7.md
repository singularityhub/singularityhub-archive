---
id: 12452
name: "TomHarrop/assemblers"
branch: "master"
tag: "flye_2.7"
commit: "e7f1aaab95bda2945ae056fe24b05c660bad5ade"
version: "02da1618144345f21d663c5987638096bb20e723d3d3ea431370dea730746f6a"
build_date: "2020-12-08T22:01:44.662Z"
size_mb: 209.421875
size: 219594752
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.7/2020-12-08-e7f1aaab-02da1618/02da1618144345f21d663c5987638096bb20e723d3d3ea431370dea730746f6a.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.7/2020-12-08-e7f1aaab-02da1618/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/flye_2.7/2020-12-08-e7f1aaab-02da1618/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:flye_2.7

```bash
$ singularity pull shub://TomHarrop/assemblers:flye_2.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Flye 2.7
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.7"

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
    git checkout -f 2.7
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

