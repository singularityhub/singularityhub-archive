---
id: 4797
name: "pescobar/singularity-openmalaria"
branch: "master"
tag: "36.1.1"
commit: "b62c456f42babe6e95626fab62737068cb399851"
version: "c14244b3dfd5823abd2c46e98a21e6fc"
build_date: "2018-09-13T14:30:55.214Z"
size_mb: 672
size: 185983007
sif: "https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/36.1.1/2018-09-13-b62c456f-c14244b3/c14244b3dfd5823abd2c46e98a21e6fc.simg"
url: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/36.1.1/2018-09-13-b62c456f-c14244b3/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/36.1.1/2018-09-13-b62c456f-c14244b3/Singularity
collection: pescobar/singularity-openmalaria
---

# pescobar/singularity-openmalaria:36.1.1

```bash
$ singularity pull shub://pescobar/singularity-openmalaria:36.1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="36.1.1"

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

