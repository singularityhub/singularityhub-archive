---
id: 983
name: "UNM-CARC/FEniCS"
branch: "master"
tag: "ubuntu"
commit: "1e66c00a279c16cd2a41a28de794cabba78b4cff"
version: "c6aada922224535b742acf1eceece0e3"
build_date: "2017-11-29T00:37:33.977Z"
size_mb: 2421
size: 729284639
sif: "https://datasets.datalad.org/shub/UNM-CARC/FEniCS/ubuntu/2017-11-29-1e66c00a-c6aada92/c6aada922224535b742acf1eceece0e3.simg"
url: https://datasets.datalad.org/shub/UNM-CARC/FEniCS/ubuntu/2017-11-29-1e66c00a-c6aada92/
recipe: https://datasets.datalad.org/shub/UNM-CARC/FEniCS/ubuntu/2017-11-29-1e66c00a-c6aada92/Singularity
collection: UNM-CARC/FEniCS
---

# UNM-CARC/FEniCS:ubuntu

```bash
$ singularity pull shub://UNM-CARC/FEniCS:ubuntu
```

## Singularity Recipe

```singularity
# MPI Ubuntu Package for running FEniCS on CARC Wheeler - derived from initial UUtah 
# CHPC package specification at:
# https://github.com/CHPC-UofU/Singularity-ubuntu-mpi/blob/master/Singularity
# Rebuild trigger edit...
#
Bootstrap: docker
From: ubuntu:17.04

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
    #pip install --no-cache-dir --upgrade pip
    
    # Install other commonly-needed packages
    #pip install --no-cache-dir --upgrade \
    #    future \
    #    matplotlib \
    #    scipy 

    # IB stuff, based on https://community.mellanox.com/docs/DOC-2431
    apt-get install -y dkms infiniband-diags libibverbs* ibacm librdmacm* libmlx4* libmlx5* mstflint libibcm.* libibmad.* libibumad* opensm srptools libmlx4-dev librdmacm-dev rdmacm-utils ibverbs-utils perftest vlan ibutils
    apt-get install -y libtool autoconf automake build-essential ibutils ibverbs-utils rdmacm-utils infiniband-diags perftest librdmacm-dev libibverbs-dev libmlx4-1 numactl libnuma-dev autoconf automake gcc g++ git libtool pkg-config
    apt-get install -y libnl-3-200 libnl-route-3-200 libnl-route-3-dev libnl-utils

    # git, wget, ncurses, ssh (openmpi requires ssh...)
    apt-get install -y git wget ssh

    # fenics
    add-apt-repository ppa:fenics-packages/fenics
    apt-get update
    apt-get -y install python-numpy python-scipy python-matplotlib ipython python-h5py
    apt-get -y --no-install-recommends install fenics
    apt-get -y -o Dpkg::Options::="--force-confold"  dist-upgrade

    # Clean up
    apt-get clean
    rm -rf /tmp/* /var/tmp/*

%environment    
    # path to mlx IB libraries and openmpi in Ubuntu
LD_LIBRARY_PATH=/usr/lib/libibverbs:$LD_LIBRARY_PATH
```

## Collection

 - Name: [UNM-CARC/FEniCS](https://github.com/UNM-CARC/FEniCS)
 - License: None

