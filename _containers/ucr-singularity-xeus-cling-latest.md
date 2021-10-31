---
id: 4067
name: "ucr-singularity/xeus-cling"
branch: "master"
tag: "latest"
commit: "b11d88a46aa7ad4abefb57bee0fa458fbfc57995"
version: "b076317e6999502fd28185ce1e977c09"
build_date: "2018-08-20T11:37:23.084Z"
size_mb: 2727
size: 1250566175
sif: "https://datasets.datalad.org/shub/ucr-singularity/xeus-cling/latest/2018-08-20-b11d88a4-b076317e/b076317e6999502fd28185ce1e977c09.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/xeus-cling/latest/2018-08-20-b11d88a4-b076317e/
recipe: https://datasets.datalad.org/shub/ucr-singularity/xeus-cling/latest/2018-08-20-b11d88a4-b076317e/Singularity
collection: ucr-singularity/xeus-cling
---

# ucr-singularity/xeus-cling:latest

```bash
$ singularity pull shub://ucr-singularity/xeus-cling:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%environment

    export PATH=/opt/conda/bin:${PATH}

%post

    apt-get -y update
    apt-get -y install curl bzip2
    
    curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x ~/miniconda.sh
    ~/miniconda.sh -b -p /opt/conda
    rm ~/miniconda.sh
    
    #For integration with JupyterHub  
    /opt/conda/bin/pip install --no-cache-dir ipykernel 
    
    # Installation of Xeus-cling.  It needs gcc7
    apt-get -y install software-properties-common
    add-apt-repository -y ppa:jonathonf/gcc-7.2
    apt-get update -y
    apt-get install -y gcc-7
    # create gcc alias to gcc-7
    cd /usr/bin && ln -sf gcc-7 gcc
    
    /opt/conda/bin/conda install xeus-cling notebook -c QuantStack -c conda-forge
```

## Collection

 - Name: [ucr-singularity/xeus-cling](https://github.com/ucr-singularity/xeus-cling)
 - License: None

