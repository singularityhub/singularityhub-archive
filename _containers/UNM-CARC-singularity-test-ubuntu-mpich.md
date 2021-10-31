---
id: 979
name: "UNM-CARC/singularity-test"
branch: "master"
tag: "ubuntu-mpich"
commit: "46b2d0f9ce50e2ad3a7e1b639284e5f93507edce"
version: "02aea91f6d727105188de14170b6a751"
build_date: "2017-11-28T19:11:34.745Z"
size_mb: 1150
size: 365404191
sif: "https://datasets.datalad.org/shub/UNM-CARC/singularity-test/ubuntu-mpich/2017-11-28-46b2d0f9-02aea91f/02aea91f6d727105188de14170b6a751.simg"
url: https://datasets.datalad.org/shub/UNM-CARC/singularity-test/ubuntu-mpich/2017-11-28-46b2d0f9-02aea91f/
recipe: https://datasets.datalad.org/shub/UNM-CARC/singularity-test/ubuntu-mpich/2017-11-28-46b2d0f9-02aea91f/Singularity
collection: UNM-CARC/singularity-test
---

# UNM-CARC/singularity-test:ubuntu-mpich

```bash
$ singularity pull shub://UNM-CARC/singularity-test:ubuntu-mpich
```

## Singularity Recipe

```singularity
# MPI Ubuntu Package for running on CARC Wheeler - derived from initial UUtah CHPC 
# package specification at:
# https://github.com/CHPC-UofU/Singularity-ubuntu-mpi/blob/master/Singularity

Bootstrap: docker
From: ubuntu:latest

%post
	# Wheeler mount points
    mkdir -p /wheeler/scratch
    mkdir -p /nfs/scratch

# Install the necessary packages (from repo)
    apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        curl \
        git \
        libopenblas-dev \
        libcurl4-openssl-dev \
        libfreetype6-dev \
        libpng-dev \
        libzmq3-dev \
        python-pip \
        pkg-config \
        python-dev \
        python-setuptools \
        rsync \
        software-properties-common \
        unzip \
        vim \
        zip \
        zlib1g-dev
    apt-get clean

    # Set up some required environment defaults
    #MC issue with locale (LC_ALL, LANGUAGE), to get it right:
    apt-get install -y language-pack-en
    locale-gen "en_US.UTF-8"
    dpkg-reconfigure locales
    export LANGUAGE="en_US.UTF-8"
    echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

    # Update to the latest pip (newer than repo)
    pip install --no-cache-dir --upgrade pip
    
    # Install other commonly-needed packages
    pip install --no-cache-dir --upgrade \
        future \
        matplotlib \
        scipy 

    # IB stuff, based on https://community.mellanox.com/docs/DOC-2431
    apt-get install -y dkms infiniband-diags libibverbs* ibacm librdmacm* libmlx4* libmlx5* mstflint libibcm.* libibmad.* libibumad* opensm srptools libmlx4-dev librdmacm-dev rdmacm-utils ibverbs-utils perftest vlan ibutils
    apt-get install -y libtool autoconf automake build-essential ibutils ibverbs-utils rdmacm-utils infiniband-diags perftest librdmacm-dev libibverbs-dev libmlx4-1 numactl libnuma-dev autoconf automake gcc g++ git libtool pkg-config
    apt-get install -y libnl-3-200 libnl-route-3-200 libnl-route-3-dev libnl-utils

    # git, wget, ncurses
    apt-get install -y git wget libncurses5-dev 

    # mpich
    apt-get install -y mpich libmpich-dev

%environment    
    # path to mlx IB libraries and openmpi in Ubuntu
LD_LIBRARY_PATH=/usr/lib/libibverbs:$LD_LIBRARY_PATH
```

## Collection

 - Name: [UNM-CARC/singularity-test](https://github.com/UNM-CARC/singularity-test)
 - License: None

