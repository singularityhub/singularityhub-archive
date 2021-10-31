---
id: 8045
name: "dominik-handler/AP_singu"
branch: "master"
tag: "medakagpu"
commit: "131d3c72fe69e01c67a16d9d97950ce977ed0c37"
version: "9fa643e0573a5f41dd40441348d728c7bb7a9998242cd0476176373bbc9b39ba"
build_date: "2020-06-17T11:33:40.119Z"
size_mb: 2131.921875
size: 2235482112
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/medakagpu/2020-06-17-131d3c72-9fa643e0/9fa643e0573a5f41dd40441348d728c7bb7a9998242cd0476176373bbc9b39ba.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/medakagpu/2020-06-17-131d3c72-9fa643e0/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/medakagpu/2020-06-17-131d3c72-9fa643e0/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:medakagpu

```bash
$ singularity pull shub://dominik-handler/AP_singu:medakagpu
```

## Singularity Recipe

```singularity
Bootstrap: docker 
From: nvidia/cuda:10.0-cudnn7-runtime-ubuntu16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  medaka v1.0.0

%post
    set -e

  #fix locale
    apt-get update
    apt-get -y upgrade
    apt-get install -y locales && rm -rf /var/lib/apt/lists/* 
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_COLLATE=C

  #install dependencies
    apt-get update
    apt-get -y install software-properties-common
    add-apt-repository universe
    apt-get update    
    apt-get -y install bzip2 g++ zlib1g-dev libbz2-dev liblzma-dev libffi-dev libncurses5-dev libcurl4-gnutls-dev libssl-dev curl make cmake wget python3-all-dev python3-pip virtualenv git-core

    #@ CUDA=10.0 CUDNN=7.4.1.5-1 /bin/bash
    #@ apt-get -y install --no-install-recommends libcudnn7=7.5.1.10-1+cuda10.0

    #@ python3 -m pip install --upgrade pip
    #@ python3 -m pip  install virtualenv

  #install git-lfs
    cd /tmp
    wget --no-check-certificate --content-disposition https://github.com/git-lfs/git-lfs/releases/download/v2.11.0/git-lfs-linux-amd64-v2.11.0.tar.gz
    tar -zxvf git-lfs-linux-amd64-v2.11.0.tar.gz
    cat install.sh | sed 's/git lfs install/git lfs install --skip-repo/' > install_mod.sh
    chmod 777 install_mod.sh
    ./install_mod.sh
 
  #install medaka
    cd /
    git clone https://github.com/nanoporetech/medaka.git
    cd medaka
    sed -i 's/tar -xvf minimap2-${MINIMAPVER}_x64-linux.tar.bz2/tar -xvf minimap2-${MINIMAPVER}_x64-linux.tar.bz2 --no-same-owner /' Makefile
    sed -i 's/tensorflow/tensorflow-gpu/' requirements.txt
    make install

  #clean up
    apt-get autoremove
    apt-get clean

%environment
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LC_COLLATE=C

  . /medaka/venv/bin/activate

%runscript
  medaka $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

