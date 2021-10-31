---
id: 4414
name: "dominik-handler/AP_singu"
branch: "master"
tag: "homer-tools"
commit: "d1ba2e26976dcd2b36ab6ebbf27d4d45e875668f"
version: "b3359a0fdb192aef0c94e072beed53b8"
build_date: "2019-09-16T07:41:49.584Z"
size_mb: 1149
size: 386551839
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/homer-tools/2019-09-16-d1ba2e26-b3359a0f/b3359a0fdb192aef0c94e072beed53b8.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/homer-tools/2019-09-16-d1ba2e26-b3359a0f/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/homer-tools/2019-09-16-d1ba2e26-b3359a0f/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:homer-tools

```bash
$ singularity pull shub://dominik-handler/AP_singu:homer-tools
```

## Singularity Recipe

```singularity
#homer-tools in singularity

Bootstrap: docker
From: ubuntu:16.04

%runscript
    "$@"

%post
    apt-get update
    apt-get -y install wget
    apt-get -y install sudo

    cd / && \
    apt-get update -y && \
    apt-get install -y build-essential cmake curl ed gdebi-core git libsm6 libxrender1 libfontconfig1 lsb-release nettle-dev python-setuptools ruby software-properties-common vim wget zlib1g-dev
    mkdir /Software && \
    cd /Software
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /Software/anaconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh
    
    PATH="/Software/anaconda3/bin:$PATH"

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    
    conda install homer

    conda clean --all

    apt-get clean
    
    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2
    mkdir /clustertmp

%environment
    PATH="PATH=/Software/anaconda3/bin:${PATH}"
    export $PATH

%test
  PATH="PATH=/Software/anaconda3/bin:${PATH}"
  export $PATH
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

