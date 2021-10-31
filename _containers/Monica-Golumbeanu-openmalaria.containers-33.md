---
id: 4853
name: "Monica-Golumbeanu/openmalaria.containers"
branch: "master"
tag: "33"
commit: "f82a7ef69a35a552d10052b9d4dcc939b54a235f"
version: "d262ea3f4e3dbc545ff1b5df00544ce2"
build_date: "2018-09-17T17:07:08.670Z"
size_mb: 613
size: 177418271
sif: "https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/33/2018-09-17-f82a7ef6-d262ea3f/d262ea3f4e3dbc545ff1b5df00544ce2.simg"
url: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/33/2018-09-17-f82a7ef6-d262ea3f/
recipe: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/33/2018-09-17-f82a7ef6-d262ea3f/Singularity
collection: Monica-Golumbeanu/openmalaria.containers
---

# Monica-Golumbeanu/openmalaria.containers:33

```bash
$ singularity pull shub://Monica-Golumbeanu/openmalaria.containers:33
```

## Singularity Recipe

```singularity
####################################
# Singularity recipe for openMalaria version 33
#
####################################

Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="33"

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

