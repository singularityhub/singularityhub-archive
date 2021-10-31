---
id: 4801
name: "pescobar/singularity-openmalaria"
branch: "master"
tag: "38.0"
commit: "b62c456f42babe6e95626fab62737068cb399851"
version: "f42ace4a28cf89076fefb65b004770f1"
build_date: "2018-09-13T14:30:55.193Z"
size_mb: 672
size: 186212383
sif: "https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/38.0/2018-09-13-b62c456f-f42ace4a/f42ace4a28cf89076fefb65b004770f1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/singularity-openmalaria/38.0/2018-09-13-b62c456f-f42ace4a/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/38.0/2018-09-13-b62c456f-f42ace4a/Singularity
collection: pescobar/singularity-openmalaria
---

# pescobar/singularity-openmalaria:38.0

```bash
$ singularity pull shub://pescobar/singularity-openmalaria:38.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="38.0"

   # install the OpenMalara dependencies
   yum -y install epel-release
   yum -y install \
   boost-devel \
   cmake \
   gcc-c++ \
   glibc-devel \
   gsl-devel \
   make \
   wget \
   xerces-c-devel \
   xsd \
   zlib-devel
   yum clean all

   # download the source code and compile it
   cd /usr/local/src/
   wget https://github.com/SwissTPH/openmalaria/archive/schema-${OPENMALARIA_VERSION}.tar.gz
   tar xf schema-${OPENMALARIA_VERSION}.tar.gz
   mkdir -p /usr/local/src/openmalaria-schema-${OPENMALARIA_VERSION}/build/
   cd /usr/local/src/openmalaria-schema-${OPENMALARIA_VERSION}/build/
   cmake ..
   make
   cp openMalaria /usr/local/bin

%runscript
   exec openMalaria "$@"

%apprun openmalaria
   openMalaria "@"
```

## Collection

 - Name: [pescobar/singularity-openmalaria](https://github.com/pescobar/singularity-openmalaria)
 - License: None

