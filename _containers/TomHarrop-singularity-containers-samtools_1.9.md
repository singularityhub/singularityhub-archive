---
id: 7850
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "samtools_1.9"
commit: "1c05b59821d3728e9088c76a9a1b9e6fcdaaf17b"
version: "020b8ac455edd00d20346776fc75c362"
build_date: "2021-01-04T23:38:46.956Z"
size_mb: 227
size: 80433183
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/samtools_1.9/2021-01-04-1c05b598-020b8ac4/020b8ac455edd00d20346776fc75c362.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/samtools_1.9/2021-01-04-1c05b598-020b8ac4/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/samtools_1.9/2021-01-04-1c05b598-020b8ac4/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:samtools_1.9

```bash
$ singularity pull shub://TomHarrop/singularity-containers:samtools_1.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.9

%help

    samtools 1.9
    bcflib 1.9
    htslib 1.9
    http://www.htslib.org/

%labels

    VERSION "samtools 1.9"

%runscript
    exec /usr/local/bin/samtools "$@"

%post

    # install dependencies
    apk add --update \
        bash \
        build-base \
        bzip2-dev \
        gcc \
        git \
        ncurses-dev \
        wget \
        xz-dev \
        zlib-dev

    # download releases
    mkdir htslib
    wget \
        -O "htslib.tar.bz2" \
        --no-check-certificate \
        https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
    tar -jxf htslib.tar.bz2 \
        -C htslib \
        --strip-components 1
    cd htslib || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf htslib.tar.bz2 htslib

    mkdir samtools
    wget \
        -O "samtools.tar.bz2" \
        --no-check-certificate \
        https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar -jxf samtools.tar.bz2 \
        -C samtools \
        --strip-components 1
    cd samtools || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf samtools.tar.bz2 samtools

    mkdir bcftools
    wget \
        -O "bcftools.tar.bz2" \
        --no-check-certificate \
        https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
    tar -jxf bcftools.tar.bz2 \
        -C bcftools \
        --strip-components 1
    cd bcftools || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf bcftools.tar.bz2 bcftools
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

