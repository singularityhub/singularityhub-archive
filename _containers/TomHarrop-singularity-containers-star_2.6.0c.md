---
id: 3755
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "star_2.6.0c"
commit: "2dde121aba48dd0ae0f988dce174c71ce2060520"
version: "eaa90a258fdb26b6b0ce7d07246ffe2c"
build_date: "2018-09-10T22:18:08.541Z"
size_mb: 353
size: 161460255
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/star_2.6.0c/2018-09-10-2dde121a-eaa90a25/eaa90a258fdb26b6b0ce7d07246ffe2c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/star_2.6.0c/2018-09-10-2dde121a-eaa90a25/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/star_2.6.0c/2018-09-10-2dde121a-eaa90a25/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:star_2.6.0c

```bash
$ singularity pull shub://TomHarrop/singularity-containers:star_2.6.0c
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential wget zlib1g-dev

%help

    Container for STAR 2.6.0c
    https://github.com/alexdobin/STAR/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "STAR 2.6.0c"

%runscript

    exec /usr/local/bin/STAR "$@"

%post

    # install STAR
    wget -O "star.tar.gz" \
        --no-check-certificate \
        https://github.com/alexdobin/STAR/archive/2.6.0c.tar.gz
    mkdir star
    tar -zxf star.tar.gz \
        -C star \
        --strip-components 1
    cd star/source || exit 1
    make
    cp STAR /usr/local/bin
    cd ../../ || exit 1
    rm -rf star.tar.gz star
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

