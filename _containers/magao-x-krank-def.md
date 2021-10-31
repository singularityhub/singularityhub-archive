---
id: 5833
name: "magao-x/krank"
branch: "master"
tag: "def"
commit: "7d2dc69e4151e4ac4c4ade101c4a8fa354da44ec"
version: "a8bc38c2dbf18745194822cb43412f44"
build_date: "2018-12-10T06:45:59.799Z"
size_mb: 3527
size: 1128603679
sif: "https://datasets.datalad.org/shub/magao-x/krank/def/2018-12-10-7d2dc69e-a8bc38c2/a8bc38c2dbf18745194822cb43412f44.simg"
url: https://datasets.datalad.org/shub/magao-x/krank/def/2018-12-10-7d2dc69e-a8bc38c2/
recipe: https://datasets.datalad.org/shub/magao-x/krank/def/2018-12-10-7d2dc69e-a8bc38c2/Singularity
collection: magao-x/krank
---

# magao-x/krank:def

```bash
$ singularity pull shub://magao-x/krank:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.10@sha256:b4c3fe75b135ca1c26ef6feb8153aade8a31c4e3e763376529c1088de7e973f4
%post
# su root
yum -y update
yum -y install centos-release-scl
yum -y install devtoolset-7
echo "if tty -s; then source /opt/rh/devtoolset-7/enable; fi" | tee /etc/profile.d/devtoolset-7.sh
echo "/usr/local/lib" | tee /etc/ld.so.conf.d/local.conf
yum -y install gsl gsl-devel wget
yum -y clean all

# Install MKL
# http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/14895/l_mkl_2019.1.144.tgz
MKL_VERSION="2019.1.144"
MKL_MAGIC_NUMBER="14895"
MKL_DOWNLOAD="l_mkl_$MKL_VERSION"
source /opt/rh/devtoolset-7/enable && cd /tmp && \
curl -L http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/$MKL_MAGIC_NUMBER/$MKL_DOWNLOAD.tgz | \
tar -xvz && \
cd $MKL_DOWNLOAD && \
sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/g' silent.cfg && \
./install.sh -s silent.cfg && \
cd && \
rm -rf /tmp/*
MKLROOT=/opt/intel/compilers_and_libraries_$MKL_VERSION/linux/mkl
echo "$MKLROOT/lib" > /etc/ld.so.conf.d/mkl.conf
# Install a more up-to-date Boost
BOOST_VERSION="1_68_0"
source /opt/rh/devtoolset-7/enable && cd /tmp && \
curl -L https://dl.bintray.com/boostorg/release/1.68.0/source/boost_$BOOST_VERSION.tar.gz | \
tar xvz && \
cd boost_$BOOST_VERSION && \
./bootstrap.sh --prefix=/usr/local --without-libraries=python && \
./b2 install && \
cd && \
rm -rf /tmp/*
# Build stuff
SOFA_VERSION="2018_0130_C"
EIGEN_VERSION="3.3.4"
LEVMAR_VERSION="2.6"
FFTW_VERSION="3.3.8"
# FFTW
source /opt/rh/devtoolset-7/enable && cd /tmp && curl -L http://fftw.org/fftw-$FFTW_VERSION.tar.gz | \
tar xvz && \
cd fftw-$FFTW_VERSION && \
./configure --prefix=/usr/local --enable-float && \
make && \
make install && \
./configure --prefix=/usr/local --enable-float --enable-threads && \
make && \
make install && \
./configure --prefix=/usr/local && \
make && \
make install && \
./configure --prefix=/usr/local --enable-threads && \
make && \
make install && \
./configure --prefix=/usr/local --enable-long-double && \
make && \
make install && \
./configure --prefix=/usr/local --enable-long-double --enable-threads && \
make && \
make install && \
./configure --prefix=/usr/local --enable-quad-precision && \
make && \
make install && \
./configure --prefix=/usr/local --enable-quad-precision --enable-threads && \
make && \
make install && \
cd && \
rm -rf /tmp/*
# CFITSIO
source /opt/rh/devtoolset-7/enable && cd /tmp && curl -L http://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio_latest.tar.gz | \
tar xvz && \
cd cfitsio && \
./configure --prefix=/usr/local && \
make && \
make install && \
cd && \
rm -rf /tmp/*
# Eigen
source /opt/rh/devtoolset-7/enable && cd /tmp && curl -L http://bitbucket.org/eigen/eigen/get/$EIGEN_VERSION.tar.gz | tar xvz && \
cp -R "$(readlink -e $(find . -type d -name 'eigen-eigen-*' | head -n 1))/Eigen" "/usr/local/include/" && \
chmod -R u=rX,g=rX,o=rX /usr/local/include/Eigen && \
cd && \
rm -rf /tmp/*
# LevMar
source /opt/rh/devtoolset-7/enable && cd /tmp && curl -LA "Mozilla/5.0" http://users.ics.forth.gr/~lourakis/levmar/levmar-$LEVMAR_VERSION.tgz | tar xvz && \
cd ./levmar-$LEVMAR_VERSION && \
make liblevmar.a && \
install liblevmar.a "/usr/local/lib/" && \
cd && \
rm -rf /tmp/*
# SOFA
source /opt/rh/devtoolset-7/enable && cd /tmp && curl http://www.iausofa.org/$SOFA_VERSION/sofa_c-$(echo $SOFA_VERSION | tr -d _C).tar.gz | tar xvz && \
cd sofa/$(echo $SOFA_VERSION | tr -d _C)/c/src && \
make "CFLAGX=-pedantic -Wall -W -O -fPIC" "CFLAGF=-c -pedantic -Wall -W -O -fPIC" && \
make install INSTALL_DIR=/usr/local && \
cd && \
rm -rf /tmp/*
mkdir -p /usr/local/src
# XPA
yum install -y git
source /opt/rh/devtoolset-7/enable && cd /tmp && git clone --depth=1 https://github.com/ericmandel/xpa.git && \
cd xpa && \
./configure --prefix=/usr/local && \
make && \
make install && \
cd && \
rm -rf /tmp/*
# mxlib
source /opt/rh/devtoolset-7/enable && cd /usr/local/src && \
git clone --depth=1 https://github.com/jaredmales/mxlib.git && \
cd mxlib && \
echo "PREFIX = /usr/local" >> local/Common.mk && \
make && \
make install
MXMAKEFILE=/usr/local/src/mxlib/mk/MxApp.mk
# klipReduce
source /opt/rh/devtoolset-7/enable && cd /usr/local/src && \
git clone --depth=1 https://github.com/jaredmales/klipReduce.git && \
cd klipReduce && \
make -B -f $MXMAKEFILE t=klipReduce && \
make -B -f $MXMAKEFILE t=klipReduce install
LD_LIBRARY_PATH="/opt/intel/mkl/lib/intel64_lin:/usr/local/lib:$LD_LIBRARY_PATH"

# UA HPC specific: make directories for mount points
mkdir -p /extra
mkdir -p /xdisk
mkdir -p /rsgrps
mkdir -p /cm/shared
mkdir -p /cm/local

# Docker best practice: run as unprivileged user
useradd -m krank
# su krank
%environment
export MKL_VERSION="2019.1.144"
export MKL_MAGIC_NUMBER="14895"
export MKL_DOWNLOAD="l_mkl_$MKL_VERSION"
export MKLROOT=/opt/intel/compilers_and_libraries_$MKL_VERSION/linux/mkl
export BOOST_VERSION="1_68_0"
export SOFA_VERSION="2018_0130_C"
export EIGEN_VERSION="3.3.4"
export LEVMAR_VERSION="2.6"
export FFTW_VERSION="3.3.8"
export MXMAKEFILE=/usr/local/src/mxlib/mk/MxApp.mk
export LD_LIBRARY_PATH="/opt/intel/mkl/lib/intel64_lin:/usr/local/lib:$LD_LIBRARY_PATH"
%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [magao-x/krank](https://github.com/magao-x/krank)
 - License: None

