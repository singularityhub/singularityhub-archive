---
id: 10872
name: "icaoberg/singularity-gnuplot"
branch: "master"
tag: "latest"
commit: "c0845cf383a5d2d2dde3cd500237f42a2abf8415"
version: "773f3f76d70a2ebd58b4d71e511d79c9"
build_date: "2021-04-02T16:40:28.717Z"
size_mb: 532.0
size: 196919327
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-gnuplot/latest/2021-04-02-c0845cf3-773f3f76/773f3f76d70a2ebd58b4d71e511d79c9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/icaoberg/singularity-gnuplot/latest/2021-04-02-c0845cf3-773f3f76/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-gnuplot/latest/2021-04-02-c0845cf3-773f3f76/Singularity
collection: icaoberg/singularity-gnuplot
---

# icaoberg/singularity-gnuplot:latest

```bash
$ singularity pull shub://icaoberg/singularity-gnuplot:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:latest

IncludeCmd: yes

%labels
    MAINTAINER icaoberg@alumni.cmu.edu
    WEBSITE http://linus.cbd.cs.cmu.edu
    VERSION 1.0

%runscript
    exec /bin/bash "$@"

%post
    /usr/bin/apt-get update 
    /usr/bin/apt-get install -y gnuplot

    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /projects; fi
    if [ ! -d /containers ]; then mkdir /containers; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi
    if [ ! -d /webservers/pfenningweb ]; then mkdir -p /webservers/pfenningweb; fi

####################################################################################
%appenv gnuplot
    APP=/path/to/gnuplot
    export APP

%apphelp gnuplot
    For more information about goto visit http://www.gnuplot.info

%apprun gnuplot
    gnuplot "$@"
```

## Collection

 - Name: [icaoberg/singularity-gnuplot](https://github.com/icaoberg/singularity-gnuplot)
 - License: None

