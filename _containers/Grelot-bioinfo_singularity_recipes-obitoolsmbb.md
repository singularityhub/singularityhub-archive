---
id: 9760
name: "Grelot/bioinfo_singularity_recipes"
branch: "master"
tag: "obitoolsmbb"
commit: "17581a046c1dca3e49ef4485cb921586001616d4"
version: "75f895e21b82eb3e0ea01f4fb6eb52e0"
build_date: "2020-12-02T00:17:59.075Z"
size_mb: 972
size: 449441823
sif: "https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/obitoolsmbb/2020-12-02-17581a04-75f895e2/75f895e21b82eb3e0ea01f4fb6eb52e0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Grelot/bioinfo_singularity_recipes/obitoolsmbb/2020-12-02-17581a04-75f895e2/
recipe: https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/obitoolsmbb/2020-12-02-17581a04-75f895e2/Singularity
collection: Grelot/bioinfo_singularity_recipes
---

# Grelot/bioinfo_singularity_recipes:obitoolsmbb

```bash
$ singularity pull shub://Grelot/bioinfo_singularity_recipes:obitoolsmbb
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    echo "This is what happens when you run the container..."

%labels
    MAINTAINER Pierre-Edouard_GUERIN
    INSTITUTE CNRS
    TEAM Biogeographie_Ecologie_Vertebres
    BUILD 1.0
    SINGULARITY_VERSION 2.4.2-dist
    Obitools 1.0
    ecoPCR 1.0.1
    ecoPrimers 0.5

%post   
    mv /etc/apt/sources.list /etc/apt/sources.list.bak

    echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
    deb-src http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
    deb http://us.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
    deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
    deb http://us.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted universe multiverse
    deb http://us.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
    deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
    deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
    deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted universe multiverse
    deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse" >> /etc/apt/sources.list


    ##  MBB config
    mkdir -p /share/apps/bin
    mkdir /share/apps/lib
    mkdir /share/apps/gridengine
    mkdir /share/bio
    mkdir -p /opt/gridengine
    mkdir -p /export/scrach
    mkdir -p /usr/lib64
    /usr/sbin/groupadd --system --gid 400 sge
    /usr/sbin/useradd --system --uid 400 --gid 400 -c GridEngine --shell /bin/true --home /opt/gridengine sge
    ln -s /bin/bash /bin/mbb_bash
    ln -s /bin/bash /bin/isem_bash

    ## git, make, wget
    apt-get -y --force-yes update
    apt-get -y --force-yes install build-essential
    apt-get -y --force-yes install git
    yes | apt install wget
    yes | apt-get install autoconf autogen

    ## zlib
    yes | apt install zlib1g-dev
  
    ## OBITOOLS v1
    yes | apt-get install python-pip
    yes | pip install --upgrade pip==9.0.3
    pip install -U virtualenv
    pip install -U sphinx
    pip install -U cython
    pip install OBITools
    
    ## ecoPRIMERS
    wget https://git.metabarcoding.org/obitools/ecoprimers/uploads/40f0fe1896a15ca9ad29835f93893464/ecoPrimers.tar.gz
    tar -zxvf ecoPrimers.tar.gz
    cd ecoprimers/src/
    yes | make
    cp ecoPrimers /usr/local/bin/ecoPrimers
    cd ../../
    
    ## ecoPCR
    wget https://git.metabarcoding.org/obitools/ecopcr/uploads/aa3828c196570ea156ce6d4baac22b10/ecopcr-1.0.1.tar.gz
    tar -zxvf ecopcr-*.tar.gz
    cd ecopcr/src/
    yes | make
    cp ecoPCR /usr/local/bin/ecoPCR
    cd ../../
```

## Collection

 - Name: [Grelot/bioinfo_singularity_recipes](https://github.com/Grelot/bioinfo_singularity_recipes)
 - License: None

