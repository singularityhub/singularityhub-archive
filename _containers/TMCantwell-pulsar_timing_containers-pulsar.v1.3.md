---
id: 4207
name: "TMCantwell/pulsar_timing_containers"
branch: "master"
tag: "pulsar.v1.3"
commit: "9290f898fe3c0791ef2c6c0daf9c7da56dd880b9"
version: "86fb3f48a86e4e6346f156d76fd332a9"
build_date: "2018-08-31T03:21:34.930Z"
size_mb: 2263
size: 705343519
sif: "https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.3/2018-08-31-9290f898-86fb3f48/86fb3f48a86e4e6346f156d76fd332a9.simg"
url: https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.3/2018-08-31-9290f898-86fb3f48/
recipe: https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.3/2018-08-31-9290f898-86fb3f48/Singularity
collection: TMCantwell/pulsar_timing_containers
---

# TMCantwell/pulsar_timing_containers:pulsar.v1.3

```bash
$ singularity pull shub://TMCantwell/pulsar_timing_containers:pulsar.v1.3
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget

%post
yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm
yum -y install build-essential curl git man vim autoconf libtool debootstrap squashfs-tools
yum -y install python2-pip
yum -y install python-devel
yum -y install fftw fftw-devel
yum -y install libpng libpng-devel
yum -y install cfitsio cfitsio-devel
yum -y install pgplot pgplot-devel
yum -y install qt qt-devel
yum -y install java java-devel
yum -y install libxml2 libxml2-devel
wget http://www.pulsarastronomy.net/psrsoft/psrsoft.tar.gz
tar -xzf psrsoft.tar.gz
cd psrsoft/config
cp profile.example profile
cd ..
cd ..
export PATH=/psrsoft/bin:$PATH
echo 'y' | psrsoft sixproc
echo 'y' | psrsoft psrchive
echo 'y' | psrsoft dspsr

%environment
export PATH=/psrsoft/bin:$PATH
export PSRSOFT_USR=/psrsoft/usr
for env in $PSRSOFT_USR/var/psrsoft/env/bash/* ; do . $env ; done
export PATH=$PSRSOFT_USR/bin:$PATH

%runscript
```

## Collection

 - Name: [TMCantwell/pulsar_timing_containers](https://github.com/TMCantwell/pulsar_timing_containers)
 - License: None

