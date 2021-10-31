---
id: 5185
name: "keceli/mpi_benchmark"
branch: "master"
tag: "nwchem_base"
commit: "7eed092e27dcf5f4fef6621fcec4432e00bfa526"
version: "a77629c70eed5622a294565b3088c475"
build_date: "2018-10-09T22:31:42.734Z"
size_mb: 2064
size: 675422239
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/nwchem_base/2018-10-09-7eed092e-a77629c7/a77629c70eed5622a294565b3088c475.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/mpi_benchmark/nwchem_base/2018-10-09-7eed092e-a77629c7/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/nwchem_base/2018-10-09-7eed092e-a77629c7/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:nwchem_base

```bash
$ singularity pull shub://keceli/mpi_benchmark:nwchem_base
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: keceli/mpi_benchmark:theta

%post
   yum update -y
   yum install -y openssh-server openssh-clients python-devel tcsh
   PATH=$PATH:/mpich-3.2.1/install/bin/
   LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   cd /container
   git clone -b release-6-8 https://github.com/nwchemgit/nwchem.git nwchem-6.8
#   cd nwchem-6.8/src 
#   pwd
#   export USE_MPI=y
#   export NWCHEM_TARGET=LINUX64
#   export NWCHEM_TOP=/container/nwchem-6.8
#   export USE_PYTHONCONFIG=y 
#   export PYTHONVERSION=2.7
#   export PYTHONHOME=/usr
#   export BLAS_SIZE=4
#   export USE_64TO32=y 
#   export NWCHEM_MODULES="all python"
#   export USE_INTERNALBLAS=y
#   export BLAS_SIZE=4
#   export FFLAGS='-g -fPIC'
#   make nwchem_config FC=gfortran CC=gcc FFLAGS='-g -fPIC'
#   make 64_to_32
#   make FC=gfortran CC=gcc FFLAGS='-g -fPIC'
#
#%runscript
#   /container/nwchem-6.8/bin/LINUX64/nwchem "$@"
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

