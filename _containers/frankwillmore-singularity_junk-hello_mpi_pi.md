---
id: 9664
name: "frankwillmore/singularity_junk"
branch: "master"
tag: "hello_mpi_pi"
commit: "090fd2d636365ee6c0be7f5606edd00133048be3"
version: "e10de5d56fab6f4c9d1eaa6532a94130"
build_date: "2019-06-08T01:44:30.138Z"
size_mb: 924
size: 260386847
sif: "https://datasets.datalad.org/shub/frankwillmore/singularity_junk/hello_mpi_pi/2019-06-08-090fd2d6-e10de5d5/e10de5d56fab6f4c9d1eaa6532a94130.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/frankwillmore/singularity_junk/hello_mpi_pi/2019-06-08-090fd2d6-e10de5d5/
recipe: https://datasets.datalad.org/shub/frankwillmore/singularity_junk/hello_mpi_pi/2019-06-08-090fd2d6-e10de5d5/Singularity
collection: frankwillmore/singularity_junk
---

# frankwillmore/singularity_junk:hello_mpi_pi

```bash
$ singularity pull shub://frankwillmore/singularity_junk:hello_mpi_pi
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   cp example_codes/pi.c ${SINGULARITY_ROOTFS}/mpitestapp/

%post
   # install development tools
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc gcc-c++ wget
   
   # install MPICH
   MPICH_VERSION=3.3
   mkdir /mpich
   cd /mpich
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1

   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=/mpich/install --disable-wrapper-rpath
   make -j 4 install
   # add to local environment to build pi.c
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort
   cd /mpitestapp
   mpicc -o pi -fPIC pi.c

%runscript
   echo $@
   /mpitestapp/pi
```

## Collection

 - Name: [frankwillmore/singularity_junk](https://github.com/frankwillmore/singularity_junk)
 - License: None

