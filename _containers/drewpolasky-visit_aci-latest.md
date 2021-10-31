---
id: 9784
name: "drewpolasky/visit_aci"
branch: "master"
tag: "latest"
commit: "b67f49b83698fc24ea9b2cecee86f8a8cc213b56"
version: "a8abffe9b51b0d4113a5a6e1f1dfa0c5"
build_date: "2020-10-27T12:34:36.896Z"
size_mb: 3132
size: 960426015
sif: "https://datasets.datalad.org/shub/drewpolasky/visit_aci/latest/2020-10-27-b67f49b8-a8abffe9/a8abffe9b51b0d4113a5a6e1f1dfa0c5.simg"
url: https://datasets.datalad.org/shub/drewpolasky/visit_aci/latest/2020-10-27-b67f49b8-a8abffe9/
recipe: https://datasets.datalad.org/shub/drewpolasky/visit_aci/latest/2020-10-27-b67f49b8-a8abffe9/Singularity
collection: drewpolasky/visit_aci
---

# drewpolasky/visit_aci:latest

```bash
$ singularity pull shub://drewpolasky/visit_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:latest
IncludeCmd: yes
%setup


%files

%environment
PATH="$PATH:/usr/lib64/openmpi/bin/:/opt/visit/bin/"
LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
MPI_ROOT=/usr/lib64/openmpi/
export PATHi
export LD_LIBRARY_PATH
export MPI_ROOT

%runscript
    exec /opt/visit/bin/visit "$@"

%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum -y update
    yum -y install epel-release \
      terminator \
      centos-release-scl
    yum -y install vte-devel \
      vte291-devel \
      vte-profile \
      devtoolset-8-gcc*
    yum -y groups install "Development Tools"
    yum -y groups install "Base"
    yum -y install git cmake gcc-c++ gcc binutils \
      libX11-devel libXpm-devel libXft-devel libXext-devel \
      gcc-gfortran openssl-devel pcre-devel \
      mesa-libGL-devel mesa-libGLU-devel glew-devel ftgl-devel mysql-devel \
      fftw-devel cfitsio-devel graphviz-devel \
      avahi-compat-libdns_sd-devel libldap-dev python-devel python36-devel python36-pip \
      libxml2-devel gsl-devel \
      cmake3 \
      hdf5-devel \
      patch \
      qt5-qtbase-devel \
      qt5-qtsvg-devel \
      g++ numpy eigen3-devel zlib-devel libqt4-devel libtiff-devel \
      bzip2 ca-certificates \
      libglib2.0-0 libxext6 libsm6 libxrender1 \
      mercurial subversion \
      mesa-libGLU-devel.i686 \
      mesa-libGL-devel.i686 \
      libcanberra-gtk* \
      autoconf \
      Lmod
      
    yum -y update
   
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
    
    # Make symlinks
    ln -s `which qmake-qt5` /usr/local/bin/qmake
    ln -s `which moc-qt5` /usr/local/bin/moc
    ln -s `which rcc-qt5` /usr/local/bin/rcc
    ln -s `which vim` /usr/local/bin/vi
    
    ldconfig -n /usr/lib64/openmpi/lib/
    
    # Install OpenMPI 2.1.6
    cd /tmp/
    wget https://download.open-mpi.org/release/open-mpi/v2.1/openmpi-2.1.6.tar.gz
    tar -xf openmpi-2.1.6.tar.gz
    cd openmpi-2.1.6
    source /opt/rh/devtoolset-8/enable
    ./configure --prefix=/usr/lib64/openmpi/bin/
    make
    make install
    cd ..
    rm -rf openmpi-2.1.6*
    
    # install visit binary
    cd /tmp/
    wget http://portal.nersc.gov/project/visit/releases/3.0.0/visit3_0_0.linux-x86_64-rhel7.tar.gz
    tar -xf visit3_0_0.linux-x86_64-rhel7.tar.gz
    mv visit3_0_0.linux-x86_64 /opt/visit
    #cd visit3_0_0.linux-x86_64
    #wget http://portal.nersc.gov/project/visit/releases/3.0.0b/visit-install3_0_0b
    #chmod 770 visit-install3_0_0b
    #./visit-install3_0_0b 3.0.0 linux-x86_64-rehl7 /usr/local/visit/
```

## Collection

 - Name: [drewpolasky/visit_aci](https://github.com/drewpolasky/visit_aci)
 - License: None

