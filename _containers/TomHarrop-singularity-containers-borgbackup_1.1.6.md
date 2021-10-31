---
id: 3894
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "borgbackup_1.1.6"
commit: "b6d12582e87c27ef90a1f715b3bee2056b32fa60"
version: "19fd504c092cd087e01f9baadd4dad2c"
build_date: "2018-08-13T01:36:23.128Z"
size_mb: 600
size: 223957023
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/borgbackup_1.1.6/2018-08-13-b6d12582-19fd504c/19fd504c092cd087e01f9baadd4dad2c.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/borgbackup_1.1.6/2018-08-13-b6d12582-19fd504c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/borgbackup_1.1.6/2018-08-13-b6d12582-19fd504c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:borgbackup_1.1.6

```bash
$ singularity pull shub://TomHarrop/singularity-containers:borgbackup_1.1.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    borgbackup 1.1.6

%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "borgbackup 1.1.6"

%post

    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        fuse \
        libacl1 \
        libacl1-dev \
        libfuse-dev \
        libssl-dev \
        openssl \
        pkg-config \
        python-virtualenv \
        python3 \
        python3-dev \
        python3-pip \
        python3-virtualenv \
        wget 

    # download borg
    wget -O "borg.tar.gz" \
        --no-check-certificate \
        https://github.com/borgbackup/borg/releases/download/1.1.6/borgbackup-1.1.6.tar.gz
    mkdir borg
    tar -zxf borg.tar.gz \
        -C borg \
        --strip-components 1

    # install
    cd borg || exit 1
    pip3 install -r requirements.d/development.txt
    pip3 install -r requirements.d/docs.txt
    pip3 install -r requirements.d/fuse.txt
    pip3 install .

    cd .. || exit 1
    rm -rf borg borg.tar.gz

%runscript

    exec /usr/local/bin/borg "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

