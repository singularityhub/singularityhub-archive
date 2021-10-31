---
id: 7947
name: "colinsauze/torch_singularity"
branch: "master"
tag: "latest"
commit: "793ab8e7c584582260dc1740ea13874f3557b2e2"
version: "78f86bf6c4f1d59b14a940ae10741a7a"
build_date: "2019-03-25T23:16:31.036Z"
size_mb: 1232
size: 422719519
sif: "https://datasets.datalad.org/shub/colinsauze/torch_singularity/latest/2019-03-25-793ab8e7-78f86bf6/78f86bf6c4f1d59b14a940ae10741a7a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/colinsauze/torch_singularity/latest/2019-03-25-793ab8e7-78f86bf6/
recipe: https://datasets.datalad.org/shub/colinsauze/torch_singularity/latest/2019-03-25-793ab8e7-78f86bf6/Singularity
collection: colinsauze/torch_singularity
---

# colinsauze/torch_singularity:latest

```bash
$ singularity pull shub://colinsauze/torch_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:18.04

%help

%labels
    MAINTAINER Colin Sauze

%environment
    #define environment variables here
    
%post  

    apt-get -y update
    apt-get -y upgrade

    #essential utilities
    apt-get -y install git sudo wget build-essential

    cd /opt

    #get torch from source
    git clone https://github.com/torch/distro.git torch --recursive
    cd torch

    #fix broken package being installed by torch
    sed -i 's/sudo apt-get install -y python-software-properties/sudo apt-get install -y software-properties-common/' install-deps

    #install torch
    bash install-deps;
    ./install.sh

    #install the optnet package
    /opt/torch/install/bin/luarocks install optnet
    
%runscript
    #set locale so multiqc doesn't complain
    export LANG=en_US.UTF-8
    
    #running stuff
    /opt/torch/install/bin/th "$@"
```

## Collection

 - Name: [colinsauze/torch_singularity](https://github.com/colinsauze/torch_singularity)
 - License: None

