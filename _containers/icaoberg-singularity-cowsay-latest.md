---
id: 10861
name: "icaoberg/singularity-cowsay"
branch: "master"
tag: "latest"
commit: "f48ad705699b2d715abdb716874fd935bc719902"
version: "cc1532ab43eb66e866a72e3519dcc95c"
build_date: "2020-11-26T04:56:13.991Z"
size_mb: 167.0
size: 67342367
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-cowsay/latest/2020-11-26-f48ad705-cc1532ab/cc1532ab43eb66e866a72e3519dcc95c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/icaoberg/singularity-cowsay/latest/2020-11-26-f48ad705-cc1532ab/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-cowsay/latest/2020-11-26-f48ad705-cc1532ab/Singularity
collection: icaoberg/singularity-cowsay
---

# icaoberg/singularity-cowsay:latest

```bash
$ singularity pull shub://icaoberg/singularity-cowsay:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%runscript
    exec /bin/bash "$@"

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%post
    /usr/bin/apt-get update

    # Make folders for CBD HPC cluster
    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /projects; fi
    if [ ! -d /containers ]; then mkdir /containers; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi

%appinstall cowsay
    /usr/bin/apt-get -y install cowsay

%appenv cowsay
    APP=cowsay
    export APP

%apphelp cowsay
    For more information visit https://en.wikipedia.org/wiki/Cowsay

%apprun cowsay
    cowsay "$@"
```

## Collection

 - Name: [icaoberg/singularity-cowsay](https://github.com/icaoberg/singularity-cowsay)
 - License: None

