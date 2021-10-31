---
id: 14751
name: "MRChemSoft/mrchem-singularity"
branch: "master"
tag: "v1.0.0-nompi"
commit: "460376a54e3cd301509d8b14f57dfd65524c238e"
version: "602386000df1c82207be55527013cb24e63d2fe097d7adff6ad66e3d0561b0b1"
build_date: "2021-04-16T13:06:26.814Z"
size_mb: 88.08203125
size: 92360704
sif: "https://datasets.datalad.org/shub/MRChemSoft/mrchem-singularity/v1.0.0-nompi/2021-04-16-460376a5-60238600/602386000df1c82207be55527013cb24e63d2fe097d7adff6ad66e3d0561b0b1.sif"
url: https://datasets.datalad.org/shub/MRChemSoft/mrchem-singularity/v1.0.0-nompi/2021-04-16-460376a5-60238600/
recipe: https://datasets.datalad.org/shub/MRChemSoft/mrchem-singularity/v1.0.0-nompi/2021-04-16-460376a5-60238600/Singularity
collection: MRChemSoft/mrchem-singularity
---

# MRChemSoft/mrchem-singularity:v1.0.0-nompi

```bash
$ singularity pull shub://MRChemSoft/mrchem-singularity:v1.0.0-nompi
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
    mkdir -p /var/tmp/mrchem-1.0.0/build && cd /var/tmp/mrchem-1.0.0/build && cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mrchem -D CMAKE_BUILD_TYPE=Release -D ENABLE_MPI=OFF -D ENABLE_OPENMP=ON -D ENABLE_ARCH_FLAGS=OFF /var/tmp/mrchem-1.0.0
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
    Description MRChem program (OpenMP version)
    Version v1.0.0


%help
    Shared memory parallel (OpenMP) build of MRChem on a Ubuntu-18.04 base image.

    For a pure OpenMP run (n threads on one process) you can run the container
    just as the regular mrchem executable, here with input file molecule.inp:

        $ export OMP_NUM_THREADS=n
        $ ./<image-name>.sif molecule
```

## Collection

 - Name: [MRChemSoft/mrchem-singularity](https://github.com/MRChemSoft/mrchem-singularity)
 - License: [Mozilla Public License 2.0](https://api.github.com/licenses/mpl-2.0)

