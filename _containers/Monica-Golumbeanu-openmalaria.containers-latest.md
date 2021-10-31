---
id: 4852
name: "Monica-Golumbeanu/openmalaria.containers"
branch: "master"
tag: "latest"
commit: "cf6af8c473b40668f970763d89633a68f751baeb"
version: "2e036bebcabc79daf1a2fe335f713fe2"
build_date: "2018-09-17T17:07:08.677Z"
size_mb: 614
size: 178233375
sif: "https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/latest/2018-09-17-cf6af8c4-2e036beb/2e036bebcabc79daf1a2fe335f713fe2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Monica-Golumbeanu/openmalaria.containers/latest/2018-09-17-cf6af8c4-2e036beb/
recipe: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/latest/2018-09-17-cf6af8c4-2e036beb/Singularity
collection: Monica-Golumbeanu/openmalaria.containers
---

# Monica-Golumbeanu/openmalaria.containers:latest

```bash
$ singularity pull shub://Monica-Golumbeanu/openmalaria.containers:latest
```

## Singularity Recipe

```singularity
####################################
# Singularity recipe for openMalaria version 38
#
####################################

Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="38.0"

   # install the OpenMalaria dependencies
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
   cmake .. -DCMAKE_BUILD_TYPE=RELEASE
   make

   # copy the binary and resource files to the bin/ folder
   cp openMalaria /usr/local/bin
   cp schema/scenario_current.xsd /usr/local/bin/
   cp ../test/densities.csv /usr/local/bin/


%runscript
   exec openMalaria "$@"

%apprun openmalaria
openMalaria "@"i

%help
To see the openMalaria command help, use the -h option
```

## Collection

 - Name: [Monica-Golumbeanu/openmalaria.containers](https://github.com/Monica-Golumbeanu/openmalaria.containers)
 - License: None

