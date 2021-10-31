---
id: 5842
name: "muhammadzaheer/singularity-recipes"
branch: "master"
tag: "steve"
commit: "0a70a67a18dc09c647ad4bce250f83abdcf70a6c"
version: "bd7ec82842213880e7ada24104a8d1e0"
build_date: "2018-12-12T21:53:21.648Z"
size_mb: 1686
size: 705855519
sif: "https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/steve/2018-12-12-0a70a67a-bd7ec828/bd7ec82842213880e7ada24104a8d1e0.simg"
url: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/steve/2018-12-12-0a70a67a-bd7ec828/
recipe: https://datasets.datalad.org/shub/muhammadzaheer/singularity-recipes/steve/2018-12-12-0a70a67a-bd7ec828/Singularity
collection: muhammadzaheer/singularity-recipes
---

# muhammadzaheer/singularity-recipes:steve

```bash
$ singularity pull shub://muhammadzaheer/singularity-recipes:steve
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu:latest

%environment
    export PATH="/usr/local/miniconda2/bin:$PATH"

%post
    apt-get -y update
    apt-get -y install wget bzip2 parallel xvfb libav-tools xorg-dev libsdl2-dev swig cmake build-essential unzip

    # Installing miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh
    bash Miniconda2-latest-Linux-x86_64.sh -b -p /usr/local/miniconda2
    rm Miniconda2-latest-Linux-x86_64.sh

    # Installing numpy, scipy, portalocker
    /usr/local/miniconda2/bin/pip install numpy scipy portalocker

    # Installing tensorflow
    /usr/local/miniconda2/bin/pip install tensorflow==1.6

    # Installing Steve   
    /usr/local/miniconda2/bin/pip install gym[all]==0.9.4
```

## Collection

 - Name: [muhammadzaheer/singularity-recipes](https://github.com/muhammadzaheer/singularity-recipes)
 - License: None

