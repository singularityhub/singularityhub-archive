---
id: 2584
name: "keceli/mpi_benchmark"
branch: "master"
tag: "mpich"
commit: "48bb3daf97693115b06509635ba94ee874293120"
version: "022332d3f00495a8f8084ff019cee9e4"
build_date: "2018-04-19T08:45:22.818Z"
size_mb: 787
size: 221769759
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/mpich/2018-04-19-48bb3daf-022332d3/022332d3f00495a8f8084ff019cee9e4.simg"
url: https://datasets.datalad.org/shub/keceli/mpi_benchmark/mpich/2018-04-19-48bb3daf-022332d3/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/mpich/2018-04-19-48bb3daf-022332d3/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:mpich

```bash
$ singularity pull shub://keceli/mpi_benchmark:mpich
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

