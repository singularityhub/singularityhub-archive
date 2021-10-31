---
id: 4799
name: "pescobar/singularity-openmalaria"
branch: "master"
tag: "37.0.1"
commit: "b62c456f42babe6e95626fab62737068cb399851"
version: "a7e7b5af80cbc3a06b3e95965d0d6444"
build_date: "2018-09-13T14:30:55.207Z"
size_mb: 671
size: 186011679
sif: "https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/37.0.1/2018-09-13-b62c456f-a7e7b5af/a7e7b5af80cbc3a06b3e95965d0d6444.simg"
url: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/37.0.1/2018-09-13-b62c456f-a7e7b5af/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/37.0.1/2018-09-13-b62c456f-a7e7b5af/Singularity
collection: pescobar/singularity-openmalaria
---

# pescobar/singularity-openmalaria:37.0.1

```bash
$ singularity pull shub://pescobar/singularity-openmalaria:37.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="37.0.1"

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

