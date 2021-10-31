---
id: 8446
name: "GuanJ-H/octave_icsaci"
branch: "master"
tag: "def"
commit: "5333c4b68ef186c1efe85359aa90e6a1b648186b"
version: "16f7f9fa4c1405b97a3eff9598156740"
build_date: "2019-04-16T15:52:00.111Z"
size_mb: 5734
size: 2136645663
sif: "https://datasets.datalad.org/shub/GuanJ-H/octave_icsaci/def/2019-04-16-5333c4b6-16f7f9fa/16f7f9fa4c1405b97a3eff9598156740.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GuanJ-H/octave_icsaci/def/2019-04-16-5333c4b6-16f7f9fa/
recipe: https://datasets.datalad.org/shub/GuanJ-H/octave_icsaci/def/2019-04-16-5333c4b6-16f7f9fa/Singularity
collection: GuanJ-H/octave_icsaci
---

# GuanJ-H/octave_icsaci:def

```bash
$ singularity pull shub://GuanJ-H/octave_icsaci:def
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
exec /octave-5.1.0/run-octave "$@"

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
#    yum -y update
    yum -y install qtwebkit
    yum -y install qt5-qtbase-devel   
    yum -y install yum-utils
    yum-builddep -y octave
    yum -y install qt-devel mercurial gcc-c++ lapack-devel libtool
    yum -y install epstool transfig pstoedit qscintilla-devel
    yum -y install librsvg2-tools icoutils bzip2-devel libsndfile-devel
    yum -y install portaudio-devel mesa-libOSMesa-devel 
    yum -y install sundials-devel sundials-threads-devel
    yum -y install gnulib-devel
    ln -s /usr/lib64/atlas/libtatlas.so /usr/lib64/atlas/libatlas.so
    yum -y install arpack arpack-devel
    export JAVA_HOME=/usr/lib/jvm/java
    
    
    git clone https://github.com/spack/spack.git
    . spack/share/spack/setup-env.sh
    spack install octave@4.4.1
    
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
    mkdir -p /usr/bin/nvidia-smi
```

## Collection

 - Name: [GuanJ-H/octave_icsaci](https://github.com/GuanJ-H/octave_icsaci)
 - License: None

