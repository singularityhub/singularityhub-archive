---
id: 8069
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "octopus_8.4"
commit: "014f1bca71459f9e865e2fe9c77bcb67526fd503"
version: "13aa48e18db5716487ffeec49723692b"
build_date: "2019-04-05T06:18:03.583Z"
size_mb: 1214
size: 385277983
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/octopus_8.4/2019-04-05-014f1bca-13aa48e1/13aa48e18db5716487ffeec49723692b.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/octopus_8.4/2019-04-05-014f1bca-13aa48e1/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/octopus_8.4/2019-04-05-014f1bca-13aa48e1/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:octopus_8.4

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:octopus_8.4
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
    ./configure
    make
    make install
# Install octopus from source
    wget --output-document=octopus.tar.gz http://www.tddft.org/programs/octopus/down.php?file=8.4/octopus-8.4.tar.gz
    tar xf octopus.tar.gz
    cd octopus-8.4/
    ./configure --with-libxc-prefix=/opt/etsf/
    
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

