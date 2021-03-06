---
id: 1577
name: "jekriske/r-base"
branch: "master"
tag: "3.4.2"
commit: "580191cbbf25063b7bdc872b64260a5654235018"
version: "2fc299bce93bf0b2d1445164dd659c05"
build_date: "2018-02-02T13:14:51.906Z"
size_mb: 826
size: 305799199
sif: "https://datasets.datalad.org/shub/jekriske/r-base/3.4.2/2018-02-02-580191cb-2fc299bc/2fc299bce93bf0b2d1445164dd659c05.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jekriske/r-base/3.4.2/2018-02-02-580191cb-2fc299bc/
recipe: https://datasets.datalad.org/shub/jekriske/r-base/3.4.2/2018-02-02-580191cb-2fc299bc/Singularity
collection: jekriske/r-base
---

# jekriske/r-base:3.4.2

```bash
$ singularity pull shub://jekriske/r-base:3.4.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7
IncludeCmd: no

%labels
  Maintainer Jeff Kriske
  Version v0.0.1
  R_Version 3.4.2

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
  export R_VERSION="R-3.4.2"
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

