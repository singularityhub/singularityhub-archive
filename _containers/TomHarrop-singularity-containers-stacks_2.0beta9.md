---
id: 3018
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "stacks_2.0beta9"
commit: "e91e8de45a1b1ad401011a0397ed3b2336fc92b2"
version: "bb2f9183318871f6228b51104056a2d0"
build_date: "2020-03-12T22:41:55.872Z"
size_mb: 469
size: 199196703
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/stacks_2.0beta9/2020-03-12-e91e8de4-bb2f9183/bb2f9183318871f6228b51104056a2d0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/stacks_2.0beta9/2020-03-12-e91e8de4-bb2f9183/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/stacks_2.0beta9/2020-03-12-e91e8de4-bb2f9183/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:stacks_2.0beta9

```bash
$ singularity pull shub://TomHarrop/singularity-containers:stacks_2.0beta9
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential language-pack-en wget zlib1g-dev

%help

    Container for stacks 2.0Beta9
    http://catchenlab.life.illinois.edu/stacks

%labels

    MAINTAINER "Tom Harrop"
    VERSION "stacks 2.0Beta9"

%post

    # install stacks
    wget -O "stacks.tar.gz" \
        http://catchenlab.life.illinois.edu/stacks/source/stacks-2.0Beta9.tar.gz
    mkdir stacks-install
    tar -zxf stacks.tar.gz \
        -C stacks-install \
        --strip-components 1
    cd stacks-install || exit 1
    ./configure \
    && make \
    && make install
    cd .. || exit 1
    rm -rf stacks-install stacks.tar.gz
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

