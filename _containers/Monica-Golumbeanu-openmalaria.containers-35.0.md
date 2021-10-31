---
id: 5665
name: "Monica-Golumbeanu/openmalaria.containers"
branch: "master"
tag: "35.0"
commit: "a371037141ffa8a5033d236e8713ca67e3b5f0e0"
version: "209def44b3b645ce277a18779afcca4d"
build_date: "2018-11-21T17:32:11.894Z"
size_mb: 613
size: 177819679
sif: "https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/35.0/2018-11-21-a3710371-209def44/209def44b3b645ce277a18779afcca4d.simg"
url: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/35.0/2018-11-21-a3710371-209def44/
recipe: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/35.0/2018-11-21-a3710371-209def44/Singularity
collection: Monica-Golumbeanu/openmalaria.containers
---

# Monica-Golumbeanu/openmalaria.containers:35.0

```bash
$ singularity pull shub://Monica-Golumbeanu/openmalaria.containers:35.0
```

## Singularity Recipe

```singularity
####################################
# Singularity recipe for openMalaria version 35
#
####################################

Bootstrap: docker
From: centos:7

%post

   export OPENMALARIA_VERSION="35.0"

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

