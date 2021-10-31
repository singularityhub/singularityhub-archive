---
id: 5184
name: "keceli/mpi_benchmark"
branch: "master"
tag: "nwchem"
commit: "338ab5cf048fc34485207f7e21e7499d3c44ab24"
version: "7e7fdcac08c014c21911d0ac1a01989d"
build_date: "2019-06-18T22:10:52.315Z"
size_mb: 2575
size: 782778399
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/nwchem/2019-06-18-338ab5cf-7e7fdcac/7e7fdcac08c014c21911d0ac1a01989d.simg"
url: https://datasets.datalad.org/shub/keceli/mpi_benchmark/nwchem/2019-06-18-338ab5cf-7e7fdcac/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/nwchem/2019-06-18-338ab5cf-7e7fdcac/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:nwchem

```bash
$ singularity pull shub://keceli/mpi_benchmark:nwchem
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: shub://keceli/mpi_benchmark:nwchem_base

%post
#   yum update -y
#   yum install -y openssh-server openssh-clients python-devel tcsh
#   cd /container
#   git clone -b release-6-8 https://github.com/nwchemgit/nwchem.git nwchem-6.8
   cd /container/nwchem-6.8/src 
   pwd
   export PATH=$PATH:/mpich-3.2.1/install/bin/
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   export USE_MPI=y
   export NWCHEM_TARGET=LINUX64
   export NWCHEM_TOP=/container/nwchem-6.8
   export USE_PYTHONCONFIG=y 
   export PYTHONVERSION=2.7
   export PYTHONHOME=/usr
#   export BLAS_SIZE=4
   export USE_64TO32=y 
   export NWCHEM_MODULES="all python"
   export USE_INTERNALBLAS=y
   export FFLAGS='-g -fPIC'
   make nwchem_config FC=gfortran CC=gcc FFLAGS='-g -fPIC'
   make 64_to_32
   make FC=gfortran CC=gcc FFLAGS='-g -fPIC'
#
#%runscript
#   /container/nwchem-6.8/bin/LINUX64/nwchem "$@"
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

