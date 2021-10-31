---
id: 9909
name: "keceli/mpi_benchmark"
branch: "master"
tag: "jdft"
commit: "477ecd3b13ef0e5277afb7f44e0a440945cde771"
version: "9d41038861a27218154aa29565ff5d93"
build_date: "2019-06-19T19:23:11.492Z"
size_mb: 1191
size: 477868063
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/jdft/2019-06-19-477ecd3b-9d410388/9d41038861a27218154aa29565ff5d93.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/mpi_benchmark/jdft/2019-06-19-477ecd3b-9d410388/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/jdft/2019-06-19-477ecd3b-9d410388/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:jdft

```bash
$ singularity pull shub://keceli/mpi_benchmark:jdft
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
   yum install -y cmake
   yum install -y gsl-devel fftw-devel	
   export PATH=$PATH:/mpich-3.2.1/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich-3.2.1/install/lib
   cd /container
   git clone https://github.com/shankar1729/jdftx.git
   cd jdftx
   mkdir -p build; cd build
   cmake ../jdftx
   make
```

## Collection

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

