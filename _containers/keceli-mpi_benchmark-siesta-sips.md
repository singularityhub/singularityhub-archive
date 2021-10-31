---
id: 9384
name: "keceli/mpi_benchmark"
branch: "master"
tag: "siesta-sips"
commit: "a095c35ed0d31d6b8ba7dde833169e8c550ea108"
version: "4ccb3e592bd71d9eecfd931de07221dc"
build_date: "2019-05-29T07:57:53.287Z"
size_mb: 1195
size: 438419487
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/siesta-sips/2019-05-29-a095c35e-4ccb3e59/4ccb3e592bd71d9eecfd931de07221dc.simg"
url: https://datasets.datalad.org/shub/keceli/mpi_benchmark/siesta-sips/2019-05-29-a095c35e-4ccb3e59/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/siesta-sips/2019-05-29-a095c35e-4ccb3e59/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:siesta-sips

```bash
$ singularity pull shub://keceli/mpi_benchmark:siesta-sips
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: keceli/mpi_benchmark:theta
%environment
   export PETSC_DIR=/container/petsc
   export SLEPC_DIR=/container/slepc
   export PETSC_ARCH=arch-container
%post
   export PETSC_DIR=/container/petsc
   export SLEPC_DIR=/container/slepc
   export PETSC_ARCH=arch-container
   export PETSC_VERSION=v3.11.1
   export PATH=$PATH:/mpich-3.2.1/install/bin/
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   yum update -y
   cd /container
   git clone https://bitbucket.org/petsc/petsc petsc
   cd $PETSC_DIR
   git checkout $PETSC_VERSION
   ./configure --with-shared-libraries=1 --with-debugging=1 --download-fblaslapack --with-cc=mpicc --with-cxx=mpicxx --with-fc=mpif90
   make all
   cd /container
   git clone https://bitbucket.org/slepc/slepc slepc
   cd $SLEPC_DIR
   git checkout $PETSC_VERSION
   ./configure 
   make -j 4 all
   cd /container
    git clone https://bitbucket.org/keceli/qetsc.git
    cd qetsc
    make qetsc
    cd ../
    git clone https://bitbucket.org/keceli/siesta-sips.git
    cd siesta-sips
    mkdir $PETSC_ARCH
    cd $PETSC_ARCH
    sh ../Src/obj_setup.sh && \
    ../Src/configure --enable-mpi CC=mpicc FC=mpif90 && \
    echo LIBS='${SLEPC_EPS_LIB} $(SCALAPACK_LIBS) $(BLACS_LIBS) $(LAPACK_LIBS) $(BLAS_LIBS) $(NETCDF_LIBS)' >> arch.make && \
    echo FFLAGS=-g -O2 -I${PETSC_DIR}/include -I${PETSC_DIR}/${PETSC_ARCH}/include -I${SLEPC_DIR}/${PETSC_ARCH}/include -I${SLEPC_DIR}/include >> arch.make && \
    make siesta && \
    mkdir ../Obj && \
    cp siesta ../Obj/
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

