---
id: 10007
name: "Grelot/bioinfo_singularity_recipes"
branch: "master"
tag: "grindermbb"
commit: "7cccd77fc568a429087033060a5d974ea6dd4e16"
version: "4f62a40c87a7cb665a2d816433fb23bb"
build_date: "2020-09-23T14:43:31.978Z"
size_mb: 2189
size: 816168991
sif: "https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/grindermbb/2020-09-23-7cccd77f-4f62a40c/4f62a40c87a7cb665a2d816433fb23bb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Grelot/bioinfo_singularity_recipes/grindermbb/2020-09-23-7cccd77f-4f62a40c/
recipe: https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/grindermbb/2020-09-23-7cccd77f-4f62a40c/Singularity
collection: Grelot/bioinfo_singularity_recipes
---

# Grelot/bioinfo_singularity_recipes:grindermbb

```bash
$ singularity pull shub://Grelot/bioinfo_singularity_recipes:grindermbb
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
      echo "Opening container...ubuntu xenial: grinder, bioperl"

%labels
    MAINTAINER Pierre-Edouard_GUERIN
    INSTITUTE CNRS
    TEAM Biogeographie_Ecologie_Vertebres
    BUILD 1.0
    SINGULARITY_VERSION 2.4.2-dist
    GRINDER 0.5.3
    PERL 5.22.1



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
    apt install wget
    yes | apt-get install autoconf autogen

    ## pigz
    yes | apt install pigz

    ## PERL
    apt-get install -y --force-yes perl
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
    echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen

    ## BIO-PERL
    yes | perl -MCPAN -e 'upgrade' 
    yes | apt-get install bioperl

    ## GRINDER
    git clone -b master https://github.com/zyxue/biogrinder.git
    cd biogrinder
    yes | perl Makefile.PL
    yes | make
    yes | make install
    cd ..
```

## Collection

 - Name: [Grelot/bioinfo_singularity_recipes](https://github.com/Grelot/bioinfo_singularity_recipes)
 - License: None

