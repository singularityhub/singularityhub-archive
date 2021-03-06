---
id: 14752
name: "MRChemSoft/mrchem-singularity"
branch: "master"
tag: "v1.0.0-openmpi4.0.5"
commit: "460376a54e3cd301509d8b14f57dfd65524c238e"
version: "e1b3c402f8ce0ad86a21e84d8ba0fcf7f2fe1afe92c79c00606a9a04a630c2fd"
build_date: "2021-04-16T12:59:47.600Z"
size_mb: 117.8359375
size: 123559936
sif: "https://datasets.datalad.org/shub/MRChemSoft/mrchem-singularity/v1.0.0-openmpi4.0.5/2021-04-16-460376a5-e1b3c402/e1b3c402f8ce0ad86a21e84d8ba0fcf7f2fe1afe92c79c00606a9a04a630c2fd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MRChemSoft/mrchem-singularity/v1.0.0-openmpi4.0.5/2021-04-16-460376a5-e1b3c402/
recipe: https://datasets.datalad.org/shub/MRChemSoft/mrchem-singularity/v1.0.0-openmpi4.0.5/2021-04-16-460376a5-e1b3c402/Singularity
collection: MRChemSoft/mrchem-singularity
---

# MRChemSoft/mrchem-singularity:v1.0.0-openmpi4.0.5

```bash
$ singularity pull shub://MRChemSoft/mrchem-singularity:v1.0.0-openmpi4.0.5
```

## Singularity Recipe

