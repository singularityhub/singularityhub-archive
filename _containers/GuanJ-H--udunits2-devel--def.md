---
id: 8300
name: "GuanJ-H/-udunits2-devel-"
branch: "master"
tag: "def"
commit: "84c76f9123a210285b5ed7eb48a991ee282198c4"
version: "4a68676734386761cabe44dc13e63020"
build_date: "2019-04-09T19:13:42.415Z"
size_mb: 6239
size: 2215256095
sif: "https://datasets.datalad.org/shub/GuanJ-H/-udunits2-devel-/def/2019-04-09-84c76f91-4a686767/4a68676734386761cabe44dc13e63020.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GuanJ-H/-udunits2-devel-/def/2019-04-09-84c76f91-4a686767/
recipe: https://datasets.datalad.org/shub/GuanJ-H/-udunits2-devel-/def/2019-04-09-84c76f91-4a686767/Singularity
collection: GuanJ-H/-udunits2-devel-
---

# GuanJ-H/-udunits2-devel-:def

```bash
$ singularity pull shub://GuanJ-H/-udunits2-devel-:def
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
# use bash as default shell
SHELL=/bin/bash
export SHELL

%setup

%files


%runscript
exec /bin/R "$@"

%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum -y groups install "Development Tools"
    yum -y groups install "GNOME Desktop"
    yum -y groups install "Base"
    yum -y groups install "X Window System" "Desktop" "Fonts"
    yum -y install qt
    yum -y install mesa-libGLU
    yum -y install SDL SDL-devel
    yum install -y epel-release
    yum install -y libxml2-devel
    yum install -y openssl-devel

    yum -y update
    yum -y install gcc
    yum -y install gcc-c++
    yum -y install libcurl-devel
    yum install -y libjpeg-devel
    yum -y install qtwebkit
    yum -y install qt5-qtbase-devel
    yum -y install gmp-devel
    yum -y install mpfr-devel
    yum -y install mpfr-devel
    yum -y install udunits2-devel 
    wget http://download.osgeo.org/gdal/2.2.3/gdal-2.2.3.tar.gz
    tar xzf gdal-2.2.3.tar.gz
    cd gdal-2.2.3
    ./configure
    make
    make install
    yum -y install R

    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [GuanJ-H/-udunits2-devel-](https://github.com/GuanJ-H/-udunits2-devel-)
 - License: None

