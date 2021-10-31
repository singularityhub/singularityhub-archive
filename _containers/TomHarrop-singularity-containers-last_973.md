---
id: 7574
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "last_973"
commit: "9c82a302fe63cfd19b01d259dcfc3097b3ca603d"
version: "09312b7b84b56f8cba89a92b3abe92e5"
build_date: "2019-03-04T03:18:47.879Z"
size_mb: 256
size: 80777247
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/last_973/2019-03-04-9c82a302-09312b7b/09312b7b84b56f8cba89a92b3abe92e5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/last_973/2019-03-04-9c82a302-09312b7b/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/last_973/2019-03-04-9c82a302-09312b7b/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:last_973

```bash
$ singularity pull shub://TomHarrop/singularity-containers:last_973
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.9

%help
    Container for LAST 973

%labels
    VERSION "LAST 973"

%post
    # packages
    apk add --update \
        bash \
        build-base \
        gcc \
        parallel \
        python \
        wget \
        zlib-dev

    # download last
    wget http://last.cbrc.jp/last-973.zip
    unzip last-973.zip
    cd last-973 || exit 1
    make
    make install
    cd .. || exit 1
    rm -rf last-973.zip last-973

%runscript
    exec /usr/local/bin/lastal "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

