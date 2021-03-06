---
id: 10043
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "octopus_8.4_parallel"
commit: "0dc75873d3c835e21134dd362f1e0d13f0e94d1d"
version: "44ca3ef62088dee4f43d4e34dd9462ce"
build_date: "2019-12-12T06:54:02.870Z"
size_mb: 2648
size: 569024543
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/octopus_8.4_parallel/2019-12-12-0dc75873-44ca3ef6/44ca3ef62088dee4f43d4e34dd9462ce.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/octopus_8.4_parallel/2019-12-12-0dc75873-44ca3ef6/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/octopus_8.4_parallel/2019-12-12-0dc75873-44ca3ef6/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:octopus_8.4_parallel

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:octopus_8.4_parallel
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install wget \
    vim \
    sudo \
    cmake \
    build-essential \
    gfortran \
    liblapack3 \
    liblapack-dev \
    libgsl-dev \
    libfftw3-dev \
    libfftw3-bin \
    libopenmpi1.10 \
    libopenmpi-dev 
# Install libxc from source
    wget --output-document=libxc.tar.gz http://www.tddft.org/programs/octopus/down.php?file=libxc/4.3.4/libxc-4.3.4.tar.gz
    tar xvf libxc.tar.gz
    cd libxc-4.3.4/
    ./configure --enable-mpi --enable-openmp
    make
    make install
# Install octopus from source
    wget --output-document=octopus.tar.gz http://www.tddft.org/programs/octopus/down.php?file=8.4/octopus-8.4.tar.gz
    tar xf octopus.tar.gz
    cd octopus-8.4/
    ./configure --with-libxc-prefix=/opt/etsf/ --enable-mpi --enable-openmp
    make 
    make install
     
#    Install BLAS libraries from source
#    wget http://www.netlib.org/blas/blas-3.8.0.tgz
#    tar xvf blas.tgz
#    cd BLAS-3.8.0/
#    make 
    

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    fortune | cowsay | lolcat
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

