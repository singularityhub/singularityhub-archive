---
id: 2815
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "stacks_2.0b"
commit: "72e9da62d9b917f17bf8416229fee6e6ad5a6248"
version: "099f0c7d8c8ff2baf7ad763ad7bcd17b"
build_date: "2019-09-18T01:24:06.358Z"
size_mb: 724
size: 240799775
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/stacks_2.0b/2019-09-18-72e9da62-099f0c7d/099f0c7d8c8ff2baf7ad763ad7bcd17b.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/stacks_2.0b/2019-09-18-72e9da62-099f0c7d/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/stacks_2.0b/2019-09-18-72e9da62-099f0c7d/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:stacks_2.0b

```bash
$ singularity pull shub://TomHarrop/singularity-containers:stacks_2.0b
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential language-pack-en wget zlib1g-dev

%help

    Container for stacks 2.0b
    http://catchenlab.life.illinois.edu/stacks

%labels

    MAINTAINER "Tom Harrop"
    VERSION "stacks 2.0b"

%post

    # install stacks
    wget -O "stacks.tar.gz" \
        http://catchenlab.life.illinois.edu/stacks/source/stacks-2.0b.tar.gz
    mkdir stacks-install
    tar -zxf stacks.tar.gz \
        -C stacks-install \
        --strip-components 1
    cd stacks-install || exit 1
    ./configure \
    && make \
    && make install
    cd ~ || exit 1
    rm -rf stacks-install stacks.tar.gz
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

