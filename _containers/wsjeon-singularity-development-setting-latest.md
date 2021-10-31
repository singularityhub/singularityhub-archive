---
id: 9502
name: "wsjeon/singularity-development-setting"
branch: "master"
tag: "latest"
commit: "5e9a1b09ee851042bc8db6eb9f464a1caac2ee13"
version: "ed43bb3efa19ee10da0c51dfa7be0526"
build_date: "2019-06-03T20:54:49.525Z"
size_mb: 3506
size: 1755193375
sif: "https://datasets.datalad.org/shub/wsjeon/singularity-development-setting/latest/2019-06-03-5e9a1b09-ed43bb3e/ed43bb3efa19ee10da0c51dfa7be0526.simg"
url: https://datasets.datalad.org/shub/wsjeon/singularity-development-setting/latest/2019-06-03-5e9a1b09-ed43bb3e/
recipe: https://datasets.datalad.org/shub/wsjeon/singularity-development-setting/latest/2019-06-03-5e9a1b09-ed43bb3e/Singularity
collection: wsjeon/singularity-development-setting
---

# wsjeon/singularity-development-setting:latest

```bash
$ singularity pull shub://wsjeon/singularity-development-setting:latest
```

## Singularity Recipe

```singularity
# Header
Bootstrap: docker
From: tensorflow/tensorflow:nightly-gpu-py3

# Section
%post
    # neovim
    apt-get install -y software-properties-common
    add-apt-repository ppa:neovim-ppa/stable
    apt-get update
    apt-get install -y neovim
    pip install neovim
    pip install pynvim

    # etc 
    apt-get install -y git
    apt-get install -y wget curl
    apt-get install -y ctags
    
    # ipython
    pip install ipython

    # cluster mounting points
    mkdir /dataset
    mkdir /tmp_log
    mkdir /final_log

%environment
    export SHELL=/bin/bash
```

## Collection

 - Name: [wsjeon/singularity-development-setting](https://github.com/wsjeon/singularity-development-setting)
 - License: None

