---
id: 498
name: "michael-tn/gromacs"
branch: "master"
tag: "ompi212"
commit: "0f279d1bf4610b43e57059c22e5691d0e65876a2"
version: "63d96d3429412123815a98534065c244"
build_date: "2017-10-23T13:06:41.837Z"
size_mb: 1260
size: 435408927
sif: "https://datasets.datalad.org/shub/michael-tn/gromacs/ompi212/2017-10-23-0f279d1b-63d96d34/63d96d3429412123815a98534065c244.simg"
url: https://datasets.datalad.org/shub/michael-tn/gromacs/ompi212/2017-10-23-0f279d1b-63d96d34/
recipe: https://datasets.datalad.org/shub/michael-tn/gromacs/ompi212/2017-10-23-0f279d1b-63d96d34/Singularity
collection: michael-tn/gromacs
---

# michael-tn/gromacs:ompi212

```bash
$ singularity pull shub://michael-tn/gromacs:ompi212
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

 - Name: [michael-tn/gromacs](https://github.com/michael-tn/gromacs)
 - License: None

