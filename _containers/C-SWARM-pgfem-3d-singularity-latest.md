---
id: 5713
name: "C-SWARM/pgfem-3d-singularity"
branch: "master"
tag: "latest"
commit: "6c51501d8f8fdd4568f9c8eb6f543529ab88e4a0"
version: "535ba2fbe4e3142cecd7a73f3d0ff65f2b08c79c0a52960890db23fccf6d17ba"
build_date: "2020-03-02T14:14:06.878Z"
size_mb: 2251.296875
size: 2360655872
sif: "https://datasets.datalad.org/shub/C-SWARM/pgfem-3d-singularity/latest/2020-03-02-6c51501d-535ba2fb/535ba2fbe4e3142cecd7a73f3d0ff65f2b08c79c0a52960890db23fccf6d17ba.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/C-SWARM/pgfem-3d-singularity/latest/2020-03-02-6c51501d-535ba2fb/
recipe: https://datasets.datalad.org/shub/C-SWARM/pgfem-3d-singularity/latest/2020-03-02-6c51501d-535ba2fb/Singularity
collection: C-SWARM/pgfem-3d-singularity
---

# C-SWARM/pgfem-3d-singularity:latest

```bash
$ singularity pull shub://C-SWARM/pgfem-3d-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: fedora:28

%files

    build.sh /build.sh
    mkl_silent.cfg /mkl_silent.cfg

%environment

    INTEL_MKL=l_mkl_2018.2.199.tgz
    SUITESPARSE=SuiteSparse-4.2.2.tar.gz
    HYPRE=hypre-2.11.2.tar.gz
    PHOTON=photon-1.1.tar.bz2

%post

    dnf -y install curl git paraview cmake cpio libXaw gcc autoconf dh-autoreconf pkgconf gcc-c++ gcc-gfortran glibc glibc-devel libibverbs rdma-core-devel rdma-core infiniband-diags infiniband-diags-devel byacc libibverbs-devel librdmacm-devel wget file unzip

    export INTEL_MKL=l_mkl_2018.2.199.tgz
    export SUITESPARSE=SuiteSparse-4.5.5.tar.gz
    export HYPRE=hypre-2.11.2.tar.gz
    export MVAPICH=mvapich2-2.2.tar.gz
    export PHOTON=photon-1.1.tar.bz2

    # Obtaining necessary software
    curl -O http://kanar.open.sice.indiana.edu/images/$INTEL_MKL
    curl -O http://kanar.open.sice.indiana.edu/images/$PHOTON
    curl -O http://faculty.cse.tamu.edu/davis/SuiteSparse/$SUITESPARSE
    curl -O http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/$MVAPICH
    curl -O https://computing.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods/download/$HYPRE

    # Obtaining PGFem3D and components
    wget -O pgfem-3d.zip https://github.com/C-SWARM/pgfem-3d/archive/develop.zip
    unzip pgfem-3d.zip
    
    mv /pgfem-3d-develop /pgfem_3d

    [ ! -d /ttl ] && git clone -b develop https://github.com/C-SWARM/ttl.git
    [ ! -d /gcm ] && git clone -b develop https://github.com/C-SWARM/gcm.git

    tar -xf $MVAPICH
    cd ${MVAPICH%.tar.gz}
    ./configure --prefix=/mvapich --disable-wrapper-rpath
    make -j 4 install
    PATH=$PATH:/mvapich/bin
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mvapich/lib
    export PATH=$PATH:/mvapich/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mvapich/lib
    cd -

    # Building software components and PGFem3D
    bash /build.sh

    rm $SUITESPARSE $INTEL_MKL $HYPRE $MVAPICH $PHOTON mkl_silent.cfg build.sh pgfem-3d.zip

%runscript

    exec /pgfem_3d/deploy/bin/PGFem3D "$@"

%labels

    Maintainer Cody Kankel <ckankel@nd.edu>, Ezra Kissel <ezkissel@indiana.edu>

    Version 1.0
```

## Collection

 - Name: [C-SWARM/pgfem-3d-singularity](https://github.com/C-SWARM/pgfem-3d-singularity)
 - License: None

