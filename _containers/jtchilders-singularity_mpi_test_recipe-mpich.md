---
id: 3210
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "mpich"
commit: "4aa2e0b529b8cc7696818e10b3761c35727a745b"
version: "a19a14aa57285193d52383720ba7c1af"
build_date: "2020-05-06T08:12:52.289Z"
size_mb: 775
size: 225202207
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/mpich/2020-05-06-4aa2e0b5-a19a14aa/a19a14aa57285193d52383720ba7c1af.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/mpich/2020-05-06-4aa2e0b5-a19a14aa/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/mpich/2020-05-06-4aa2e0b5-a19a14aa/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:mpich

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:mpich
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/mpitestapp
   cp pi.c ${SINGULARITY_ROOTFS}/mpitestapp/
   # make directory for MPICH
   mkdir ${SINGULARITY_ROOTFS}/mpich
   cd ${SINGULARITY_ROOTFS}/mpich/
   wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xf mpich-3.2.1.tar.gz --strip-components=1

%post
   # install development tools
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   # yum install -y wget
   # install MPICH
   cd /mpich
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

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

