---
id: 9756
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "bracken_2.2"
commit: "5c2812870e3db907993a0304afb24289887d501e"
version: "57b002998bb026cc75c32d6c4f7f261e"
build_date: "2019-06-13T22:59:54.038Z"
size_mb: 487
size: 169119775
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bracken_2.2/2019-06-13-5c281287-57b00299/57b002998bb026cc75c32d6c4f7f261e.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bracken_2.2/2019-06-13-5c281287-57b00299/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bracken_2.2/2019-06-13-5c281287-57b00299/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:bracken_2.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:bracken_2.2
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:kraken_2.0.8beta

%help

    bracken 2.2
    https://github.com/jenniferlu717/Bracken

%labels

    MAINTAINER "Tom Harrop"
    VERSION "bracken 2.2"

%post
    # install bracken
    wget -O bracken.tar.gz \
        --no-check-certificate \
        https://github.com/jenniferlu717/Bracken/archive/v2.2.tar.gz
    mkdir bracken
    tar -zxf bracken.tar.gz \
        -C bracken \
        --strip-components 1
    cd bracken/src || exit 1
    make
    cd ../.. || exit 1
    rm bracken.tar.gz

%environment
    export PATH="${PATH}:/bracken:/bracken/src"

%runscript

    exec /bracken/bracken "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

