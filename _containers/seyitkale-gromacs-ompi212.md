---
id: 3846
name: "seyitkale/gromacs"
branch: "master"
tag: "ompi212"
commit: "0f279d1bf4610b43e57059c22e5691d0e65876a2"
version: "ce4dea134b395768c1c3458157c9b568"
build_date: "2018-08-04T22:20:18.790Z"
size_mb: 1239
size: 436924447
sif: "https://datasets.datalad.org/shub/seyitkale/gromacs/ompi212/2018-08-04-0f279d1b-ce4dea13/ce4dea134b395768c1c3458157c9b568.simg"
url: https://datasets.datalad.org/shub/seyitkale/gromacs/ompi212/2018-08-04-0f279d1b-ce4dea13/
recipe: https://datasets.datalad.org/shub/seyitkale/gromacs/ompi212/2018-08-04-0f279d1b-ce4dea13/Singularity
collection: seyitkale/gromacs
---

# seyitkale/gromacs:ompi212

```bash
$ singularity pull shub://seyitkale/gromacs:ompi212
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install build-essential wget cmake ibutils libibverbs-dev ibverbs-utils  libibverbs1 libsysfs2 libsysfs-dev

    wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.2.tar.bz2
    tar -xjf openmpi-2.1.2.tar.bz2
    cd openmpi-2.1.2 
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

 - Name: [seyitkale/gromacs](https://github.com/seyitkale/gromacs)
 - License: None

