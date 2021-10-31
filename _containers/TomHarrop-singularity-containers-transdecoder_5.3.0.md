---
id: 4952
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "transdecoder_5.3.0"
commit: "5d255615ab338131511b9ee71291ac6cf57e002d"
version: "b1bc75e47da8f0ed4a49063d45db2ad6"
build_date: "2018-09-24T07:21:04.891Z"
size_mb: 323
size: 127090719
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/transdecoder_5.3.0/2018-09-24-5d255615-b1bc75e4/b1bc75e47da8f0ed4a49063d45db2ad6.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/transdecoder_5.3.0/2018-09-24-5d255615-b1bc75e4/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/transdecoder_5.3.0/2018-09-24-5d255615-b1bc75e4/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:transdecoder_5.3.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:transdecoder_5.3.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    TransDecoder 5.3.0
    https://github.com/TransDecoder/TransDecoder/wiki

%labels

    MAINTAINER "Tom Harrop"
    VERSION "TransDecoder 5.3.0"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        hmmer \
        language-pack-en \
        libany-uri-escape-perl \
        make \
        ncbi-blast+ \
        perl \
        wget

    # install TD
    wget -O "transdecoder.tar.gz" \
        --no-check-certificate \
        https://github.com/TransDecoder/TransDecoder/archive/TransDecoder-v5.3.0.tar.gz
    mkdir transdecoder
    tar -zxf transdecoder.tar.gz \
        -C transdecoder \
        --strip-components 1
    rm -f transdecoder.tar.gz

%environment

    export PATH="${PATH}:/transdecoder"

%runscript

    exec /transdecoder/TransDecoder.LongOrfs "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

