---
id: 7353
name: "willgpaik/qt5_aci"
branch: "master"
tag: "latest"
commit: "aa18fef582937d89698a6f986567cbb189ff1361"
version: "db45734bc17eecb7935d65ebb5944c1d"
build_date: "2020-02-07T16:51:07.389Z"
size_mb: 2466
size: 842096671
sif: "https://datasets.datalad.org/shub/willgpaik/qt5_aci/latest/2020-02-07-aa18fef5-db45734b/db45734bc17eecb7935d65ebb5944c1d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/qt5_aci/latest/2020-02-07-aa18fef5-db45734b/
recipe: https://datasets.datalad.org/shub/willgpaik/qt5_aci/latest/2020-02-07-aa18fef5-db45734b/Singularity
collection: willgpaik/qt5_aci
---

# willgpaik/qt5_aci:latest

```bash
$ singularity pull shub://willgpaik/qt5_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum
%setup

%files

%environment 

%runscript


%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum update -y
    yum install -y epel-release
    yum install -y terminator
    yum install -y centos-release-scl
    yum install -y vte-devel
    yum install -y vte291-devel
    yum install -y vte-profile
#    yum -y install devtoolset-7
    yum install -y devtoolset-7-gcc*
    scl enable devtoolset-7 bash
    yum -y groups install "Development Tools"
#    yum -y groups install "GNOME Desktop"
    yum -y groups install "Base"
#    yum -y groups install "X Window System" "Desktop" "Fonts"
    yum -y install git cmake gcc-c++ gcc binutils \
	libX11-devel libXpm-devel libXft-devel libXext-devel
    yum -y install gcc-gfortran openssl-devel pcre-devel \
	mesa-libGL-devel mesa-libGLU-devel glew-devel ftgl-devel mysql-devel \
	fftw-devel cfitsio-devel graphviz-devel \
	avahi-compat-libdns_sd-devel libldap-dev python-devel \
	libxml2-devel gsl-devel
    yum -y install openmpi-devel
    yum -y install cmake3
    yum -y install hdf5-devel
    yum -y install boost-devel
    yum -y install patch
    yum -y install qt5-qtbase-devel
    yum -y install qt5-qtsvg-devel
    yum -y install git g++ numpy eigen3-devel zlib-devel libqt4-devel libgl1-mesa-dev libtiff-devel
    yum -y update
   
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque


    # Make symlink to vi and qmake
    ln -s `which qmake-qt5` /usr/local/bin/qmake
    ln -s `which moc-qt5` /usr/local/bin/moc
    ln -s `which rcc-qt5` /usr/local/bin/rcc
    ln -s `which vim` /usr/local/bin/vi


#    scl enable devtoolset-7 bash
#    echo "scl enable devtoolset-7 bash" >> ~/.bashrc
```

## Collection

 - Name: [willgpaik/qt5_aci](https://github.com/willgpaik/qt5_aci)
 - License: None

