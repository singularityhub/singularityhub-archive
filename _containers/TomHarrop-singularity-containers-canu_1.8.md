---
id: 5779
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "canu_1.8"
commit: "be2d35a5a8b2350270900221aaeff5a0a104a359"
version: "2a22e8402e4ad63eb607806c22dac5f3"
build_date: "2018-12-03T09:49:40.921Z"
size_mb: 1198
size: 380846111
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/canu_1.8/2018-12-03-be2d35a5-2a22e840/2a22e8402e4ad63eb607806c22dac5f3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/canu_1.8/2018-12-03-be2d35a5-2a22e840/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/canu_1.8/2018-12-03-be2d35a5-2a22e840/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:canu_1.8

```bash
$ singularity pull shub://TomHarrop/singularity-containers:canu_1.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10 

%help

    Container for Canu 1.8
    https://github.com/marbl/canu

%labels

    VERSION "Canu 1.8"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        gnuplot \
        language-pack-en \
        openjdk-8-jre \
        perl \
        wget

    # install Canu
    wget -O "canu.tar.gz" \
        --no-check-certificate \
        https://github.com/marbl/canu/archive/v1.8.tar.gz
    mkdir canu
    tar -zxf canu.tar.gz \
        -C canu \
        --strip-components 1
    cd canu/src || exit 1
    make
    cd ../.. || exit 1
    rm -rf canu.tar.gz

%environment

    export PATH="${PATH}:/canu/Linux-amd64/bin"

%runscript

    exec /canu/Linux-amd64/bin/canu "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

