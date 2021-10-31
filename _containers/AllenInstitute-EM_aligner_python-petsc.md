---
id: 9000
name: "AllenInstitute/EM_aligner_python"
branch: "catch_up_distributed"
tag: "petsc"
commit: "bfde0506b21d0e5f0bea086d56c9d44a6520e684"
version: "cf2cbf2ac9cf9367754469183e2f65ee"
build_date: "2019-05-10T10:48:47.606Z"
size_mb: 2071
size: 586702879
sif: "https://datasets.datalad.org/shub/AllenInstitute/EM_aligner_python/petsc/2019-05-10-bfde0506-cf2cbf2a/cf2cbf2ac9cf9367754469183e2f65ee.simg"
url: https://datasets.datalad.org/shub/AllenInstitute/EM_aligner_python/petsc/2019-05-10-bfde0506-cf2cbf2a/
recipe: https://datasets.datalad.org/shub/AllenInstitute/EM_aligner_python/petsc/2019-05-10-bfde0506-cf2cbf2a/Singularity
collection: AllenInstitute/EM_aligner_python
---

# AllenInstitute/EM_aligner_python:petsc

```bash
$ singularity pull shub://AllenInstitute/EM_aligner_python:petsc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stable

%help
Debian container with configured and installed petsc.

%labels
    Author Dan Kapner (danielk@alleninstitute.org)
    PETSc_version 3.11.1

%post
    # requirements for petsc and the petsc build
    apt-get update
    apt-get upgrade -y
    apt-get install git vim wget gcc g++ gfortran make cmake        \
                    curl python pkg-config build-essential          \
                    valgrind openssh-client openssh-server          \
                    libopenblas-dev libopenblas-base bison flex -y

    # we need these variables right now
    export PETSC_VERSION=petsc-3.11.1
    export PETSC_ARCH=arch-linux2-c
    export PETSC_DIR=/${PETSC_VERSION}

    # we will reuse these at runtime and child containers
    echo "export PETSC_DIR=$PETSC_DIR" >> /sourceme
    echo "export PATH=$PETSC_DIR/$PETSC_ARCH/bin:$PATH" >> /sourceme
    echo "export LD_LIBRARY_PATH=$PETSC_DIR/$PETSC_ARCH/lib" >> /sourceme

    # download the petsc version we want and extract it
    wget http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/${PETSC_VERSION}.tar.gz
    tar -xzf ${PETSC_VERSION}.tar.gz
    cd ${PETSC_DIR}
    
    # configure the build
    ./configure --with-blaslapack-lib=-lopenblas \
                --download-mpich                 \
                --download-hypre                 \
                --download-superlu_dist          \
                --download-parmetis              \
                --download-metis                 \
                --download-ptscotch              \
                --download-hdf5                  \
                --download-pastix                \
                --with-cxx-dialect=C++11         \
                --with-debugging=0               \
                --with-64-bit-indices=1          \
                --with-debugging=no              \
                COPTFLAGS=-O3                    \
                CXXOPTFLAGS=-O3                  \
                FOPTFLAGS=-O3

    # build and test 
    make all test
```

## Collection

 - Name: [AllenInstitute/EM_aligner_python](https://github.com/AllenInstitute/EM_aligner_python)
 - License: [Other](None)

