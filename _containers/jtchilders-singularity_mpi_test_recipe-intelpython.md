---
id: 5092
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "intelpython"
commit: "af2299bc9c2e9c8fc2519ab52e92588b1761745d"
version: "45e3fdd3fe3f71d28c27850ae25a30e9"
build_date: "2018-10-02T17:54:24.223Z"
size_mb: 4064
size: 1206132767
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/intelpython/2018-10-02-af2299bc-45e3fdd3/45e3fdd3fe3f71d28c27850ae25a30e9.simg"
url: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/intelpython/2018-10-02-af2299bc-45e3fdd3/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/intelpython/2018-10-02-af2299bc-45e3fdd3/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:intelpython

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:intelpython
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: intelpython/intelpython3_full:latest

%setup
   # make directory for MPICH
   mkdir ${SINGULARITY_ROOTFS}/mpich
   cd ${SINGULARITY_ROOTFS}/mpich/
   wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xf mpich-3.2.1.tar.gz --strip-components=1
   
   # check out singularity
   cd ${SINGULARITY_ROOTFS}
   git clone https://github.com/uber/horovod.git
   cd horovod
   git checkout v0.14.1

%post
   # install development tools
   # yum update -y
   # yum groupinstall -y "Development Tools"
   # yum install -y gcc
   # yum install -y gcc-c++
   apt-get update
   apt-get install build-essential --assume-yes
   apt-get install gcc g++ gfortran --assume-yes

   
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
   
   export PATH=/opt/conda/bin:$PATH
   export PYTHONPATH=/opt/conda/lib/python3.6/site-packages
   cd /horovod
   HOROVOD_WITHOUT_PYTORCH=1 HOROVOD_WITH_TENSORFLOW=1 python setup.py build
   HOROVOD_WITHOUT_PYTORCH=1 HOROVOD_WITH_TENSORFLOW=1 python setup.py install --prefix=/opt/conda 

   # install keras
   export PATH=/opt/conda/bin:$PATH
   conda install -y keras
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

