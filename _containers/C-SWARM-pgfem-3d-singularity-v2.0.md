---
id: 8822
name: "C-SWARM/pgfem-3d-singularity"
branch: "master"
tag: "v2.0"
commit: "b1b89184cce6d28b21bac8904501f2684931cd9a"
version: "3ecd2a38e8cbb8e92843fbf462a90487"
build_date: "2019-05-03T21:23:33.491Z"
size_mb: 5315
size: 2324193311
sif: "https://datasets.datalad.org/shub/C-SWARM/pgfem-3d-singularity/v2.0/2019-05-03-b1b89184-3ecd2a38/3ecd2a38e8cbb8e92843fbf462a90487.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/C-SWARM/pgfem-3d-singularity/v2.0/2019-05-03-b1b89184-3ecd2a38/
recipe: https://datasets.datalad.org/shub/C-SWARM/pgfem-3d-singularity/v2.0/2019-05-03-b1b89184-3ecd2a38/Singularity
collection: C-SWARM/pgfem-3d-singularity
---

# C-SWARM/pgfem-3d-singularity:v2.0

```bash
$ singularity pull shub://C-SWARM/pgfem-3d-singularity:v2.0
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
    curl -Ok https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods/download/$HYPRE

    # Obtaining PGFem3D and components
    [ ! -d /pgfem-3d ] && git clone -b develop https://github.com/C-SWARM/pgfem-3d.git --branch v2.0 --depth 1
    [ ! -d /ttl ] && git clone https://github.com/C-SWARM/ttl.git --branch v0.2 --depth 1
    [ ! -d /gcm ] && git clone -b develop https://github.com/C-SWARM/gcm.git --branch v2.0 --depth 1

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

    rm $SUITESPARSE $INTEL_MKL $HYPRE $MVAPICH $PHOTON mkl_silent.cfg build.sh

%runscript

    exec /pgfem-3d/deploy/bin/PGFem3D "$@"

%labels

    Maintainer Cody Kankel <ckankel@nd.edu>, Ezra Kissel <ezkissel@indiana.edu>

    Version 1.0
```

## Collection

 - Name: [C-SWARM/pgfem-3d-singularity](https://github.com/C-SWARM/pgfem-3d-singularity)
 - License: None

