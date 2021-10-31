---
id: 3211
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "mpifileutils"
commit: "ea686b87780c342f065e0dbeab4299b7f4688300"
version: "2c824beec1b79904e4c0ec62cad4b731"
build_date: "2018-06-20T02:46:53.580Z"
size_mb: 846
size: 253997087
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/mpifileutils/2018-06-20-ea686b87-2c824bee/2c824beec1b79904e4c0ec62cad4b731.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/mpifileutils/2018-06-20-ea686b87-2c824bee/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/mpifileutils/2018-06-20-ea686b87-2c824bee/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:mpifileutils

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:mpifileutils
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:mpich

%post
   # need wget
   echo installing yum packages
   yum install -y cmake openssl-devel wget libattr-devel libarchive-devel
   export LD_LIBRARY_PATH=/mpifileutils/install/lib:/mpich/install/lib:/usr/local/lib64:/usr/local/lib:/usr/lib64:/usr/lib:/lib64:/lib
   export PATH=/mpifileutils/install/bin:/mpich/install/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin
   export PKG_CONFIG_PATH=/lib64/pkgconfig:/lib/pkgconfig:/usr/lib64/pkgconfig:/usr/lib/pkgconfig
   export libcircle_CFLAGS='-I/usr/include'
   export libcircle_LIBS='-L/usr/lib64 -L/usr/lib -lcircle'
   env
   
   # build mpifileutils dependencies
   echo checking out mpifileutils
   mkdir /mpifileutils
   cd /mpifileutils
   git clone https://github.com/hpc/mpifileutils.git .
   
   
   echo creating dependency directory
   mkdir deps
   cd deps
   
      
   # install lwgrp-1.0.2
   echo checkout/install lwgrp
   git clone https://github.com/LLNL/lwgrp.git
   cd lwgrp
   git checkout tags/v1.0.2
   ./configure --prefix=/usr
   make
   make install
   cd ..

   # install dtcmp
   echo checkout/install dtcmp
   git clone https://github.com/LLNL/dtcmp.git
   cd dtcmp
   git checkout tags/v1.0.3
   ./autogen.sh
   ./configure --prefix=/usr --with-lwgrp=/usr
   make
   make install
   cd ..

   # install libcircle-0.2.1-rc.1
   echo checkout/install libcircle
   # git clone https://github.com/hpc/libcircle.git
   git clone https://github.com/JulianKunkel/libcircle.git
   cd libcircle
   ./configure --prefix=/usr
   make
   make install
   cd ..

   
   cd /mpifileutils

   # build mpifileutils
   echo install mpifileutils
   ./autogen.sh
   env | sort
   CC=mpicc CXX=mpicxx ./configure --prefix=$PWD/install --enable-lustre
   make V=1
   make install
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

