---
id: 13694
name: "kiwiroy/singularity-tomahawk"
branch: "master"
tag: "latest"
commit: "6d887777e5ba0e9027b42d468c0c0ffbcf945a17"
version: "4ab7c49529e970b14ab43b603f4fbbff905013f3bb39f8603dc6eb6ca64c4586"
build_date: "2020-07-29T09:42:09.779Z"
size_mb: 236.015625
size: 247480320
sif: "https://datasets.datalad.org/shub/kiwiroy/singularity-tomahawk/latest/2020-07-29-6d887777-4ab7c495/4ab7c49529e970b14ab43b603f4fbbff905013f3bb39f8603dc6eb6ca64c4586.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/kiwiroy/singularity-tomahawk/latest/2020-07-29-6d887777-4ab7c495/
recipe: https://datasets.datalad.org/shub/kiwiroy/singularity-tomahawk/latest/2020-07-29-6d887777-4ab7c495/Singularity
collection: kiwiroy/singularity-tomahawk
---

# kiwiroy/singularity-tomahawk:latest

```bash
$ singularity pull shub://kiwiroy/singularity-tomahawk:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:bionic

%labels
    Author kiwiroy@users-noreply.github.com
    Maintainer kiwiroy@users-noreply.github.com
    Version 1.00

%post
### install / update system dependencies
    apt-get -y update && apt-get -y install \
        autoconf             \
        build-essential      \
        curl                 \
        git                  \
        libbz2-dev           \
        libcurl4-openssl-dev \
        liblz4-dev           \
        liblzma-dev          \
        libssl-dev           \
        libzstd-dev          \
        zlib1g-dev
### install htslib 1.9 due to a dependency
    git clone https://github.com/samtools/htslib.git htslib-1.9
    cd htslib-1.9
    git reset --hard 1832d3a
    autoreconf && ./configure && make -j5 && make install
    cd ..
### install zstd - commented as libzstd-dev installs enough
    # git clone https://github.com/facebook/zstd.git zstd
    # cd zstd
    # make -j5 V=1 && make install V=1
    # cd ..
### clone project
    git clone https://github.com/mklarqvist/tomahawk.git tomahawk
    cd tomahawk
    make -j5 && make install
### update ld.so.cache - avoid setting LD_LIBRARY_PATH for libhts.so
    ldconfig

%runscript
    exec tomahawk "$@"
```

## Collection

 - Name: [kiwiroy/singularity-tomahawk](https://github.com/kiwiroy/singularity-tomahawk)
 - License: None