```singularity
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

# Mellanox OFED version 5.1-2.3.7.1
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        gnupg \
        wget
    rm -rf /var/lib/apt/lists/*
%post
    wget -qO - https://www.mellanox.com/downloads/ofed/RPM-GPG-KEY-Mellanox | apt-key add -
    mkdir -p /etc/apt/sources.list.d && wget -q -nc --no-check-certificate -P /etc/apt/sources.list.d https://linux.mellanox.com/public/repo/mlnx_ofed/5.1-2.3.7.1/ubuntu18.04/mellanox_mlnx_ofed.list
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ibverbs-providers \
        ibverbs-utils \
        libibmad-dev \
        libibmad5 \
        libibumad-dev \
        libibumad3 \
        libibverbs-dev \
        libibverbs1 \
        librdmacm-dev \
        librdmacm1
    rm -rf /var/lib/apt/lists/*

# UCX version 1.9.0
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
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://github.com/openucx/ucx/releases/download/v1.9.0/ucx-1.9.0.tar.gz
    mkdir -p /var/tmp && tar -x -f /var/tmp/ucx-1.9.0.tar.gz -C /var/tmp -z
    cd /var/tmp/ucx-1.9.0 &&   ./configure --prefix=/usr/local/ucx --disable-assertions --disable-debug --disable-doxygen-doc --disable-logging --disable-params-check --enable-optimizations --with-rdmacm --with-verbs --without-cuda
    make -j$(nproc)
    make -j$(nproc) install
    rm -rf /var/tmp/ucx-1.9.0 /var/tmp/ucx-1.9.0.tar.gz
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

# http://github.com/MRChemSoft/mrchem/archive/v1.0.0.tar.gz
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp http://github.com/MRChemSoft/mrchem/archive/v1.0.0.tar.gz
    mkdir -p /var/tmp && tar -x -f /var/tmp/v1.0.0.tar.gz -C /var/tmp -z
    mkdir -p /var/tmp/mrchem-1.0.0/build && cd /var/tmp/mrchem-1.0.0/build && cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mrchem -D CMAKE_BUILD_TYPE=Release -D ENABLE_MPI=ON -D ENABLE_OPENMP=ON -D ENABLE_ARCH_FLAGS=OFF -D CXX_COMPILER=mpicxx /var/tmp/mrchem-1.0.0
    cmake --build /var/tmp/mrchem-1.0.0/build --target all -- -j$(nproc)
    cmake --build /var/tmp/mrchem-1.0.0/build --target install -- -j$(nproc)
    rm -rf /var/tmp/mrchem-1.0.0 /var/tmp/v1.0.0.tar.gz

BootStrap: docker
From: ubuntu:18.04
%post
    . /.singularity.d/env/10-docker*.sh

# GNU compiler runtime
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libgfortran4 \
        libgomp1
    rm -rf /var/lib/apt/lists/*

# Mellanox OFED version 5.1-2.3.7.1
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        gnupg \
        wget
    rm -rf /var/lib/apt/lists/*
%post
    wget -qO - https://www.mellanox.com/downloads/ofed/RPM-GPG-KEY-Mellanox | apt-key add -
    mkdir -p /etc/apt/sources.list.d && wget -q -nc --no-check-certificate -P /etc/apt/sources.list.d https://linux.mellanox.com/public/repo/mlnx_ofed/5.1-2.3.7.1/ubuntu18.04/mellanox_mlnx_ofed.list
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ibverbs-providers \
        ibverbs-utils \
        libibmad-dev \
        libibmad5 \
        libibumad-dev \
        libibumad3 \
        libibverbs-dev \
        libibverbs1 \
        librdmacm-dev \
        librdmacm1
    rm -rf /var/lib/apt/lists/*

# UCX
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libbinutils
    rm -rf /var/lib/apt/lists/*
%files from build
    /usr/local/ucx /usr/local/ucx
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

# SLURM PMI2
%files from build
    /usr/local/slurm-pmi2 /usr/local/slurm-pmi2

# OpenMPI
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        hwloc \
        openssh-client
    rm -rf /var/lib/apt/lists/*
%files from build
    /usr/local/openmpi /usr/local/openmpi
%environment
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/openmpi/bin:$PATH
%post
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/openmpi/bin:$PATH

# Python
%post
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3
    rm -rf /var/lib/apt/lists/*

# http://github.com/MRChemSoft/mrchem/archive/v1.0.0.tar.gz
%files from build
    /usr/local/mrchem /usr/local/mrchem

%environment
    export PATH=$PATH:/usr/local/mrchem/bin
%post
    export PATH=$PATH:/usr/local/mrchem/bin

%runscript
    exec mrchem "$@"

%labels
    Author Stig Rune Jensen <stig.r.jensen@uit.no>
    Dependency OpenMPI v4.0
    Description MRChem program (MPI+OpenMP version)
    Version v1.0.0


%help
    Hybrid parallel (MPI + OpenMP) build of MRChem using OpenMPI-4.0.5 on a
    Ubuntu-18.04 base image. Requires compatible OpenMPI version on the host.
    The image includes Mellanox OFED, UCX and PMI2 for compatibility with
    common HPC environments with InfiniBand and SLURM.

    For a pure OpenMP run (n threads on one process) you can run the container
    just as the regular mrchem executable, here with input file molecule.inp:

        $ export OMP_NUM_THREADS=n
        $ ./<image-name>.sif molecule

    In order to run with more that one MPI process you must first manually run
    the input parser to obtain the JSON input file. This is done by dry-running
    (--dryrun) the container on the main input file, here called molecule.inp:

        $ ./<image-name>.sif --dryrun molecule
    
    This will produce a new file molecule.json in the current directory which can
    be passed to the mrchem.x program inside the container using the singularity
    exec command:

        $ singularity exec <image-name>.sif mrchem.x mrchem.json

    To run in hybrid parallel (n threads on N processes) you should launch the
    singularity execution with mpirun/srun:

        $ export OMP_NUM_THREADS=n
        $ mpirun -np N singularity exec <image-name>.sif mrchem.x mrchem.json
```

## Collection

 - Name: [MRChemSoft/mrchem-singularity](https://github.com/MRChemSoft/mrchem-singularity)
 - License: [Mozilla Public License 2.0](https://api.github.com/licenses/mpl-2.0)

