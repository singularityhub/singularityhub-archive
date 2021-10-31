---
id: 8464
name: "rearmstr/singularity_image_recipes"
branch: "master"
tag: "mpich33"
commit: "08cc5c2bab50c0da462d55b6d7da07eb6d427de3"
version: "2954196691ee47e3bc889e33d2c01e68"
build_date: "2019-04-17T14:28:05.119Z"
size_mb: 902
size: 254058527
sif: "https://datasets.datalad.org/shub/rearmstr/singularity_image_recipes/mpich33/2019-04-17-08cc5c2b-29541966/2954196691ee47e3bc889e33d2c01e68.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rearmstr/singularity_image_recipes/mpich33/2019-04-17-08cc5c2b-29541966/
recipe: https://datasets.datalad.org/shub/rearmstr/singularity_image_recipes/mpich33/2019-04-17-08cc5c2b-29541966/Singularity
collection: rearmstr/singularity_image_recipes
---

# rearmstr/singularity_image_recipes:mpich33

```bash
$ singularity pull shub://rearmstr/singularity_image_recipes:mpich33
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
   /mpitestapp/pi

%environment
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   export PATH=$PATH:/mpich/install/bin
```

## Collection

 - Name: [rearmstr/singularity_image_recipes](https://github.com/rearmstr/singularity_image_recipes)
 - License: None

