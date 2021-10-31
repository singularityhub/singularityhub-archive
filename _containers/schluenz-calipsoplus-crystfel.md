---
id: 5199
name: "schluenz/calipsoplus"
branch: "master"
tag: "crystfel"
commit: "03cbf8d91e9ba5b90c3c155f86975e5acfb31d3c"
version: "5a74d8aa674c69aac2256f03162732d8"
build_date: "2018-10-11T09:24:02.696Z"
size_mb: 1152
size: 320958495
sif: "https://datasets.datalad.org/shub/schluenz/calipsoplus/crystfel/2018-10-11-03cbf8d9-5a74d8aa/5a74d8aa674c69aac2256f03162732d8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/schluenz/calipsoplus/crystfel/2018-10-11-03cbf8d9-5a74d8aa/
recipe: https://datasets.datalad.org/shub/schluenz/calipsoplus/crystfel/2018-10-11-03cbf8d9-5a74d8aa/Singularity
collection: schluenz/calipsoplus
---

# schluenz/calipsoplus:crystfel

```bash
$ singularity pull shub://schluenz/calipsoplus:crystfel
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/centos

#centos:7

%runscript
	echo "test"

%help
Singularity Container for the CrystFEL package.

# add appdefs for various commands!
%apprun mosflm
   exec /usr/local/crystfel/bin/mosflm

%apprun indexamajig
   exec /usr/local/crystfel/bin/indexamajig

%apprun hdfsee
   exec /usr/local/crystfel/bin/hdfsee

%labels
Version 0.7.0
Packager Calipso+
Author Calipso+

%environment
export CINCL=/usr/local/crystfel/include
export CLIBD=/usr/local/crystfel/data
export CCP4_SCR=/tmp
export PATH=/usr/local/crystfel/bin:$PATH

%post
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y 2>&1 | grep -v "already installed and latest version"
yum install -y gcc gcc-gfortran libstdc++ GConf2 gtk2 libXtst curl hdf5 hdf5-devel libstdc++-devel libstdc++-static libgcc gtk2-devel libpng-devel ncurses-devel fftw-devel cairo-gobject-devel pango-devel gtk-doc gsl-devel bzip2 make cmake gcc gfortran autoconf automake tar unzip 2>&1 | grep -v "already installed and latest version"
#
#  install everything in /usr/local
#
mkdir -p /usr/local/src
pushd /usr/local
#
#  Crystfel itself
#
mkdir -p /usr/local/crystfel/bin
export cv=0.7.0
curl -L http://www.desy.de/~twhite/crystfel/crystfel-$cv.tar.gz  | gzip -dc | tar -xv -C /usr/local
pushd /usr/local/crystfel-$cv
./configure --prefix=/usr/local/crystfel
make
make install
popd
rm -rf /usr/local/crystfel-$cv
#
#  MOSFLM
#
# v7.2.2 has problems. revert back to mosflm 7.2.1!
#curl -s -L http://www.desy.de/~schluenz/crystfel/mosflm.tgz | gzip -dc | tar -xv -C /usr/local/crystfel/bin/
curl -s -L http://www.desy.de/~schluenz/crystfel/mosflm-7.2.1.tgz | gzip -dc | tar -xv -C /usr/local/crystfel/bin/
ln -sf /usr/local/crystfel/bin/mosflm-linux-64-noX11 /usr/local/crystfel/bin/mosflm
ln -sf /usr/local/crystfel/bin/mosflm-linux-64-noX11 /usr/local/crystfel/bin/ipmosflm
#
#  aux files
#
curl -s -L http://www.desy.de/~schluenz/crystfel/default.def -o  /usr/local/crystfel/include/default.def
curl -s -L http://www.desy.de/~schluenz/crystfel/environ.def -o  /usr/local/crystfel/include/environ.def
curl -s -L http://www.desy.de/~schluenz/crystfel/clibd.tgz | gzip -dc | tar -xv -C /usr/local/crystfel/
#
#  Bind DIRs
#
mkdir -p /datadir /procdir
#
#  Clean up
#
rm -rf /usr/local/src
yum remove \*-devel -y
```

## Collection

 - Name: [schluenz/calipsoplus](https://github.com/schluenz/calipsoplus)
 - License: None

