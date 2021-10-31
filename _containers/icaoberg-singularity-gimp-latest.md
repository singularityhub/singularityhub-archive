---
id: 10864
name: "icaoberg/singularity-gimp"
branch: "master"
tag: "latest"
commit: "425907b89d449f8f2be4997b81f3c8e8cba21885"
version: "e087e93567e9ea9faa2567e528ac0b0a"
build_date: "2019-10-08T15:04:58.709Z"
size_mb: 376.0
size: 144687135
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-gimp/latest/2019-10-08-425907b8-e087e935/e087e93567e9ea9faa2567e528ac0b0a.sif"
url: https://datasets.datalad.org/shub/icaoberg/singularity-gimp/latest/2019-10-08-425907b8-e087e935/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-gimp/latest/2019-10-08-425907b8-e087e935/Singularity
collection: icaoberg/singularity-gimp
---

# icaoberg/singularity-gimp:latest

```bash
$ singularity pull shub://icaoberg/singularity-gimp:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%labels
    MAINTAINER icaoberg@cmu.edu
    WEBSITE http://www.cbd.cmu.edu/icaoberg
    VERSION 1.0

%runscript
    exec /bin/bash "$@"

%post
    apt-get update
    echo "Install Gimp"
    apt-get install -y gimp

    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /projects; fi
    if [ ! -d /containers ]; then mkdir /containers; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi

####################################################################################
%appenv gimp
    APP=/usr/bin/gimp
    export APP

%apphelp gimp
    For more information about goto visit https://www.gimp.org/

%apprun gimp
    gimp "$@"
```

## Collection

 - Name: [icaoberg/singularity-gimp](https://github.com/icaoberg/singularity-gimp)
 - License: None

