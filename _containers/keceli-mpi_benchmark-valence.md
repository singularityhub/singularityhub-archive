---
id: 5685
name: "keceli/mpi_benchmark"
branch: "master"
tag: "valence"
commit: "338ab5cf048fc34485207f7e21e7499d3c44ab24"
version: "17a074c930dd7c9958d0c62001f3e6d7"
build_date: "2019-06-19T16:10:37.000Z"
size_mb: 1106
size: 328912927
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/valence/2019-06-19-338ab5cf-17a074c9/17a074c930dd7c9958d0c62001f3e6d7.simg"
url: https://datasets.datalad.org/shub/keceli/mpi_benchmark/valence/2019-06-19-338ab5cf-17a074c9/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/valence/2019-06-19-338ab5cf-17a074c9/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:valence

```bash
$ singularity pull shub://keceli/mpi_benchmark:valence
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: keceli/mpi_benchmark:theta

%post
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   yum install -y which
   yum install -y wget
   yum install -y git
   yum install -y ca-certificates
   yum install -y lapack-devel blas-devel
    yum --enablerepo=extras install -y epel-release
    yum install -y wget  vim 
    yum install -y openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools
   yum install -y cmake3
   export PATH=$PATH:/mpich-3.2.1/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   cd /container
   git clone https://github.com/VALENCE-software/VALENCE.git
   cd VALENCE
   git clone https://github.com/simint-chem/simint-generator simint-generator
   cd simint-generator
   mkdir -p build; cd build
   cmake3 ../
   make
   cd ..
   python ./create.py -g build/generator/ostei -l 3 -p 3 outdir
   mkdir -p outdir/build; cd outdir/build
   cmake3 $SIMINT_EXTRA -DSIMINT_C_FLAGS=-g  -DENABLE_FORTRAN=ON -DSIMINT_VECTOR=scalar -DCMAKE_INSTALL_PREFIX=../../../simint ../
   make;make install
   
   cd /container/VALENCE
   sed -i.bak s:/lib/:/lib64/: Makefile
   sed -i.bak s:PRINT_TIMING=no:PRINT_TIMING=yes: Makefile
   SEQUENTIAL=false make
   
%runscript
   /container/VALENCE/bin/valence
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

