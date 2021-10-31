---
id: 2902
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "scrmshaw_20180523"
commit: "42d7e2da3c422334dd0a0120f3a3d0a3b268a9b5"
version: "f39568cde123eace5881811d8c9e0345"
build_date: "2018-05-25T02:19:39.182Z"
size_mb: 775
size: 240390175
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/scrmshaw_20180523/2018-05-25-42d7e2da-f39568cd/f39568cde123eace5881811d8c9e0345.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/scrmshaw_20180523/2018-05-25-42d7e2da-f39568cd/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/scrmshaw_20180523/2018-05-25-42d7e2da-f39568cd/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:scrmshaw_20180523

```bash
$ singularity pull shub://TomHarrop/singularity-containers:scrmshaw_20180523
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioperl/bioperl:latest

%help

    Container for SCRMshaw 05142018
    http://halfonlab.ccr.buffalo.edu/scrmshaw.html

%labels

    MAINTAINER "Tom Harrop"
    VERSION "SCRMshaw 05142018"

%post

    export DEBIAN_FRONTEND=noninteractive

    # install apt packages
    apt-get update \
        && apt-get install -y \
        language-pack-en \
        wget

    # download scrmshaw
    wget -O "scrmshaw.tar.gz" \
        http://halfonlab.ccr.buffalo.edu/scrmshaw/SCRMshaw.05142018.tar.gz
    mkdir scrmshaw
    tar -zxf scrmshaw.tar.gz \
        -C scrmshaw \
        --strip-components 1

    # build
    cd scrmshaw || exit 1
    make
    chmod -R a+r /scrmshaw
    chmod -R a+x /scrmshaw

    # fix the example data
    printf "/scrmshaw/example/test_data/mapping0.ap\n" \
        > /scrmshaw/example/test_data/trainingSet.lst     

    # tidy up
    cd .. || exit 1
    rm scrmshaw.tar.gz

%runscript

    exec /scrmshaw/code/scrm.pl "$@"

%environment

    PATH="/scrmshaw/code:/scrmshaw/bin:${PATH}"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

