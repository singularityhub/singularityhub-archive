---
id: 508
name: "michael-tn/gromacs"
branch: "master"
tag: "cent7"
commit: "94cb0aa230ac16c8d3b79c9621e04b3f8435d647"
version: "79802a4b1620f678bf36c4bb5e3d8665"
build_date: "2020-04-08T22:34:08.990Z"
size_mb: 1461
size: 523989023
sif: "https://datasets.datalad.org/shub/michael-tn/gromacs/cent7/2020-04-08-94cb0aa2-79802a4b/79802a4b1620f678bf36c4bb5e3d8665.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/michael-tn/gromacs/cent7/2020-04-08-94cb0aa2-79802a4b/
recipe: https://datasets.datalad.org/shub/michael-tn/gromacs/cent7/2020-04-08-94cb0aa2-79802a4b/Singularity
collection: michael-tn/gromacs
---

# michael-tn/gromacs:cent7

```bash
$ singularity pull shub://michael-tn/gromacs:cent7
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7

%post

# update system
yum install -y epel-release
yum group install -y "Development Tools"

yum install -y \
    tar gzip wget cmake  curl net-tools numactl libmlx4 librdmacm libibverbs libibverbs-utils dapl rdma libsysfs-devel libsysfs rdma-core-devel \


    wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.bz2
    tar -xjf openmpi-3.0.0.tar.bz2
    cd openmpi-3.0.0
    ./configure --prefix=/usr/local --with-hwloc --with-verbs
    make -j4
    make install
    ldconfig

    wget http://ftp.gromacs.org/pub/gromacs/gromacs-5.1.4.tar.gz
    tar zxf gromacs-5.1.4.tar.gz
    cd gromacs-5.1.4
    mkdir build
    cd build
    cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON -DCMAKE_INSTALL_PREFIX=/usr/local
    make
    make check
    make install
    cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON -DGMX_MPI=on -DGMX_MPI=on -DCMAKE_INSTALL_PREFIX=/usr/local
    make
    make check
    make install


%environment
    export LC_ALL=C
    export PATH=/opt//games:$PATH

%runscript
```

## Collection

 - Name: [michael-tn/gromacs](https://github.com/michael-tn/gromacs)
 - License: None

