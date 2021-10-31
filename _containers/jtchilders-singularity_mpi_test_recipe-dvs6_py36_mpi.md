---
id: 7196
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "dvs6_py36_mpi"
commit: "72103691611e5a0f3db1d299ffc5d4417670eb49"
version: "477d7eeb2576619b8028775e13ec18ee"
build_date: "2019-02-14T08:45:01.838Z"
size_mb: 1338
size: 403017759
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi/2019-02-14-72103691-477d7eeb/477d7eeb2576619b8028775e13ec18ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi/2019-02-14-72103691-477d7eeb/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/dvs6_py36_mpi/2019-02-14-72103691-477d7eeb/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:dvs6_py36_mpi
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:dvs6_py36

%post
   yum install -y wget git patch
   echo setting up devtoolset6
   # setup devtoolset6
   scl enable devtoolset-6 bash

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

