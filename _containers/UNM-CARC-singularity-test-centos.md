---
id: 978
name: "UNM-CARC/singularity-test"
branch: "master"
tag: "centos"
commit: "967178ff6e9c002decd66fd6a9187abd673913d6"
version: "0d8336bdfd177fd0282065e2a255c466"
build_date: "2018-09-12T22:22:09.847Z"
size_mb: 824
size: 260489247
sif: "https://datasets.datalad.org/shub/UNM-CARC/singularity-test/centos/2018-09-12-967178ff-0d8336bd/0d8336bdfd177fd0282065e2a255c466.simg"
url: https://datasets.datalad.org/shub/UNM-CARC/singularity-test/centos/2018-09-12-967178ff-0d8336bd/
recipe: https://datasets.datalad.org/shub/UNM-CARC/singularity-test/centos/2018-09-12-967178ff-0d8336bd/Singularity
collection: UNM-CARC/singularity-test
---

# UNM-CARC/singularity-test:centos

```bash
$ singularity pull shub://UNM-CARC/singularity-test:centos
```

## Singularity Recipe

```singularity
# MPI Ubuntu Package for running on CARC Wheeler - derived from initial UUtah CHPC 
# package specification at:
# https://github.com/CHPC-UofU/Singularity-ubuntu-mpi/blob/master/Singularity

Bootstrap: docker
From: centos:latest

%post
    # Wheeler mount points
    mkdir -p /wheeler/scratch
    mkdir -p /nfs/scratch
    yum -y update && yum clean all
    yum groupinstall -y "Development Tools"
    yum install -y \
	which \
        curl \
        git
    yum install -y epel-release
    yum install -y python-pip python-devel
    pip install --upgrade pip
    pip install setuptools

    # Set up some required environment defaults
    #MC issue with locale (LC_ALL, LANGUAGE), to get it right:
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
    yum -y install dapl dapl-utils ibacm infiniband-diags libibverbs libibverbs-devel libibverbs-utils libmlx4 librdmacm librdmacm-utils mstflint opensm-libs perftest qperf rdma
    yum clean all

%environment    
    # path to mlx IB libraries in Ubuntu
LD_LIBRARY_PATH=/usr/lib/libibverbs:$LD_LIBRARY_PATH
```

## Collection

 - Name: [UNM-CARC/singularity-test](https://github.com/UNM-CARC/singularity-test)
 - License: None

