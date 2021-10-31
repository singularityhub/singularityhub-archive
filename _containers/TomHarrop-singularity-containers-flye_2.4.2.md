---
id: 8466
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "flye_2.4.2"
commit: "8c81b8f674350003c3cf0c3195d255d28da45e0f"
version: "84f0d256e6dd8e771ba66b6b077a0632"
build_date: "2019-09-05T02:32:57.710Z"
size_mb: 454
size: 150466591
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/flye_2.4.2/2019-09-05-8c81b8f6-84f0d256/84f0d256e6dd8e771ba66b6b077a0632.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/flye_2.4.2/2019-09-05-8c81b8f6-84f0d256/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/flye_2.4.2/2019-09-05-8c81b8f6-84f0d256/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:flye_2.4.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:flye_2.4.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Flye 2.4.2
    https://github.com/fenderglass/Flye

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Flye 2.4.2"

%post
    # deps
    apt-get clean
    apt-get update
    apt-get install -y \
        build-essential \
        language-pack-en \
        python \
        wget \
        zlib1g-dev

    # install flye
    mkdir Flye
    wget -O "Flye.tar.gz" \
        --no-check-certificate \
        https://github.com/fenderglass/Flye/archive/2.4.2.tar.gz
    tar -zxf Flye.tar.gz \
        -C Flye \
        --strip-components 1

    cd Flye || exit 1
    python setup.py install
    cd .. || exit 1
    rm -r Flye.tar.gz Flye

%runscript
    exec /usr/local/bin/flye "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

