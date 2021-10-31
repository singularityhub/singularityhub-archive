---
id: 5734
name: "Monica-Golumbeanu/openmalaria.containers"
branch: "master"
tag: "39.0"
commit: "8ea71048edeec8339a1aae3407bc8dd63a0c2d3e"
version: "3a9c41d2209aadf5041bfffe000c983f"
build_date: "2018-12-11T09:34:04.740Z"
size_mb: 777
size: 211005471
sif: "https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/39.0/2018-12-11-8ea71048-3a9c41d2/3a9c41d2209aadf5041bfffe000c983f.simg"
url: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/39.0/2018-12-11-8ea71048-3a9c41d2/
recipe: https://datasets.datalad.org/shub/Monica-Golumbeanu/openmalaria.containers/39.0/2018-12-11-8ea71048-3a9c41d2/Singularity
collection: Monica-Golumbeanu/openmalaria.containers
---

# Monica-Golumbeanu/openmalaria.containers:39.0

```bash
$ singularity pull shub://Monica-Golumbeanu/openmalaria.containers:39.0
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

   export OPENMALARIA_VERSION="39.0"

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

