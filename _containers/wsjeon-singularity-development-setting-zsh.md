---
id: 9510
name: "wsjeon/singularity-development-setting"
branch: "master"
tag: "zsh"
commit: "7259e5439bfda7c1ba4af2ef98bf1bf987005653"
version: "d65a1182240c19c04a5a7941d399d5b1"
build_date: "2020-01-15T04:43:51.784Z"
size_mb: 3522
size: 1759768607
sif: "https://datasets.datalad.org/shub/wsjeon/singularity-development-setting/zsh/2020-01-15-7259e543-d65a1182/d65a1182240c19c04a5a7941d399d5b1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/wsjeon/singularity-development-setting/zsh/2020-01-15-7259e543-d65a1182/
recipe: https://datasets.datalad.org/shub/wsjeon/singularity-development-setting/zsh/2020-01-15-7259e543-d65a1182/Singularity
collection: wsjeon/singularity-development-setting
---

# wsjeon/singularity-development-setting:zsh

```bash
$ singularity pull shub://wsjeon/singularity-development-setting:zsh
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
    
    # zsh
    apt-get install -y zsh

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
    export SHELL=/bin/zsh
    
%runscript
    exec /bin/zsh "$@"
```

## Collection

 - Name: [wsjeon/singularity-development-setting](https://github.com/wsjeon/singularity-development-setting)
 - License: None

