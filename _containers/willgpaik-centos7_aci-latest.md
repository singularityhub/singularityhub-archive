---
id: 11542
name: "willgpaik/centos7_aci"
branch: "master"
tag: "latest"
commit: "c9d45fa61b835a92b8f0aef8b6b12237704a2d4e"
version: "6da9c55e6e4445a46c0d6c013c2fa098"
build_date: "2021-02-08T16:09:51.029Z"
size_mb: 2925.0
size: 1016905759
sif: "https://datasets.datalad.org/shub/willgpaik/centos7_aci/latest/2021-02-08-c9d45fa6-6da9c55e/6da9c55e6e4445a46c0d6c013c2fa098.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/centos7_aci/latest/2021-02-08-c9d45fa6-6da9c55e/
recipe: https://datasets.datalad.org/shub/willgpaik/centos7_aci/latest/2021-02-08-c9d45fa6-6da9c55e/Singularity
collection: willgpaik/centos7_aci
---

# willgpaik/centos7_aci:latest

```bash
$ singularity pull shub://willgpaik/centos7_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7

%setup

%files

%environment
    PATH="/usr/local/bin/:$PATH:/usr/lib64/openmpi/bin/"
    LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
    MPI_ROOT=/usr/lib64/openmpi/
    export PATH
    export LD_LIBRARY_PATH
    export MPI_ROOT
    export BOOST_ROOT=/usr/local/

%runscript

%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum -y update
    yum -y install epel-release \
      centos-release-scl
    yum -y install vte-devel \
      vte291-devel \
      vte-profile \
      devtoolset-7-gcc* \
      devtoolset-8-gcc*
    yum -y groups install "Development Tools"
    yum -y groups install "Base"
    yum -y install git cmake gcc-c++ gcc binutils \
      libX11-devel libXpm-devel libXft-devel libXext-devel \
      gcc-gfortran openssl-devel pcre-devel \
      mesa-libGL-devel mesa-libGLU-devel glew-devel ftgl-devel mysql-devel \
      fftw-devel cfitsio-devel graphviz-devel \
      avahi-compat-libdns_sd-devel openldap-devel \
      libxml2-devel gsl-devel \
      cmake3 \
      hdf5-devel \
      patch \
      qt5-qtbase-devel \
      qt5-qtsvg-devel \
      gcc-g++ numpy eigen3-devel zlib-devel qt-devel libtiff-devel \
      bzip2 ca-certificates \
      glibc-devel libXext-devel libSM-devel libXrender-devel \
      mercurial subversion \
      mesa-libGLU-devel.i686 \
      mesa-libGL-devel.i686 \
      libcanberra-gtk* \
      autoconf \
      Lmod \
      python3-devel \
      lapack-devel \
      blas-devel
      
    yum -y install tix-devel tk-devel tkinter
      
    yum -y install python27-python-devel python27-pip
    # Command below is installing python 3.6.3 while system version is 3.6.8
    # yum -y install rh-python36-python-devel rh-python36-python-pip
    
    yum -y install libxkbcommon-devel libxkbcommon-x11-devel
    yum -y install readline-devel bzip2-devel
    
    yum -y update
    
    source /opt/rh/devtoolset-8/enable
       
#    mkdir -p /storage/home
#    mkdir -p /storage/work
#    mkdir -p /gpfs/scratch
#    mkdir -p /gpfs/group
#    mkdir -p /var/spool/torque
    
    # Make symlinks
    ln -s `which qmake-qt5` /usr/local/bin/qmake
    ln -s `which moc-qt5` /usr/local/bin/moc
    ln -s `which rcc-qt5` /usr/local/bin/rcc
    ln -s `which vim` /usr/local/bin/vi
    
    ldconfig -n /usr/lib64/openmpi/lib/
    
    # Install OpenMPI 4.0.1
#    cd /tmp/
#    wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.1.tar.gz
#    tar -xf openmpi-4.0.1.tar.gz
#    cd openmpi-4.0.1
#    ./configure --prefix=/usr/lib64/openmpi/bin/
#    make -j 2
#    make install
#    cd ..
#    rm -rf openmpi-4.0.1*

    # Install OpenMPI 1.10.1
    cd /tmp/
    wget https://download.open-mpi.org/release/open-mpi/v1.10/openmpi-1.10.1.tar.gz
    tar -xf openmpi-1.10.1.tar.gz
    cd openmpi-1.10.1
    ./configure --prefix=/usr/lib64/openmpi/bin/
    make -j 2
    make install
    cd ..
    rm -rf openmpi-*
    
    # Install Boost 1.74.0
    cd /tmp/
    wget https://dl.bintray.com/boostorg/release/1.74.0/source/boost_1_74_0.tar.gz
    tar -xf boost_1_74_0.tar.gz
    cd boost_1_74_0
    ./bootstrap.sh #--prefix=/usr/local
    ./b2 -j 2 install
    cd ..
    rm -rf boost_*
    
    # Install CMake 3.18.4
    cd /tmp
    wget https://github.com/Kitware/CMake/releases/download/v3.18.4/cmake-3.18.4.tar.gz
    tar -xf cmake-3.18.4.tar.gz
    cd cmake-3.18.4
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf cmake-*
    
    # Install libcurl 7.72.0 (for R 4.0.3)
    cd /tmp
    wget https://curl.haxx.se/download/curl-7.72.0.tar.gz
    tar -xf curl-7.72.0.tar.gz
    cd curl-7.72.0
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf curl-*
    
    # Install xz 5.2.5 (for R 4.0.3)
    cd /tmp
    wget https://tukaani.org/xz/xz-5.2.5.tar.gz
    tar -xf xz-5.2.5.tar.gz
    cd xz-5.2.5
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf xz-*
    
    # Install R 4.0.3
    cd /tmp
    wget https://cran.r-project.org/src/base/R-4/R-4.0.3.tar.gz
    tar -xf R-4.0.3.tar.gz
    cd R-4.0.3
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf R-*
    
    # Install UDUNITS 2.2.26
    cd /tmp
    wget https://www.unidata.ucar.edu/downloads/udunits/udunits-2.2.26.tar.gz
    tar -xf udunits-2.2.26.tar.gz
    cd udunits-2.2.26
    ./configure
    make -j 2 && make install
    cd ..
    rm -rf udunits*
```

## Collection

 - Name: [willgpaik/centos7_aci](https://github.com/willgpaik/centos7_aci)
 - License: None

