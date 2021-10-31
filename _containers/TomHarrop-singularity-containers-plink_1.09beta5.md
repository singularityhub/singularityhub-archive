---
id: 4865
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "plink_1.09beta5"
commit: "98c69c859b563f91cc18264d5ed6bc510a461c40"
version: "43028012f29a70de72e266ce4e6621f9"
build_date: "2018-09-18T03:28:17.926Z"
size_mb: 401
size: 147279903
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/plink_1.09beta5/2018-09-18-98c69c85-43028012/43028012f29a70de72e266ce4e6621f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/plink_1.09beta5/2018-09-18-98c69c85-43028012/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/plink_1.09beta5/2018-09-18-98c69c85-43028012/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:plink_1.09beta5

```bash
$ singularity pull shub://TomHarrop/singularity-containers:plink_1.09beta5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    plink 1.09 beta 5
    http://www.cog-genomics.org/plink/1.9/

%labels

    MAINTAINER "Tom Harrop"
    VERSION "plink 1.09 beta 5"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        curl \
        language-pack-en \
        libatlas-base-dev \
        libblas-dev \
        wget

    # install plink
    wget -O "plink.tar.gz" \
        --no-check-certificate \
        https://github.com/chrchang/plink-ng/archive/b15c19f.tar.gz
    mkdir plink
    tar -zxf plink.tar.gz \
        -C plink \
        --strip-components 1

    cd plink/1.9 || exit 1
    ./plink_first_compile

    mv plink /usr/local/bin

    cd ../../ || exit 1
    rm -rf plink plink.tar.gz

%runscript

    exec /usr/bin/plink "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

