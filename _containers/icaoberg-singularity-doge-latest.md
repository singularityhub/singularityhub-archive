---
id: 10862
name: "icaoberg/singularity-doge"
branch: "master"
tag: "latest"
commit: "59769c4a7013a5d9e17a258b151d75f6ad50bac6"
version: "24b83f00aa75a1a98a9d52cb2477c589"
build_date: "2019-09-11T19:20:23.936Z"
size_mb: 395.0
size: 165859359
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-doge/latest/2019-09-11-59769c4a-24b83f00/24b83f00aa75a1a98a9d52cb2477c589.sif"
url: https://datasets.datalad.org/shub/icaoberg/singularity-doge/latest/2019-09-11-59769c4a-24b83f00/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-doge/latest/2019-09-11-59769c4a-24b83f00/Singularity
collection: icaoberg/singularity-doge
---

# icaoberg/singularity-doge:latest

```bash
$ singularity pull shub://icaoberg/singularity-doge:latest
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
    /usr/bin/apt-get update && /usr/bin/apt-get -y upgrade
    /usr/bin/apt-get install -y build-essential

    # Make folders for CBD HPC cluster
    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /containers; fi
    if [ ! -d /containers ]; then mkdir /containers; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi

%appinstall doge
    apt-get -y install python-pip
    pip install doge

%appenv doge
    BEST_APP=doge
    export BEST_APP

%apphelp doge
    For more information visit https://github.com/thiderman/doge

%apprun doge
doge
```

## Collection

 - Name: [icaoberg/singularity-doge](https://github.com/icaoberg/singularity-doge)
 - License: None

