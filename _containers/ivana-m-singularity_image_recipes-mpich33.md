---
id: 8331
name: "ivana-m/singularity_image_recipes"
branch: "master"
tag: "mpich33"
commit: "5d2183af032ed50f57f5dac9fd229b5822bb6004"
version: "98a24496de2e869b57b63a4e7e3d1b2e"
build_date: "2019-04-10T18:24:19.218Z"
size_mb: 902
size: 254058527
sif: "https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/mpich33/2019-04-10-5d2183af-98a24496/98a24496de2e869b57b63a4e7e3d1b2e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ivana-m/singularity_image_recipes/mpich33/2019-04-10-5d2183af-98a24496/
recipe: https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/mpich33/2019-04-10-5d2183af-98a24496/Singularity
collection: ivana-m/singularity_image_recipes
---

# ivana-m/singularity_image_recipes:mpich33

```bash
$ singularity pull shub://ivana-m/singularity_image_recipes:mpich33
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
```

## Collection

 - Name: [ivana-m/singularity_image_recipes](https://github.com/ivana-m/singularity_image_recipes)
 - License: None

