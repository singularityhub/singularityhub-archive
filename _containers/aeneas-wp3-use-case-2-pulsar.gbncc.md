---
id: 5485
name: "aeneas-wp3/use-case-2"
branch: "master"
tag: "pulsar.gbncc"
commit: "530f3e5ef2b000b30c6b8def8fb50ab61b83fa3a"
version: "b9c12fbcb88c790247185875a9c239b7"
build_date: "2018-11-06T16:15:10.726Z"
size_mb: 2134
size: 685137951
sif: "https://datasets.datalad.org/shub/aeneas-wp3/use-case-2/pulsar.gbncc/2018-11-06-530f3e5e-b9c12fbc/b9c12fbcb88c790247185875a9c239b7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aeneas-wp3/use-case-2/pulsar.gbncc/2018-11-06-530f3e5e-b9c12fbc/
recipe: https://datasets.datalad.org/shub/aeneas-wp3/use-case-2/pulsar.gbncc/2018-11-06-530f3e5e-b9c12fbc/Singularity
collection: aeneas-wp3/use-case-2
---

# aeneas-wp3/use-case-2:pulsar.gbncc

```bash
$ singularity pull shub://aeneas-wp3/use-case-2:pulsar.gbncc
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

 - Name: [aeneas-wp3/use-case-2](https://github.com/aeneas-wp3/use-case-2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

