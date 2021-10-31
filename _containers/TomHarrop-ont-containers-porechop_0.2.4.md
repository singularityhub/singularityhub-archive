---
id: 11670
name: "TomHarrop/ont-containers"
branch: "master"
tag: "porechop_0.2.4"
commit: "d9b54eff12e72fd380f530f9e3e2b796b1958e31"
version: "142281752952dd53ceefd1c7af176b43ceb3af061e42d21788380c88cd792fea"
build_date: "2021-04-12T22:53:40.049Z"
size_mb: 313.80859375
size: 329052160
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/porechop_0.2.4/2021-04-12-d9b54eff-14228175/142281752952dd53ceefd1c7af176b43ceb3af061e42d21788380c88cd792fea.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/porechop_0.2.4/2021-04-12-d9b54eff-14228175/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/porechop_0.2.4/2021-04-12-d9b54eff-14228175/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:porechop_0.2.4

```bash
$ singularity pull shub://TomHarrop/ont-containers:porechop_0.2.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.5-buster

%help
    Porechop 0.2.3
    https://github.com/rrwick/Porechop

%labels
    MAINTAINER "Tom Harrop"
    VERSION "Porechop 0.2.3"

%post
    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential

    # install porechop 
    /usr/local/bin/pip3 install setuptools
    /usr/local/bin/pip3 install \
        git+https://github.com/rrwick/Porechop@v0.2.4

%runscript
    exec /usr/local/bin/porechop "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

