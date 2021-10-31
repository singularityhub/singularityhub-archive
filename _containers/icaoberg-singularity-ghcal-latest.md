---
id: 7147
name: "icaoberg/singularity-ghcal"
branch: "master"
tag: "latest"
commit: "a8f8978ee249b3210c2c9586f756cc0749f106f6"
version: "e92c60e6f29b937b58dce8df674151ba"
build_date: "2019-03-03T20:55:52.942Z"
size_mb: 464
size: 166240287
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-ghcal/latest/2019-03-03-a8f8978e-e92c60e6/e92c60e6f29b937b58dce8df674151ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/icaoberg/singularity-ghcal/latest/2019-03-03-a8f8978e-e92c60e6/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-ghcal/latest/2019-03-03-a8f8978e-e92c60e6/Singularity
collection: icaoberg/singularity-ghcal
---

# icaoberg/singularity-ghcal:latest

```bash
$ singularity pull shub://icaoberg/singularity-ghcal:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%labels
    AUTHOR icaoberg
    EMAIL icaoberg@cmu.edu
    WEBSITE http://www.cbd.cmu.edu/icaoberg

%runscript
    exec /bin/bash "$@"

%post
    /usr/bin/apt-get update && apt-get install -y --no-install-recommends apt-utils
    /usr/bin/apt-get update --fix-missing
    /usr/bin/apt-get install -y curl nodejs npm
    ln -s /usr/bin/nodejs /usr/bin/node
    npm install --global ghcal

####################################################################################
%appenv ghcal
    APP=/usr/local/bin/
    export APP

%apphelp ghcal
    For more information about goto visit https://github.com/IonicaBizau/ghcal

%apprun ghcal
    ghcal "$@"
```

## Collection

 - Name: [icaoberg/singularity-ghcal](https://github.com/icaoberg/singularity-ghcal)
 - License: None

