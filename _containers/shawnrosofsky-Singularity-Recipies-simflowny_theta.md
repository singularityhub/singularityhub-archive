---
id: 13302
name: "shawnrosofsky/Singularity-Recipies"
branch: "master"
tag: "simflowny_theta"
commit: "cdb8c36a7cf1bb55ae604e8eead26403cd791848"
version: "af224a1eeefea07807c22e68714c684b4ff58bfa26cd17bf220a38c1549ac065"
build_date: "2020-06-17T21:10:43.276Z"
size_mb: 783.79296875
size: 821866496
sif: "https://datasets.datalad.org/shub/shawnrosofsky/Singularity-Recipies/simflowny_theta/2020-06-17-cdb8c36a-af224a1e/af224a1eeefea07807c22e68714c684b4ff58bfa26cd17bf220a38c1549ac065.sif"
url: https://datasets.datalad.org/shub/shawnrosofsky/Singularity-Recipies/simflowny_theta/2020-06-17-cdb8c36a-af224a1e/
recipe: https://datasets.datalad.org/shub/shawnrosofsky/Singularity-Recipies/simflowny_theta/2020-06-17-cdb8c36a-af224a1e/Singularity
collection: shawnrosofsky/Singularity-Recipies
---

# shawnrosofsky/Singularity-Recipies:simflowny_theta

```bash
$ singularity pull shub://shawnrosofsky/Singularity-Recipies:simflowny_theta
```

## Singularity Recipe

```singularity
bootstrap: docker
from: shawngr/test:app

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
#    cp example_codes/pi.c ${SINGULARITY_ROOTFS}/mpitestapp/

%environment
   export MPICH_DIR=/mpich/install
   export SINGULARITY_MPICH_DIR=$MPICH_DIR
   export SINGULARITYENV_APPEND_PATH=$MPICH_DIR/bin
   export SINGULAIRTYENV_APPEND_LD_LIBRARY_PATH=$MPICH_DIR/lib
   export PATH=$PATH:$MPICH_DIR/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MPICH_DIR/lib


%post
   # install development tools
   apt-get update -y 
   apt-get install -y wget
   
   # install MPICH
   MPICH_VERSION=3.3
   mkdir /mpich
   cd /mpich
   export MPICH_DIR=/mpich/install
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1

   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=$MPICH_DIR --disable-wrapper-rpath
   make -j 16 install
   # add to local environment to build pi.c
   env | sort
#    cd /mpitestapp
#    mpicc -o pi -fPIC pi.c

# %runscript
#    /mpitestapp/pi
```

## Collection

 - Name: [shawnrosofsky/Singularity-Recipies](https://github.com/shawnrosofsky/Singularity-Recipies)
 - License: None

