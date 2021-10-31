---
id: 2800
name: "CHRUdeLille/vep_containers"
branch: "master"
tag: "92.1"
commit: "3d7b95e1c05a3a6ed7bad007d48f1a7b35146084"
version: "19e9a48293eed201c4fb812cf9ed9b8c"
build_date: "2018-05-16T15:23:51.863Z"
size_mb: 1626
size: 622141471
sif: "https://datasets.datalad.org/shub/CHRUdeLille/vep_containers/92.1/2018-05-16-3d7b95e1-19e9a482/19e9a48293eed201c4fb812cf9ed9b8c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CHRUdeLille/vep_containers/92.1/2018-05-16-3d7b95e1-19e9a482/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/vep_containers/92.1/2018-05-16-3d7b95e1-19e9a482/Singularity
collection: CHRUdeLille/vep_containers
---

# CHRUdeLille/vep_containers:92.1

```bash
$ singularity pull shub://CHRUdeLille/vep_containers:92.1
```

## Singularity Recipe

```singularity
#!/bin/bash
#
# Christophe Demay <christophe.demay@chru-lille.fr>
# 2018/04/24: initial version
BootStrap: docker
From: phusion/baseimage:0.10.1
%labels
  MAINTAINER christophe.demay@chru-lille.fr
  VERSION 92.1

%environment
  PATH=/opt/vep/src/ensembl-vep:$PATH
  LC_ALL=en_US.UTF-8
  LANGUAGE=en_US.UTF-8

%help
    __     _______ ____     ___ ____    _ 
    \ \   / / ____|  _ \   / _ \___ \  / |
     \ \ / /|  _| | |_) | | (_) |__) | | |
      \ V / | |___|  __/   \__, / __/ _| |
       \_/  |_____|_|        /_/_____(_)_|

  Singularity container for VEP 92.1 <https://github.com/Ensembl/ensembl-vep> application. Documentation available at http://www.ensembl.org/info/docs/tools/vep/script/index.html
  Cache folder is not included in the container. You have to bind folder containing the cache and add it with the '--cache' option.

%post

  apt-get update
  apt-get -y install  apache2 \
    build-essential \
    cpanminus \
    curl \
    git \
    libmysqlclient-dev \
    libpng12-dev \
    libssl-dev \
    locales \
    manpages \
    mysql-client \
    openssl \
    perl \
    perl-base \
    unzip \
    wget

  locale-gen en_US.UTF-8
  export LANGUAGE=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  locale-gen en_US.UTF-8
  dpkg-reconfigure locales
  
  cpanm DBI DBD::mysql
  
  git config --global http.postBuffer 524288000
  
  mkdir -p /opt/vep/src
  
  cd /opt/vep/src
  git clone -b release/92 https://github.com/Ensembl/ensembl.git
  git clone -b release/92 https://github.com/Ensembl/ensembl-vep.git 
  
  ensembl-vep/travisci/get_dependencies.sh
  export PERL5LIB=$PERL5LIB:/opt/vep/src/bioperl-live-release-1-6-924
  export KENT_SRC=/opt/vep/src/kent-335_base/src
  KENT_SRC=/opt/vep/src/kent-335_base/src
  export HTSLIB_DIR=/opt/vep/src/htslib
  export MACHTYPE=x86_64
  export CFLAGS="-fPIC"
  export DEPS=/opt/vep/src
  
  cd /opt/vep/src
  ensembl-vep/travisci/build_c.sh
  
  cd $HTSLIB_DIR
  make install
  
  cd /opt/vep/src
  git clone https://github.com/bioperl/bioperl-ext.git
  cd bioperl-ext
  git reset --hard 1b59725
  cd Bio/Ext/Align/
  perl -pi -e"s|(cd libs.+)CFLAGS=\\\'|\$1CFLAGS=\\\'-fPIC |" Makefile.PL
  perl Makefile.PL
  make
  make install
  
  cd /opt/vep/src
  cpanm --installdeps --with-recommends --notest --cpanfile ensembl/cpanfile .
  cpanm --installdeps --with-recommends --notest --cpanfile ensembl-vep/cpanfile .
  
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.utf8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8
  
  cd /opt/vep/src/ensembl-vep
  chmod u+x *.pl
  ./INSTALL.pl -a a -l
```

## Collection

 - Name: [CHRUdeLille/vep_containers](https://github.com/CHRUdeLille/vep_containers)
 - License: None

