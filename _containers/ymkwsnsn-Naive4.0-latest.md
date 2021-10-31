---
id: 6057
name: "ymkwsnsn/Naive4.0"
branch: "master"
tag: "latest"
commit: "2523b41e537be4ee5ea5c9fc8e0ff751f2631c06"
version: "c9ad4e758bccd89d48319275844f827e"
build_date: "2018-12-29T03:55:59.411Z"
size_mb: 1144
size: 326610975
sif: "https://datasets.datalad.org/shub/ymkwsnsn/Naive4.0/latest/2018-12-29-2523b41e-c9ad4e75/c9ad4e758bccd89d48319275844f827e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ymkwsnsn/Naive4.0/latest/2018-12-29-2523b41e-c9ad4e75/
recipe: https://datasets.datalad.org/shub/ymkwsnsn/Naive4.0/latest/2018-12-29-2523b41e-c9ad4e75/Singularity
collection: ymkwsnsn/Naive4.0
---

# ymkwsnsn/Naive4.0:latest

```bash
$ singularity pull shub://ymkwsnsn/Naive4.0:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help

%setup

%files

%labels

%environment
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib

%post
    echo "Installing Development Tools YUM group"
    yum -y groupinstall "Development Tools"
    echo "Installing OpenMPI into container..."
    yum -y install wget
    OPENMPI_VERSION=4.0.0
    OPENMPI_NAME=openmpi-${OPENMPI_VERSION}
    wget https://download.open-mpi.org/release/open-mpi/v4.0/${OPENMPI_NAME}.tar.gz
    tar -xvf ${OPENMPI_NAME}.tar.gz
    cd ${OPENMPI_NAME}
    ./configure --prefix=/usr/local
    make all install
    /usr/local/bin/mpicc examples/ring_c.c -o /usr/bin/mpi_ring
    cd /

#osu bench
    OSU_VERSION=5.5
    OSU_NAME=osu-micro-benchmarks-${OSU_VERSION}
    wget http://mvapich.cse.ohio-state.edu/download/mvapich/${OSU_NAME}.tar.gz
    tar -xvf ${OSU_NAME}.tar.gz
    cd ${OSU_NAME}
    ./configure --prefix=/usr/local CC=/usr/local/bin/mpicc CXX=/usr/local/bin/mpicxx
    make
    make install

%runscript
    /usr/local/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw
```

## Collection

 - Name: [ymkwsnsn/Naive4.0](https://github.com/ymkwsnsn/Naive4.0)
 - License: None

