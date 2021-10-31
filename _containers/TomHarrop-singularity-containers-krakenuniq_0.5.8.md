---
id: 8387
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "krakenuniq_0.5.8"
commit: "17bce598aaf408bf908afc34717d9dc6ddf3a2c6"
version: "165cc47245fbc80d9737ed10b97b2a15"
build_date: "2019-06-04T21:30:00.828Z"
size_mb: 518
size: 179793951
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/krakenuniq_0.5.8/2019-06-04-17bce598-165cc472/165cc47245fbc80d9737ed10b97b2a15.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/krakenuniq_0.5.8/2019-06-04-17bce598-165cc472/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/krakenuniq_0.5.8/2019-06-04-17bce598-165cc472/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:krakenuniq_0.5.8

```bash
$ singularity pull shub://TomHarrop/singularity-containers:krakenuniq_0.5.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.04

%help

    krakenuniq 0.5.8
    https://github.com/fbreitwieser/krakenuniq

%labels

    MAINTAINER "Tom Harrop"
    VERSION "krakenuniq 0.5.8"

%post

    # dependencies
    apt update
    apt install -y \
        build-essential \
        cpanminus \
        curl \
        git \
        jellyfish1 \
        language-pack-en \
        ncbi-blast+ \
        wget \
        zlib1g-dev 

    # intall perl modules
    cpanm --force ExtUtils::Helpers
    cpanm LWP::Simple || cat /.cpanm/work/*/build.log

    # install krakenuniq
    wget -O krakenuniq.tar.gz \
        --no-check-certificate \
        https://github.com/fbreitwieser/krakenuniq/archive/v0.5.8.tar.gz

    mkdir krakenuniq
    tar -zxf krakenuniq.tar.gz \
        -C krakenuniq \
        --strip-components 1
    cd krakenuniq || exit 1
    ./install_krakenuniq.sh /usr/local/bin
    cd .. || exit 1
    rm -rf krakenuniq krakenuniq.tar.gz

%runscript

    exec /usr/local/bin/krakenuniq "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

