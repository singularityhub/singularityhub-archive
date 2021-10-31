---
id: 7929
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "vcftools_0.1.16"
commit: "6ec2aff7b2f7df278991c177d6061b1857982f4b"
version: "b7e92cd92d7477a523e9241e2d4281f3"
build_date: "2021-03-04T19:04:17.720Z"
size_mb: 253
size: 82649119
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/vcftools_0.1.16/2021-03-04-6ec2aff7-b7e92cd9/b7e92cd92d7477a523e9241e2d4281f3.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/vcftools_0.1.16/2021-03-04-6ec2aff7-b7e92cd9/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/vcftools_0.1.16/2021-03-04-6ec2aff7-b7e92cd9/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:vcftools_0.1.16

```bash
$ singularity pull shub://TomHarrop/singularity-containers:vcftools_0.1.16
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.9

%help
    Container for vcftools 0.1.16

%labels
    VERSION "vcftools 0.1.16"

%post
    # packages
    apk add --update \
        bash \
        build-base \
        gcc \
        git \
        perl \
        wget \
        zlib-dev

    # download vcftools
    mkdir vcftools
    wget \
        -O "vcftools.tar.gz" \
        --no-check-certificate \
        https://github.com/vcftools/vcftools/releases/download/v0.1.16/vcftools-0.1.16.tar.gz
    tar -zxf vcftools.tar.gz \
        -C vcftools \
        --strip-components 2

    cd vcftools || exit 1
    ./configure
    make 
    make install
    cd .. || exit 1
    rm -rf vcftools vcftools.tar.gz

%runscript
    exec /usr/local/bin/vcftools "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

