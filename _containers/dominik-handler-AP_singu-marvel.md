---
id: 11746
name: "dominik-handler/AP_singu"
branch: "master"
tag: "marvel"
commit: "0e1e72c7a3f6299df1f9db8101e804cd080c9bf4"
version: "11b6d72f61a758516290ca8d7c04071ceb9a4345c149e7577e39eedbd777bf93"
build_date: "2020-03-04T16:48:03.909Z"
size_mb: 654.953125
size: 686768128
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/marvel/2020-03-04-0e1e72c7-11b6d72f/11b6d72f61a758516290ca8d7c04071ceb9a4345c149e7577e39eedbd777bf93.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/marvel/2020-03-04-0e1e72c7-11b6d72f/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/marvel/2020-03-04-0e1e72c7-11b6d72f/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:marvel

```bash
$ singularity pull shub://dominik-handler/AP_singu:marvel
```

## Singularity Recipe

```singularity
#marvel in singularity

Bootstrap: docker
From: ubuntu:18.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at 
  MARVEL and all other tools required for assembly pipeline

%runscript
    "$@"

%environment
    #!/bin/bash
    export LANG=en_US.UTF-8  
    export LANGUAGE=en_US:en  
    export LC_ALL=C

    export PYTHONPATH=/MARVEL/install/lib.python:$PYTHONPATH
    export PATH=/MARVEL/install/bin:$PATH

%post    
    apt-get update

    #properly install locales
    apt-get -y install locales
    locale-gen en_US.UTF-8
    export LANG=en_US.UTF-8  
    export LANGUAGE=en_US:en  
    export LC_ALL=C

    #install general tools required
    apt-get update
    apt-get -y  install sudo wget build-essential software-properties-common locales libhdf5-dev libgtk-3-dev python3.6 python3-setuptools git-core autoconf parallel zlib1g-dev python3-pip libbz2-dev liblzma-dev
    
    #install networx for MARVEL
    pip3 install networkx

    #install MARVEl
    cd /
    git clone https://github.com/schloi/MARVEL.git
    cd MARVEL
    autoreconf configure.ac
    ./configure --prefix=/MARVEL/install/
    make -j 2
    make install

    #install nanoplot
    pip3 install NanoPlot

    #install filtlong
    cd /
    git clone https://github.com/rrwick/Filtlong.git
    cd Filtlong
    make -j 2    
    cp bin/filtlong /usr/bin/

    #install mawk v1.3.4
    cd /
    wget --quiet  https://invisible-island.net/datafiles/release/mawk.tar.gz
    tar -xzf mawk.tar.gz
    cd mawk-1.3.4-20190203
    ./configure
    make -j 2
    rm -rf /usr/bin/mawk
    cp mawk /usr/bin/
  
%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

