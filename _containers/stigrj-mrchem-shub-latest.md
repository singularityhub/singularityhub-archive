---
id: 14697
name: "stigrj/mrchem-shub"
branch: "master"
tag: "latest"
commit: "f8a3f655e1404890b99fe2eac2523467ae900479"
version: "216450bb618871ab8bea1879309fc977"
build_date: "2020-10-22T11:17:02.695Z"
size_mb: 1285.0
size: 569163807
sif: "https://datasets.datalad.org/shub/stigrj/mrchem-shub/latest/2020-10-22-f8a3f655-216450bb/216450bb618871ab8bea1879309fc977.sif"
url: https://datasets.datalad.org/shub/stigrj/mrchem-shub/latest/2020-10-22-f8a3f655-216450bb/
recipe: https://datasets.datalad.org/shub/stigrj/mrchem-shub/latest/2020-10-22-f8a3f655-216450bb/Singularity
collection: stigrj/mrchem-shub
---

# stigrj/mrchem-shub:latest

```bash
$ singularity pull shub://stigrj/mrchem-shub:latest
```

## Singularity Recipe

```singularity
# 
# MRChem OpenMPI-OFED image
# 
# Contents:
#   Ubuntu 18.04
#   GNU compilers (upstream)
#   OFED
#   OpenMPI
#   PMI2 (SLURM)
#   UCX
# 
# Building:
#   1. Docker to Singularity
#      $ hpccm --recipe mpi_bandwidth.py > Dockerfile
#      $ sudo docker build -t mpi_bw -f Dockerfile .
#      $ singularity build mpi_bw.sif docker-daemon://mpi_bw:latest
# 
#   2. Singularity
#      $ hpccm --recipe mpi_bandwidth.py --format singularity --singularity-version=3.2 > Singularity.def
#      $ sudo singularity build mpi_bw.sif Singularity.def
# 
# Running with Singularity:
#   1. Using a compatible host MPI runtime
#      $ singularity run mrchem-fram.sif mrchem --dryrun molecule.inp
#      $ mpirun -map-by ppr:1:numa -bind-to numa singularity run mrchem-fram.sif mrchem.x molecule.json >molecule.out
# 
#   2. Using SLURM srun
#      $ singularity run mrchem-fram.sif mrchem --dryrun molecule.inp
#      $ srun singularity run mrchem-fram.sif mrchem.x molecule.json >molecule.out
# 

# NOTE: this definition file depends on features only available in
# Singularity 3.2 and later.
BootStrap: docker
From: ubuntu:18.04
Stage: build
%post
    . /.singularity.d/env/10-docker*.sh

# GNU compiler
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        g++ \
        gcc \
        gfortran
    rm -rf /var/lib/apt/lists/*

# OFED
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends -t bionic \
        dapl2-utils \
        ibutils \
        ibverbs-providers \
        ibverbs-utils \
        infiniband-diags \
        libdapl-dev \
        libdapl2 \
        libibmad-dev \
        libibmad5 \
        libibverbs-dev \
        libibverbs1 \
        librdmacm-dev \
        librdmacm1 \
        rdmacm-utils
    rm -rf /var/lib/apt/lists/*

# UCX version 1.7.0
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        binutils-dev \
        file \
        libnuma-dev \
        make \
        wget
    rm -rf /var/lib/apt/lists/*
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://github.com/openucx/ucx/releases/download/v1.7.0/ucx-1.7.0.tar.gz
    mkdir -p /var/tmp && tar -x -f /var/tmp/ucx-1.7.0.tar.gz -C /var/tmp -z
    cd /var/tmp/ucx-1.7.0 &&   ./configure --prefix=/usr/local/ucx --disable-assertions --disable-debug --disable-doxygen-doc --disable-logging --disable-params-check --enable-optimizations --with-rdmacm --with-verbs --without-cuda
    make -j$(nproc)
    make -j$(nproc) install
    rm -rf /var/tmp/ucx-1.7.0 /var/tmp/ucx-1.7.0.tar.gz
%environment
    export CPATH=/usr/local/ucx/include:$CPATH
    export LD_LIBRARY_PATH=/usr/local/ucx/lib:$LD_LIBRARY_PATH
    export LIBRARY_PATH=/usr/local/ucx/lib:$LIBRARY_PATH
    export PATH=/usr/local/ucx/bin:$PATH
%post
    export CPATH=/usr/local/ucx/include:$CPATH
    export LD_LIBRARY_PATH=/usr/local/ucx/lib:$LD_LIBRARY_PATH
    export LIBRARY_PATH=/usr/local/ucx/lib:$LIBRARY_PATH
    export PATH=/usr/local/ucx/bin:$PATH

# SLURM PMI2 version 20.02.5
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bzip2 \
        file \
        make \
        perl \
        tar \
        wget
    rm -rf /var/lib/apt/lists/*
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://download.schedmd.com/slurm/slurm-20.02.5.tar.bz2
    mkdir -p /var/tmp && tar -x -f /var/tmp/slurm-20.02.5.tar.bz2 -C /var/tmp -j
    cd /var/tmp/slurm-20.02.5 &&   ./configure --prefix=/usr/local/slurm-pmi2
    cd /var/tmp/slurm-20.02.5
    make -C contribs/pmi2 install
    rm -rf /var/tmp/slurm-20.02.5 /var/tmp/slurm-20.02.5.tar.bz2

# OpenMPI version 4.0.5
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bzip2 \
        file \
        hwloc \
        libnuma-dev \
        make \
        openssh-client \
        perl \
        tar \
        wget
    rm -rf /var/lib/apt/lists/*
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://www.open-mpi.org/software/ompi/v4.0/downloads/openmpi-4.0.5.tar.bz2
    mkdir -p /var/tmp && tar -x -f /var/tmp/openmpi-4.0.5.tar.bz2 -C /var/tmp -j
    cd /var/tmp/openmpi-4.0.5 &&  CC=gcc CXX=g++ F77=gfortran F90=gfortran FC=gfortran ./configure --prefix=/usr/local/openmpi --disable-getpwuid --enable-orterun-prefix-by-default --with-pmi=/usr/local/slurm-pmi2 --with-ucx=/usr/local/ucx --without-cuda --without-verbs
    make -j$(nproc)
    make -j$(nproc) install
    rm -rf /var/tmp/openmpi-4.0.5 /var/tmp/openmpi-4.0.5.tar.bz2
%environment
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/openmpi/bin:$PATH
%post
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/openmpi/bin:$PATH

# CMake version 3.16.3
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        make \
        wget
    rm -rf /var/lib/apt/lists/*
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://cmake.org/files/v3.16/cmake-3.16.3-Linux-x86_64.sh
    mkdir -p /usr/local
    /bin/sh /var/tmp/cmake-3.16.3-Linux-x86_64.sh --prefix=/usr/local --skip-license
    rm -rf /var/tmp/cmake-3.16.3-Linux-x86_64.sh
%environment
    export PATH=/usr/local/bin:$PATH
%post
    export PATH=/usr/local/bin:$PATH

# Python
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3
    rm -rf /var/lib/apt/lists/*

%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        patch
    rm -rf /var/lib/apt/lists/*

%post
    export LC_ALL=C.UTF-8

    apt --yes update && \
    apt --yes upgrade && \
    apt --yes install git \
                      g++ \
                      gcc \
                      wget \
                      python3

    export MRCHEM_VERSION=1.0
    export MRCHEM_DIR=/usr/local
    export MRCHEM_SRC=/src/mrchem

    # Download MRChem
    mkdir -p ${MRCHEM_SRC} && \
    cd ${MRCHEM_SRC} && \
    git clone --branch 'master' \
              --depth 1 \
              https://github.com/stigrj/mrchem.git \
              mrchem-${MRCHEM_VERSION}

    # Install MRChem
    cd mrchem-${MRCHEM_VERSION}
    python3 setup --prefix=${MRCHEM_DIR} --omp --mpi --cxx=mpicxx build && \
    cd build && \
    make -j2 && \
    make install
```

## Collection

 - Name: [stigrj/mrchem-shub](https://github.com/stigrj/mrchem-shub)
 - License: None

