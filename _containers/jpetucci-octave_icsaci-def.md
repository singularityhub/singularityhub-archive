---
id: 6220
name: "jpetucci/octave_icsaci"
branch: "master"
tag: "def"
commit: "18251bd529fcb57226392adadaf77abe2d4fd153"
version: "adcbca0772157f3996251ed89ee1fa53"
build_date: "2019-01-14T21:19:29.958Z"
size_mb: 4530
size: 1715027999
sif: "https://datasets.datalad.org/shub/jpetucci/octave_icsaci/def/2019-01-14-18251bd5-adcbca07/adcbca0772157f3996251ed89ee1fa53.simg"
url: https://datasets.datalad.org/shub/jpetucci/octave_icsaci/def/2019-01-14-18251bd5-adcbca07/
recipe: https://datasets.datalad.org/shub/jpetucci/octave_icsaci/def/2019-01-14-18251bd5-adcbca07/Singularity
collection: jpetucci/octave_icsaci
---

# jpetucci/octave_icsaci:def

```bash
$ singularity pull shub://jpetucci/octave_icsaci:def
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
exec /bin/octave "$@"

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
    yum -y install octave
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
    mkdir -p /usr/bin/nvidia-smi
```

## Collection

 - Name: [jpetucci/octave_icsaci](https://github.com/jpetucci/octave_icsaci)
 - License: None

