---
id: 8271
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs8_py36_mpi33"
commit: "f3e0b2e03c17399cdbf830d07ba044cbdf1a7044"
version: "6e3f69e10d68062cea97beacddebe072"
build_date: "2019-04-08T19:28:20.992Z"
size_mb: 1404
size: 438874143
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36_mpi33/2019-04-08-f3e0b2e0-6e3f69e1/6e3f69e10d68062cea97beacddebe072.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36_mpi33/2019-04-08-f3e0b2e0-6e3f69e1/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs8_py36_mpi33/2019-04-08-f3e0b2e0-6e3f69e1/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs8_py36_mpi33

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs8_py36_mpi33
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:dvs8_py36

%post
   yum install -y wget git patch
   echo setting up devtoolset6
   # setup devtoolset6
   scl enable devtoolset-8 bash

   echo make alias for python 3.6
   # alias python3.6
   rm /usr/bin/python
   ln -s /usr/bin/python3.6 /usr/bin/python
   ln -s /usr/bin/pip3.6 /usr/bin/pip
   
   MPICH_VERSION=3.3
   echo installing mpich $MPICH_VERSION

   mkdir /mpich
   cd /mpich
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1
   ./configure --prefix=/mpich/install --disable-wrapper-rpath
   make -j 4 install
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

