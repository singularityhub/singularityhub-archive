---
id: 3420
name: "TMCantwell/pulsar_timing_containers"
branch: "master"
tag: "pulsar.v1.1"
commit: "e287f32e207fccb63cb8c2e81515456b39133a3e"
version: "02a73088642add261e89564c5b7088df"
build_date: "2018-07-06T17:40:27.777Z"
size_mb: 2109
size: 675704863
sif: "https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.1/2018-07-06-e287f32e-02a73088/02a73088642add261e89564c5b7088df.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.1/2018-07-06-e287f32e-02a73088/
recipe: https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.1/2018-07-06-e287f32e-02a73088/Singularity
collection: TMCantwell/pulsar_timing_containers
---

# TMCantwell/pulsar_timing_containers:pulsar.v1.1

```bash
$ singularity pull shub://TMCantwell/pulsar_timing_containers:pulsar.v1.1
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
echo 'y' | psrsoft psrchive

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

