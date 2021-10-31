---
id: 6109
name: "mcw-meier-lab/Singularity"
branch: "master"
tag: "afni"
commit: "5e51bb88a5e3a75c894b8dfd0cd8cd1add3af8c0"
version: "c3709bbd68ee9c853d23b8733b3ad245"
build_date: "2019-04-15T15:37:30.911Z"
size_mb: 3652
size: 1546768415
sif: "https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/afni/2019-04-15-5e51bb88-c3709bbd/c3709bbd68ee9c853d23b8733b3ad245.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-meier-lab/Singularity/afni/2019-04-15-5e51bb88-c3709bbd/
recipe: https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/afni/2019-04-15-5e51bb88-c3709bbd/Singularity
collection: mcw-meier-lab/Singularity
---

# mcw-meier-lab/Singularity:afni

```bash
$ singularity pull shub://mcw-meier-lab/Singularity:afni
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
    Maintainer Lezlie Espana
    Version v1.0

%help
    This is a test container for installing the latest version of AFNI.

###################
## GLOBAL ##
###################

%environment
    export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

%runscript
    exec tcsh "${@}"

%post
    #RCC bind points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    #Install necessary packages (used by all apps).
    apt-get update && apt-get install -y \
        git \
        build-essential \
        gcc-multilib \
        curl \
        bc \
        libgomp1 \
        software-properties-common \
        apt-transport-https \
        locales \
        wget \
        tcsh

    #Install AFNI
    add-apt-repository universe
    apt-get update
    apt-get install -y xfonts-base \
        python-qt4 \
        gsl-bin \
        netpbm \
        libjpeg62 \
        xvfb \
        vim \
        xterm \
        evince \
        libglu1-mesa-dev \
        libglw1-mesa \
        libxm4 \
        nautilus \
        openssl \
        libssl-dev \
        libcurl4-openssl-dev

    curl -O https://afni.nimh.nih.gov/pub/dist/bin/linux_ubuntu_16_64/@update.afni.binaries
    tcsh @update.afni.binaries -package linux_ubuntu_16_64 -do_extras -bindir /usr/local/abin
    echo 'setenv PATH /usr/local/abin:$PATH' >> ~/.cshrc
    echo 'export PATH=/usr/local/abin:$PATH' >> ~/.bashrc
    echo 'export PATH=/usr/local/abin:$PATH' >> $SINGULARITY_ENVIRONMENT
    export PATH=/usr/local/abin:$PATH
    cp /usr/local/abin/AFNI.afnirc /usr/local/.afnirc

    #Clean up
    apt-get clean
    rm -rf /var/lib/apt/lists/*

%test
    /usr/local/abin/afni -ver
```

## Collection

 - Name: [mcw-meier-lab/Singularity](https://github.com/mcw-meier-lab/Singularity)
 - License: None

