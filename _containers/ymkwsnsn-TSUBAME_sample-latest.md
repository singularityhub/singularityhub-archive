---
id: 8963
name: "ymkwsnsn/TSUBAME_sample"
branch: "master"
tag: "latest"
commit: "9b2399460915df2f373a16493616112ff7347e07"
version: "dde13d835df38978dcd359e1c432ec56"
build_date: "2019-09-05T02:07:05.076Z"
size_mb: 1319
size: 395403295
sif: "https://datasets.datalad.org/shub/ymkwsnsn/TSUBAME_sample/latest/2019-09-05-9b239946-dde13d83/dde13d835df38978dcd359e1c432ec56.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ymkwsnsn/TSUBAME_sample/latest/2019-09-05-9b239946-dde13d83/
recipe: https://datasets.datalad.org/shub/ymkwsnsn/TSUBAME_sample/latest/2019-09-05-9b239946-dde13d83/Singularity
collection: ymkwsnsn/TSUBAME_sample
---

# ymkwsnsn/TSUBAME_sample:latest

```bash
$ singularity pull shub://ymkwsnsn/TSUBAME_sample:latest
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
    echo "Installing OFED Infiniband Support"
    yum -y install libibverbs-devel
    yum -y install infiniband-diags perftest qperf opensm
    yum -y install numactl-libs hwloc-libs libfabric libibverbs infinipath-psm
    yum -y groupinstall "Infiniband Support"
    echo "Installing OpenMPI into container..."
    yum -y install wget
    OPENMPI_VERSION=2.1.2
    OPENMPI_NAME=openmpi-${OPENMPI_VERSION}
    wget https://download.open-mpi.org/release/open-mpi/v2.1/${OPENMPI_NAME}.tar.gz
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

 - Name: [ymkwsnsn/TSUBAME_sample](https://github.com/ymkwsnsn/TSUBAME_sample)
 - License: None

