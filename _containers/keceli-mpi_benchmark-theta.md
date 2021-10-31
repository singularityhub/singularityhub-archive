---
id: 5107
name: "keceli/mpi_benchmark"
branch: "master"
tag: "theta"
commit: "22a1e73aa2cd4ce2ecda9d0237b1c11f48733631"
version: "666a7ead1ef9233665568b33c30133e1"
build_date: "2019-10-10T00:23:30.122Z"
size_mb: 796
size: 222756895
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/theta/2019-10-10-22a1e73a-666a7ead/666a7ead1ef9233665568b33c30133e1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/mpi_benchmark/theta/2019-10-10-22a1e73a-666a7ead/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/theta/2019-10-10-22a1e73a-666a7ead/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:theta

```bash
$ singularity pull shub://keceli/mpi_benchmark:theta
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   echo ${SINGULARITY_ROOTFS}
   mkdir ${SINGULARITY_ROOTFS}/container
  
%post
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   yum install -y which
   yum install -y wget
   yum install -y git
   yum install -y ca-certificates
   wget http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xf mpich-3.2.1.tar.gz
   rm -f mpich-3.2.1.tar.gz
   cd mpich-3.2.1
   ./configure --prefix=$PWD/install --disable-wrapper-rpath
   make -j 4 install
   export PATH=$PATH:$PWD/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/install/lib
   cd /container
   git clone https://github.com/LLNL/mpiBench
   cd mpiBench
   mpicc -o mpibench -fPIC mpiBench.c

%environment
   PATH=$PATH:/mpich-3.2.1/install/bin/
   #LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   export PATH
   #export LD_LIBRARY_PATH
   
%runscript
   /container/mpiBench/mpibench
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

