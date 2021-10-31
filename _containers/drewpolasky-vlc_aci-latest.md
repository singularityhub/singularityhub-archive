---
id: 9689
name: "drewpolasky/vlc_aci"
branch: "master"
tag: "latest"
commit: "adfebed4dd27e61306948ee075c7685ce9867e64"
version: "4dc39c091e3b224e8c1a6b1e12bedc8e"
build_date: "2019-06-08T01:44:30.150Z"
size_mb: 2013
size: 747745311
sif: "https://datasets.datalad.org/shub/drewpolasky/vlc_aci/latest/2019-06-08-adfebed4-4dc39c09/4dc39c091e3b224e8c1a6b1e12bedc8e.simg"
url: https://datasets.datalad.org/shub/drewpolasky/vlc_aci/latest/2019-06-08-adfebed4-4dc39c09/
recipe: https://datasets.datalad.org/shub/drewpolasky/vlc_aci/latest/2019-06-08-adfebed4-4dc39c09/Singularity
collection: drewpolasky/vlc_aci
---

# drewpolasky/vlc_aci:latest

```bash
$ singularity pull shub://drewpolasky/vlc_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:latest
IncludeCmd: yes
%setup

%files

%environment
PATH="$PATH:/usr/lib64/openmpi/bin/"
LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
MPI_ROOT=/usr/lib64/openmpi/
export PATH
export LD_LIBRARY_PATH
export MPI_ROOT

%runscript
    exec /usr/bin/vlc "$@"

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
    
    #rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm
    rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

    yum -y install vlc
```

## Collection

 - Name: [drewpolasky/vlc_aci](https://github.com/drewpolasky/vlc_aci)
 - License: None

