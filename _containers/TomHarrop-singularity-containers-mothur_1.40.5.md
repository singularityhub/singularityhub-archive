---
id: 5008
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "mothur_1.40.5"
commit: "9b85f37aecfaf09cbc9dd7182ea63c4ccdc1b080"
version: "f0eab7bf3b6c7105395c1f783ddd55a5"
build_date: "2018-09-27T01:15:52.389Z"
size_mb: 622
size: 188686367
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/mothur_1.40.5/2018-09-27-9b85f37a-f0eab7bf/f0eab7bf3b6c7105395c1f783ddd55a5.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/mothur_1.40.5/2018-09-27-9b85f37a-f0eab7bf/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/mothur_1.40.5/2018-09-27-9b85f37a-f0eab7bf/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:mothur_1.40.5

```bash
$ singularity pull shub://TomHarrop/singularity-containers:mothur_1.40.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    Mothur 1.40.5
    https://www.mothur.org/wiki/Main_Page

%labels

    MAINTAINER "Tom Harrop"
    VERSION "Mothur 1.40.5"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        libboost-dev \
        libboost-iostreams-dev \
        libreadline-dev \
        wget \
        zlib1g-dev

    # install mothur
    wget -O "mothur.tar.gz" \
        --no-check-certificate \
        https://github.com/mothur/mothur/archive/v1.40.5.tar.gz
    mkdir mothur
    tar -zxf mothur.tar.gz \
        -C mothur \
        --strip-components 1
    cd mothur || exit 1
    make
    mv mothur /usr/local/bin/
    cd .. || exit 1
    rm -rf mothur mothur.tar.gz

%runscript

    exec /usr/local/bin/mothur "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

