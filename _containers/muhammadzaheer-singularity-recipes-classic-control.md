---
id: 4186
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "classic-control"
commit: "65f098e43cd93eb9079b6a2bf522ec242817130c"
version: "6667c948514cc45c86af74285115fee9"
build_date: "2018-08-25T18:39:33.440Z"
size_mb: 2054
size: 960811039
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/classic-control/2018-08-25-65f098e4-6667c948/6667c948514cc45c86af74285115fee9.simg"
url: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/classic-control/2018-08-25-65f098e4-6667c948/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/classic-control/2018-08-25-65f098e4-6667c948/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:classic-control

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:classic-control
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu:latest

%environment
    export PATH="/usr/local/miniconda3/bin:$PATH"

%post
    apt-get -y update
    apt-get -y install wget bzip2 parallel
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda3
    rm Miniconda3-latest-Linux-x86_64.sh

    # Installing gym, psutil
    /usr/local/miniconda3/bin/pip install gym
    /usr/local/miniconda3/bin/conda install -c anaconda psutil

    # Installing torch (cpu-version)
    /usr/local/miniconda3/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

