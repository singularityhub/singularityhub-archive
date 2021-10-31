---
id: 14337
name: "wilkinson-nu/nuisance_project"
branch: "master"
tag: "34.36_pythia6.def"
commit: "d59a16fc2dd291140cb755be479e0809c1e208f3"
version: "e7805ea89f7aa46028edcccc6b9983dd781913e7757a6522c45e655c020d3d66"
build_date: "2020-09-17T15:35:11.447Z"
size_mb: 600.2890625
size: 629448704
sif: "https://datasets.datalad.org/shub/wilkinson-nu/nuisance_project/34.36_pythia6.def/2020-09-17-d59a16fc-e7805ea8/e7805ea89f7aa46028edcccc6b9983dd781913e7757a6522c45e655c020d3d66.sif"
url: https://datasets.datalad.org/shub/wilkinson-nu/nuisance_project/34.36_pythia6.def/2020-09-17-d59a16fc-e7805ea8/
recipe: https://datasets.datalad.org/shub/wilkinson-nu/nuisance_project/34.36_pythia6.def/2020-09-17-d59a16fc-e7805ea8/Singularity
collection: wilkinson-nu/nuisance_project
---

# wilkinson-nu/nuisance_project:34.36_pythia6.def

```bash
$ singularity pull shub://wilkinson-nu/nuisance_project:34.36_pythia6.def
```

## Singularity Recipe

```singularity
Bootstrap: library
From: centos:7

%post
    yum -y install wget
    yum -y install dnf-plugins-core
    yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    yum -y update

    yum -y group install "Development Tools"

    ## Needed for the old configure ROOT build that for some reason I use :p
    yum -y install file
    yum -y install tar

    ## ROOT deps
    yum -y install git
    yum -y install cmake3
    yum -y install gcc-c++
    yum -y install gcc
    yum -y install binutils 
    yum -y install libX11-devel
    yum -y install libXpm-devel
    yum -y install libXft-devel
    yum -y install libXext-devel
    yum -y install openssl-devel

    ## ROOT optional deps
    yum -y install gcc-gfortran
    yum -y install pcre-devel
    yum -y install mesa-libGL-devel
    yum -y install mesa-libGLU-devel
    yum -y install glew-devel
    yum -y install ftgl-devel
    yum -y install mysql-devel 
    yum -y install fftw-devel
    yum -y install cfitsio-devel
    yum -y install graphviz-devel 
    yum -y install avahi-compat-libdns_sd-devel
    yum -y install openldap-devel
    yum -y install python2-devel
    yum -y install libxml2-devel
    yum -y install gsl-devel

    yum -y install imake
    yum -y install openssh-clients
    yum -y install procmail
    yum -y install patch
    yum -y install make
    yum -y install libdrm-devel
    yum -y install ncurses-devel
    yum -y install openmotif

    ## Required by the packages used downstream (some gotchas here)
    yum -y install which
    yum -y install cmake
    yum -y install ed
    yum -y install automake
    yum -y install perl
    yum -y install libXt-devel
    yum -y install openmotif-devel
    yum -y install csh

    ## For my sanity
    yum -y install emacs

    ## Now the root file

    ## Use 2 cores for the singularity-hub builder
    export NCORES=2
    
    ## Create working directory
    export GEN_DIR=/opt/generators
    mkdir -p $GEN_DIR
    cd $GEN_DIR

    ## Get a copy of ROOT
    wget https://root.cern.ch/download/root_v5.34.36.source.tar.gz
    tar -zxvf root_v5.34.36.source.tar.gz
    rm root_v5.34.36.source.tar.gz

    ## Get PYTHIA6 (with specific placement for NuWro)
    wget --no-check-certificate http://root.cern.ch/download/pythia6.tar.gz
    tar -xzvf pythia6.tar.gz
    rm pythia6.tar.gz
    wget --no-check-certificate http://www.hepforge.org/archive/pythia6/pythia-6.4.28.f.gz
    gunzip pythia-6.4.28.f.gz
    mv pythia-6.4.28.f pythia6/pythia6428.f
    rm pythia6/pythia6416.f

    ## Build PYTHIA6 and copy to where NuWro expects it
    cd pythia6
    ./makePythia6.linuxx8664
    mkdir ${GEN_DIR}/root/lib
    cp ${GEN_DIR}/pythia6/libPythia6.so ${GEN_DIR}/root/lib

    ## Now build root
    cd ${GEN_DIR}/root
    ./configure --with-pythia6-libdir=${GEN_DIR}/root/lib --enable-minuit2 --enable-gsl-shared \
    	    --enable-python --with-python-incdir=/usr/include/python2.7/ --with-python-libdir=/usr/lib64/
    make -j ${NCORES}

%environment
    export ROOTSYS=/opt/generators/root
    source ${ROOTSYS}/bin/thisroot.sh
```

## Collection

 - Name: [wilkinson-nu/nuisance_project](https://github.com/wilkinson-nu/nuisance_project)
 - License: None

