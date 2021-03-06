---
id: 2280
name: "jekriske/r-base"
branch: "master"
tag: "3.4.4"
commit: "be4bc35d5b75b7e73d281224727b5849aeba51ed"
version: "cd4f5fb61b45e01787eaf231cbfb0eee"
build_date: "2021-04-19T18:37:58.172Z"
size_mb: 770
size: 289116191
sif: "https://datasets.datalad.org/shub/jekriske/r-base/3.4.4/2021-04-19-be4bc35d-cd4f5fb6/cd4f5fb61b45e01787eaf231cbfb0eee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jekriske/r-base/3.4.4/2021-04-19-be4bc35d-cd4f5fb6/
recipe: https://datasets.datalad.org/shub/jekriske/r-base/3.4.4/2021-04-19-be4bc35d-cd4f5fb6/Singularity
collection: jekriske/r-base
---

# jekriske/r-base:3.4.4

```bash
$ singularity pull shub://jekriske/r-base:3.4.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7
IncludeCmd: no

%labels
  Maintainer Jeff Kriske
  Version v0.1.0
  R_Version 3.4.4

%environment
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"

%post
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export R_VERSION="R-3.4.4"
  yum update -y
  cd /tmp
  curl -O http://ftp.ussg.iu.edu/CRAN/src/base/R-3/${R_VERSION}.tar.gz
  tar xf ${R_VERSION}.tar.gz && rm ${R_VERSION}.tar.gz
  yum install -y epel-release
  yum install -y autoconf \
                 bison \
                 blas \
                 bzip2 bzip2-devel \
                 cairo-devel \
                 fdupes \
                 flex \
                 ftp \
                 gcc \
                 gcc-c++ \
                 gcc-gfortran \
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
                 pango-devel \
                 pcre pcre-devel \
                 perl-macros \
                 perl-Text-Unidecode.noarch \
                 readline-devel \
                 tar \
                 tcl-devel \
                 texlive-helvetic \
                 texlive-metafont \
                 texlive-psnfss \
                 texlive-times \
                 tk-devel \
                 unzip \
                 vim-minimal \
                 wget \
                 which \
                 xdg-utils \
                 xorg-x11-fonts-ISO* \
                 xz xz-devel \
                 zlib zlib-devel
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
      && locale-gen en_US.utf8 \
      && /usr/sbin/update-locale LANG=en_US.UTF-8
  echo "Etc/UTC" /etc/timezone
  cd /tmp/${R_VERSION}
  dbus-uuidgen >/etc/machine-id
  rm /usr/bin/timedatectl
  ./configure --enable-R-shlib
  make -j4
  make install
  make install-libR
  make check
  yum clean all && rm -rf /var/cache/yum
  rm -rf /tmp/${R_VERSION}
```

## Collection

 - Name: [jekriske/r-base](https://github.com/jekriske/r-base)
 - License: None

