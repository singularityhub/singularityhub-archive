---
id: 5112
name: "keceli/mpi_benchmark"
branch: "master"
tag: "petsc"
commit: "5b5a90ff266d5c217834d366717e15b5107ba021"
version: "a97559c2b5efaacdc42012f3dcee9025"
build_date: "2019-08-06T19:09:57.149Z"
size_mb: 1198
size: 439578655
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/petsc/2019-08-06-5b5a90ff-a97559c2/a97559c2b5efaacdc42012f3dcee9025.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/mpi_benchmark/petsc/2019-08-06-5b5a90ff-a97559c2/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/petsc/2019-08-06-5b5a90ff-a97559c2/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:petsc

```bash
$ singularity pull shub://keceli/mpi_benchmark:petsc
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: keceli/mpi_benchmark:theta

%post
   export PATH=$PATH:/mpich-3.2.1/install/bin/
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   export PETSC_DIR=/container/petsc
   export PETSC_ARCH=arch-container
   export PETSC_VERSION=v3.11.1
   yum update -y
   yum install -y openssh-server openssh-clients python-devel 
   cd /container
   git clone https://bitbucket.org/petsc/petsc petsc
   cd $PETSC_DIR
   git checkout $PETSC_VERSION
   ./configure --with-shared-libraries=1 --with-debugging=1 --download-fblaslapack --with-cc=mpicc --with-cxx=mpicxx --with-fc=mpif90
   make all
   cd ./src/ksp/ksp/examples/tutorials
   make ex5
   
%environment
   export PETSC_DIR=/container/petsc
   export PETSC_ARCH=arch-container
     
%runscript
   /petsc/src/ksp/ksp/examples/tutorials/ex5
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

