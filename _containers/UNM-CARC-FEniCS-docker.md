---
id: 981
name: "UNM-CARC/FEniCS"
branch: "master"
tag: "docker"
commit: "621954edfe64d10c4e1b95697e9f49e86b12944e"
version: "0a712f6adfdf8d31fb39a292a09c72c2"
build_date: "2017-11-28T19:11:34.789Z"
size_mb: 2134
size: 646811679
sif: "https://datasets.datalad.org/shub/UNM-CARC/FEniCS/docker/2017-11-28-621954ed-0a712f6a/0a712f6adfdf8d31fb39a292a09c72c2.simg"
url: https://datasets.datalad.org/shub/UNM-CARC/FEniCS/docker/2017-11-28-621954ed-0a712f6a/
recipe: https://datasets.datalad.org/shub/UNM-CARC/FEniCS/docker/2017-11-28-621954ed-0a712f6a/Singularity
collection: UNM-CARC/FEniCS
---

# UNM-CARC/FEniCS:docker

```bash
$ singularity pull shub://UNM-CARC/FEniCS:docker
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/fenicsproject/stable:current

%post
    # Wheeler mount points
    mkdir -p /wheeler/scratch
    mkdir -p /nfs/scratch

    # Update apt-get
    apt-get update

    # IB stuff, based on https://community.mellanox.com/docs/DOC-2431
    apt-get install -y dkms infiniband-diags libibverbs* ibacm librdmacm* libmlx4* libmlx5* mstflint libibcm.* libibmad.* libibumad* opensm srptools libmlx4-dev librdmacm-dev rdmacm-utils ibverbs-utils perftest vlan ibutils
    apt-get install -y libtool autoconf automake build-essential ibutils ibverbs-utils rdmacm-utils infiniband-diags perftest librdmacm-dev libibverbs-dev libmlx4-1 numactl libnuma-dev autoconf automake gcc g++ git libtool pkg-config
    apt-get install -y libnl-3-200 libnl-route-3-200 libnl-route-3-dev libnl-utils
    
    # Make sure all of the libraries are indexed right
    ldconfig

#environment
    # path to mlx IB libraries and openmpi in Ubuntu
    export LD_LIBRARY_PATH=/usr/lib/libibverbs:/use/local/lib:$LD_LIBRARY_PATH
    export FENICS_PREFIX=/home/fenics
    export SLEPC_DIR=${FENICS_PREFIX}
    export PETSC_DIR=${FENICS_PREFIX}
    export PYBIND11_DIR=${FENICS_PREFIX}

%runscript
    exec /bin/bash -i
```

## Collection

 - Name: [UNM-CARC/FEniCS](https://github.com/UNM-CARC/FEniCS)
 - License: None

