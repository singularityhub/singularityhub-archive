---
id: 4800
name: "pescobar/singularity-openmalaria"
branch: "master"
tag: "37.0.2"
commit: "b62c456f42babe6e95626fab62737068cb399851"
version: "74b6ef33ab76ff72713162e30c47cdc4"
build_date: "2018-09-13T14:30:55.200Z"
size_mb: 671
size: 186097695
sif: "https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/37.0.2/2018-09-13-b62c456f-74b6ef33/74b6ef33ab76ff72713162e30c47cdc4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/singularity-openmalaria/37.0.2/2018-09-13-b62c456f-74b6ef33/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/37.0.2/2018-09-13-b62c456f-74b6ef33/Singularity
collection: pescobar/singularity-openmalaria
---

# pescobar/singularity-openmalaria:37.0.2

```bash
$ singularity pull shub://pescobar/singularity-openmalaria:37.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="37.0.2"

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

