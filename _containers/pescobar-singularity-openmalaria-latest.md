---
id: 4782
name: "pescobar/singularity-openmalaria"
branch: "master"
tag: "latest"
commit: "633db93a56f4ffd5373b14b061b3a4dce58485e6"
version: "6149a5b9ff7f5350e534157d1f3f01df"
build_date: "2018-09-13T11:38:52.487Z"
size_mb: 672
size: 186212383
sif: "https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/latest/2018-09-13-633db93a-6149a5b9/6149a5b9ff7f5350e534157d1f3f01df.simg"
url: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/latest/2018-09-13-633db93a-6149a5b9/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-openmalaria/latest/2018-09-13-633db93a-6149a5b9/Singularity
collection: pescobar/singularity-openmalaria
---

# pescobar/singularity-openmalaria:latest

```bash
$ singularity pull shub://pescobar/singularity-openmalaria:latest
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

