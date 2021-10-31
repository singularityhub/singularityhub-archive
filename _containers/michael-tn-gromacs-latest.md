---
id: 488
name: "michael-tn/gromacs"
branch: "master"
tag: "latest"
commit: "67a754ea4c00348a369c552696e1e970b2d52894"
version: "3c5ea1ea26b3d09927ed444ba109bc47"
build_date: "2020-12-17T15:37:12.676Z"
size_mb: 1289
size: 442200095
sif: "https://datasets.datalad.org/shub/michael-tn/gromacs/latest/2020-12-17-67a754ea-3c5ea1ea/3c5ea1ea26b3d09927ed444ba109bc47.simg"
url: https://datasets.datalad.org/shub/michael-tn/gromacs/latest/2020-12-17-67a754ea-3c5ea1ea/
recipe: https://datasets.datalad.org/shub/michael-tn/gromacs/latest/2020-12-17-67a754ea-3c5ea1ea/Singularity
collection: michael-tn/gromacs
---

# michael-tn/gromacs:latest

```bash
$ singularity pull shub://michael-tn/gromacs:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install build-essential wget cmake libmlx4-1 ibutils libibverbs-dev ibverbs-utils  libibverbs1 libsysfs2 libsysfs-dev

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

