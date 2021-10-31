---
id: 8334
name: "ivana-m/singularity_image_recipes"
branch: "master"
tag: "dvs6_py36_mpi33"
commit: "a375cb8ec77799394eb2450cd3f4f82c65f4dd49"
version: "ca2f67c816e4025510e604a93cead872"
build_date: "2019-04-10T18:24:19.201Z"
size_mb: 1302
size: 396574751
sif: "https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/dvs6_py36_mpi33/2019-04-10-a375cb8e-ca2f67c8/ca2f67c816e4025510e604a93cead872.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ivana-m/singularity_image_recipes/dvs6_py36_mpi33/2019-04-10-a375cb8e-ca2f67c8/
recipe: https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/dvs6_py36_mpi33/2019-04-10-a375cb8e-ca2f67c8/Singularity
collection: ivana-m/singularity_image_recipes
---

# ivana-m/singularity_image_recipes:dvs6_py36_mpi33

```bash
$ singularity pull shub://ivana-m/singularity_image_recipes:dvs6_py36_mpi33
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_image_recipes:dvs6_py36

%setup
   # copy test script to container
   mkdir $SINGULARITY_ROOTFS/myapp
   cp example_codes/pi.py $SINGULARITY_ROOTFS/myapp

%post
   yum install -y wget
   echo setting up devtoolset6
   # setup devtoolset6
   scl enable devtoolset-6 bash
   
   MPICH_VERSION=3.3
   echo installing mpich $MPICH_VERSION
   mkdir /mpich
   cd /mpich
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1
   ./configure --prefix=/mpich/install --disable-wrapper-rpath
   make -j 4 install
   
   # add mpich to environment
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   
   # install mpi4py
   pip3.6 install mpi4py

%runscript
   python3.6 /myapp/pi.py
```

## Collection

 - Name: [ivana-m/singularity_image_recipes](https://github.com/ivana-m/singularity_image_recipes)
 - License: None

