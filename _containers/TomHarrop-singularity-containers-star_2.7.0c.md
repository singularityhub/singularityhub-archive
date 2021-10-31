---
id: 7255
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "star_2.7.0c"
commit: "a1241a6b28cba026d4d237bbf1b0a1faa91ac8ec"
version: "142e413ffee6b36329e9060bf6a2c70e"
build_date: "2020-04-29T23:00:39.275Z"
size_mb: 354
size: 161517599
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/star_2.7.0c/2020-04-29-a1241a6b-142e413f/142e413ffee6b36329e9060bf6a2c70e.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/star_2.7.0c/2020-04-29-a1241a6b-142e413f/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/star_2.7.0c/2020-04-29-a1241a6b-142e413f/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:star_2.7.0c

```bash
$ singularity pull shub://TomHarrop/singularity-containers:star_2.7.0c
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential wget zlib1g-dev

%help

    Container for STAR 2.7.0c
    https://github.com/alexdobin/STAR/releases

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "STAR 2.7.0c"

%runscript

    exec /usr/local/bin/STAR "$@"

%post

    # install STAR
    wget -O "star.tar.gz" \
        --no-check-certificate \
        https://github.com/alexdobin/STAR/archive/2.7.0c.tar.gz
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

