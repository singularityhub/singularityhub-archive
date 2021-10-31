---
id: 5009
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "swarm_2.2.2"
commit: "0e9f326c433705e2465ee2d06a247f01e646d43e"
version: "43ac7b2ccf469a227e9fcbf3b6a8472e"
build_date: "2018-09-27T01:15:52.398Z"
size_mb: 327
size: 125153311
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/swarm_2.2.2/2018-09-27-0e9f326c-43ac7b2c/43ac7b2ccf469a227e9fcbf3b6a8472e.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/swarm_2.2.2/2018-09-27-0e9f326c-43ac7b2c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/swarm_2.2.2/2018-09-27-0e9f326c-43ac7b2c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:swarm_2.2.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:swarm_2.2.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    Swarm 2.2.2
    https://github.com/torognes/swarm

%labels

    MAINTAINER "Tom Harrop"
    VERSION "Swarm 2.2.2"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        wget

    # install swarm
    wget -O "swarm.tar.gz" \
        --no-check-certificate \
        https://github.com/torognes/swarm/archive/v2.2.2.tar.gz
    mkdir swarm
    tar -zxf swarm.tar.gz \
        -C swarm \
        --strip-components 1
    cd swarm/src || exit 1
    make
    cd .. || exit 1
    mv bin/swarm /usr/local/bin/
    cd .. || exit 1
    rm -rf swarm swarm.tar.gz

%runscript

    exec /usr/local/bin/swarm "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

