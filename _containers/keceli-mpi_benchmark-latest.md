---
id: 1459
name: "keceli/mpi_benchmark"
branch: "master"
tag: "latest"
commit: "13836f73f38475dd2275620b1701958e3674fea8"
version: "9ddd90dbd2af47f7236834a9123d246a"
build_date: "2019-09-26T18:13:41.966Z"
size_mb: 796
size: 222740511
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/latest/2019-09-26-13836f73-9ddd90db/9ddd90dbd2af47f7236834a9123d246a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/mpi_benchmark/latest/2019-09-26-13836f73-9ddd90db/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/latest/2019-09-26-13836f73-9ddd90db/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:latest

```bash
$ singularity pull shub://keceli/mpi_benchmark:latest
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
   
%runscript
   /container/mpiBench/mpibench
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

