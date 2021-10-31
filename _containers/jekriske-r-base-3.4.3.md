---
id: 1011
name: "jekriske/r-base"
branch: "master"
tag: "3.4.3"
commit: "d3420e7e2ae989257d82a74106af816b8187e273"
version: "796c71822cd8d135d97b44f7719c60cf"
build_date: "2021-02-10T13:38:30.300Z"
size_mb: 826
size: 305799199
sif: "https://datasets.datalad.org/shub/jekriske/r-base/3.4.3/2021-02-10-d3420e7e-796c7182/796c71822cd8d135d97b44f7719c60cf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jekriske/r-base/3.4.3/2021-02-10-d3420e7e-796c7182/
recipe: https://datasets.datalad.org/shub/jekriske/r-base/3.4.3/2021-02-10-d3420e7e-796c7182/Singularity
collection: jekriske/r-base
---

# jekriske/r-base:3.4.3

```bash
$ singularity pull shub://jekriske/r-base:3.4.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7
IncludeCmd: no

%labels
  Maintainer Jeff Kriske
  Version v0.0.2
  R_Version 3.4.3

%environment
  source /opt/rh/devtoolset-7/enable

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"

%post
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export R_VERSION="R-3.4.3"
  yum update -y
  cd /tmp
  curl -O http://ftp.ussg.iu.edu/CRAN/src/base/R-3/${R_VERSION}.tar.gz
  tar xf ${R_VERSION}.tar.gz && rm ${R_VERSION}.tar.gz
  yum install -y centos-release-scl epel-release
  yum install -y autoconf \
                 bison \
                 blas \
                 bzip2 bzip2-devel \
                 cairo-devel \
                 devtoolset-7-gcc \
                 devtoolset-7-gcc-c++ \
                 devtoolset-7-gcc-gfortran \
                 flex \
                 ftp \
                 gettext \
                 git \
                 java-1.8.0-openjdk-devel \
                 lapack \
                 libcurl-devel \
                 libicu-devel \
                 libjpeg-turbo libjpeg-devel \
                 libpng libpng-devel \
                 libtiff libtiff-devel \
                 libXt-devel \
                 m4 \
                 make \
                 ncurses-devel \
                 openssl-devel \
                 pcre pcre-devel \
                 readline-devel \
                 tcl-devel \
                 tk-devel \
                 unzip \
                 vim-minimal \
                 wget \
                 which \
                 xz xz-devel \
                 zlib zlib-devel

  cd /tmp/${R_VERSION}
  dbus-uuidgen >/etc/machine-id
  source /opt/rh/devtoolset-7/enable
  ./configure --enable-R-shlib
  make -j4
  make install
  make install-libR
  echo /opt/rh/devtoolset-7/enable >> /tmp/${R_VERSION}/etc/ldpaths
  make check
  echo /opt/rh/devtoolset-7/enable >> /usr/local/lib64/R/etc/ldpaths
  yum clean all && rm -rf /var/cache/yum
  rm -rf /tmp/${R_VERSION}
```

## Collection

 - Name: [jekriske/r-base](https://github.com/jekriske/r-base)
 - License: None

