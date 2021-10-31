---
id: 6571
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "flye_2.4"
commit: "8a78de7b3dd9ff8ec13a0b60c3403f861174693e"
version: "5174c30af44ac8cb9adc989c51680aca"
build_date: "2019-04-17T02:51:00.593Z"
size_mb: 454
size: 150052895
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/flye_2.4/2019-04-17-8a78de7b-5174c30a/5174c30af44ac8cb9adc989c51680aca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/flye_2.4/2019-04-17-8a78de7b-5174c30a/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/flye_2.4/2019-04-17-8a78de7b-5174c30a/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:flye_2.4

```bash
$ singularity pull shub://TomHarrop/singularity-containers:flye_2.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Flye 2.4 
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.4 "

%post
    # deps
    apt-get clean
    apt-get update
    apt-get install -y \
        build-essential \
        language-pack-en \
        python \
        wget \
        zlib1g-dev

    # install flye
    mkdir Flye
    wget -O "Flye.tar.gz" \
        --no-check-certificate \
        https://github.com/fenderglass/Flye/archive/2.4.tar.gz
    tar -zxf Flye.tar.gz \
        -C Flye \
        --strip-components 1

    cd Flye || exit 1
    python setup.py install
    cd .. || exit 1
    rm -r Flye.tar.gz Flye

%runscript
    exec /usr/local/bin/flye "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

