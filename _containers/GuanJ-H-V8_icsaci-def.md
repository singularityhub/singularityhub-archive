---
id: 8657
name: "GuanJ-H/V8_icsaci"
branch: "master"
tag: "def"
commit: "de685a33fdd2ef2c47ca3bc93503d41ea9e63649"
version: "dc7e478f269a5a57a8cd0efdd3ae31f1"
build_date: "2019-04-25T15:46:05.843Z"
size_mb: 4930
size: 1920606239
sif: "https://datasets.datalad.org/shub/GuanJ-H/V8_icsaci/def/2019-04-25-de685a33-dc7e478f/dc7e478f269a5a57a8cd0efdd3ae31f1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GuanJ-H/V8_icsaci/def/2019-04-25-de685a33-dc7e478f/
recipe: https://datasets.datalad.org/shub/GuanJ-H/V8_icsaci/def/2019-04-25-de685a33-dc7e478f/Singularity
collection: GuanJ-H/V8_icsaci
---

# GuanJ-H/V8_icsaci:def

```bash
$ singularity pull shub://GuanJ-H/V8_icsaci:def
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
exec R "$@"

%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum -y update
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
    yum -y install v8-devel
    yum -y install R
    
    
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
    mkdir -p /usr/bin/nvidia-smi
```

## Collection

 - Name: [GuanJ-H/V8_icsaci](https://github.com/GuanJ-H/V8_icsaci)
 - License: None

