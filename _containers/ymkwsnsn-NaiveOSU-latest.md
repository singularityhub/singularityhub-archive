---
id: 5704
name: "ymkwsnsn/NaiveOSU"
branch: "master"
tag: "latest"
commit: "01b35abe24730815cff1ad4fc00b0ed8b1603986"
version: "4aca0b90401dbdbc60c7b8b2c845c17f"
build_date: "2018-12-19T23:56:58.978Z"
size_mb: 1146
size: 325697567
sif: "https://datasets.datalad.org/shub/ymkwsnsn/NaiveOSU/latest/2018-12-19-01b35abe-4aca0b90/4aca0b90401dbdbc60c7b8b2c845c17f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ymkwsnsn/NaiveOSU/latest/2018-12-19-01b35abe-4aca0b90/
recipe: https://datasets.datalad.org/shub/ymkwsnsn/NaiveOSU/latest/2018-12-19-01b35abe-4aca0b90/Singularity
collection: ymkwsnsn/NaiveOSU
---

# ymkwsnsn/NaiveOSU:latest

```bash
$ singularity pull shub://ymkwsnsn/NaiveOSU:latest
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
    OPENMPI_VERSION=3.1.3
    OPENMPI_NAME=openmpi-${OPENMPI_VERSION}
    wget https://download.open-mpi.org/release/open-mpi/v3.1/${OPENMPI_NAME}.tar.gz
    tar -xvf ${OPENMPI_NAME}.tar.gz
    cd ${OPENMPI_NAME}
    ./configure --prefix=/usr/local
    make all install
    /usr/local/bin/mpicc examples/ring_c.c -o /usr/bin/mpi_ring
    cd /

#osu bench
    OSU_VERSION=5.5
    wget http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-${OSU_VERSION}.tar.gz
    tar -xvf osu-micro-benchmarks-${OSU_VERSION}.tar.gz
    cd osu-micro-benchmarks-${OSU_VERSION}
    ./configure --prefix=/usr/local CC=/usr/local/bin/mpicc CXX=/usr/local/bin/mpicxx
    make
    make install

%runscript
    /usr/local/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw
```

## Collection

 - Name: [ymkwsnsn/NaiveOSU](https://github.com/ymkwsnsn/NaiveOSU)
 - License: None

