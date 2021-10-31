---
id: 3212
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "openmpi"
commit: "56c9824c6ebb592942fae3df5f748b891f1affb2"
version: "bd45c08fb947af0cd3ece2ddec00859c"
build_date: "2020-06-30T13:12:53.970Z"
size_mb: 874
size: 244748319
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/openmpi/2020-06-30-56c9824c-bd45c08f/bd45c08fb947af0cd3ece2ddec00859c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/openmpi/2020-06-30-56c9824c-bd45c08f/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/openmpi/2020-06-30-56c9824c-bd45c08f/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:openmpi

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:openmpi
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   # copy test file into directory
   cp pi.c ${SINGULARITY_ROOTFS}/mpitestapp/

%post
   env | sort
   # install development tools
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   yum install -y wget 

   # build openmpi
   mkdir /openmpi
   cd /openmpi
   wget https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.0.tar.gz
   tar xf openmpi-3.1.0.tar.gz --strip-components=1
   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=$PWD/install --disable-wrapper-rpath --disable-wrapper-runpath
   make -j 4 install
   export LD_LIBRARY_PATH=$PWD/install/lib:$LD_LIBRARY_PATH
   export PATH=$PWD/install/bin:$PATH

   cd /mpitestapp
   mpicc -o pi -fPIC pi.c

%runscript
   /mpitestapp/pi
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

