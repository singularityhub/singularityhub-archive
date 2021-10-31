---
id: 5839
name: "Monica-Golumbeanu/openmalaria.containers"
branch: "master"
tag: "39.1"
commit: "8cef2ede788f5839eacc9a4b0ff6e811cb79535e"
version: "ddd33481ddc0a843a29c509417ac4df5"
build_date: "2018-12-10T20:17:30.701Z"
size_mb: 777
size: 211009567
sif: "https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/39.1/2018-12-10-8cef2ede-ddd33481/ddd33481ddc0a843a29c509417ac4df5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Monica-Golumbeanu/openmalaria.containers/39.1/2018-12-10-8cef2ede-ddd33481/
recipe: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/39.1/2018-12-10-8cef2ede-ddd33481/Singularity
collection: Monica-Golumbeanu/openmalaria.containers
---

# Monica-Golumbeanu/openmalaria.containers:39.1

```bash
$ singularity pull shub://Monica-Golumbeanu/openmalaria.containers:39.1
```

## Singularity Recipe

```singularity
####################################
# Singularity recipe for openMalaria version 39.1
#
####################################

Bootstrap: docker
From: fedora:latest

%post

   export OPENMALARIA_VERSION="39.1"

   # install the OpenMalaria dependencies
   # yum -y install epel-release
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
   zlib-devel \
   python2
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

