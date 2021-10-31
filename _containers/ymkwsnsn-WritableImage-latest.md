---
id: 6059
name: "ymkwsnsn/WritableImage"
branch: "master"
tag: "latest"
commit: "3aec3c912761d988fd7043691eb6eb5f907e4a00"
version: "da59eb563853d44e0419853046697d42"
build_date: "2018-12-29T03:55:59.401Z"
size_mb: 1097
size: 315572255
sif: "https://datasets.datalad.org/shub/ymkwsnsn/WritableImage/latest/2018-12-29-3aec3c91-da59eb56/da59eb563853d44e0419853046697d42.simg"
url: https://datasets.datalad.org/shub/ymkwsnsn/WritableImage/latest/2018-12-29-3aec3c91-da59eb56/
recipe: https://datasets.datalad.org/shub/ymkwsnsn/WritableImage/latest/2018-12-29-3aec3c91-da59eb56/Singularity
collection: ymkwsnsn/WritableImage
---

# ymkwsnsn/WritableImage:latest

```bash
$ singularity pull shub://ymkwsnsn/WritableImage:latest
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

%post
    echo "Installing Development Tools YUM group"
    yum -y groupinstall "Development Tools"
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

 - Name: [ymkwsnsn/WritableImage](https://github.com/ymkwsnsn/WritableImage)
 - License: None

