---
id: 12512
name: "ymkwsnsn/shubTest"
branch: "master"
tag: "latest"
commit: "e8b5b6ee1b6282d9d290e4b18e950ff61f7e3a4c"
version: "46cea684533b3f6c414ff29fdc86c7659b25529be308ce4a5e7b132feaa7db11"
build_date: "2020-03-13T05:12:49.459Z"
size_mb: 468.2265625
size: 490971136
sif: "https://datasets.datalad.org/shub/ymkwsnsn/shubTest/latest/2020-03-13-e8b5b6ee-46cea684/46cea684533b3f6c414ff29fdc86c7659b25529be308ce4a5e7b132feaa7db11.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ymkwsnsn/shubTest/latest/2020-03-13-e8b5b6ee-46cea684/
recipe: https://datasets.datalad.org/shub/ymkwsnsn/shubTest/latest/2020-03-13-e8b5b6ee-46cea684/Singularity
collection: ymkwsnsn/shubTest
---

# ymkwsnsn/shubTest:latest

```bash
$ singularity pull shub://ymkwsnsn/shubTest:latest
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
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

%post
    echo "Installing Development Tools YUM group"
    yum -y groupinstall "Development Tools"
    echo "Installing OFED Infiniband Support"
    yum -y install libibverbs-devel
    yum -y install infiniband-diags perftest qperf opensm
    yum -y groupinstall "Infiniband Support"
    echo "Installing OpenMPI into container..."
    yum -y install wget
    wget https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.1.tar.gz
    tar -xvf openmpi-3.1.1.tar.gz
    cd openmpi-3.1.1
    ./configure --prefix=/usr/local --with-platform=contrib/platform/mellanox/optimized
    make all install
    /usr/local/bin/mpicc examples/ring_c.c -o /usr/bin/mpi_ring

#osu bench
     OSU_VERSION=5.4.2
     wget http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-${OSU_VERSION}.tar.gz
     tar -xvf osu-micro-benchmarks-${OSU_VERSION}.tar.gz
     cd osu-micro-benchmarks-${OSU_VERSION}
     ./configure --prefix=/usr/local CC=/usr/local/bin/mpicc CXX=/usr/local/bin/mpicxx
     make
     make install
```

## Collection

 - Name: [ymkwsnsn/shubTest](https://github.com/ymkwsnsn/shubTest)
 - License: None

