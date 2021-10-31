---
id: 10521
name: "monaghaa/hello_openmpi_teton"
branch: "master"
tag: "latest"
commit: "31cef146ccf082888b22be8367311180f17ea907"
version: "993a5a08168fbf7ebe15c68d2a49cf792289db46880a61ff614ad57d97bd08fb"
build_date: "2019-08-09T16:43:45.563Z"
size_mb: 431.41015625
size: 452366336
sif: "https://datasets.datalad.org/shub/monaghaa/hello_openmpi_teton/latest/2019-08-09-31cef146-993a5a08/993a5a08168fbf7ebe15c68d2a49cf792289db46880a61ff614ad57d97bd08fb.sif"
url: https://datasets.datalad.org/shub/monaghaa/hello_openmpi_teton/latest/2019-08-09-31cef146-993a5a08/
recipe: https://datasets.datalad.org/shub/monaghaa/hello_openmpi_teton/latest/2019-08-09-31cef146-993a5a08/Singularity
collection: monaghaa/hello_openmpi_teton
---

# monaghaa/hello_openmpi_teton:latest

```bash
$ singularity pull shub://monaghaa/hello_openmpi_teton:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:centos:centos7

%files

%post

# Update yum
#yum check-update
yum -y update
yum -y upgrade

# Speed up yum
yum install -y yum-plugin-fastestmirror
yum install -y deltarpm

# Epel
yum install -y epel-release

# Omnipath, Infiniband and OpenMPI user libraries
yum install -y libhfi1 libpsm2 libpsm2-devel libpsm2-compat
yum install -y perftest qperf
yum install -y libibverbs libibverbs-devel rdma
yum install -y numactl-libs numactl-devel

# Other useful libraries
yum install -y pciutils
yum install -y which

# Editors (not useful in production, but useful for debugging)
yum install -y vim emacs

# GCC make bison flex etc
yum groupinstall -y 'Development Tools'
yum install -y wget

# GCC 8.2.1 (default system GCC is OLD, use newer version)
yum install -y centos-release-scl
yum install -y devtoolset-8-gcc*
scl enable devtoolset-8 bash

export LD_LIBRARY_PATH=/opt/rh/devtoolset-8/root/usr/lib/gcc/x86_64-redhat-linux/8:$LD_LIBRARY_PATH
export PATH=/opt/rh/devtoolset-8/root/usr/bin:$PATH

# openmpi 3.1.0
# Explicitly use the GCC 8 compilers to compile
wget https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.0.tar.gz
tar -xf openmpi-3.1.0.tar.gz
cd openmpi-3.1.0/
./configure \
--with-verbs \
--with-psm2 \
--enable-mpi-thread-multiple \
CXX=/opt/rh/devtoolset-8/root/usr/bin/g++ \
CC=/opt/rh/devtoolset-8/root/usr/bin/gcc \
FC=/opt/rh/devtoolset-8/root/usr/bin/gfortran
make -j4
make install

# intall a test "hello world" mpi code
cd /opt
git clone https://github.com/wesleykendall/mpitutorial
cd mpitutorial/tutorials/mpi-hello-world/code
make

######################################################
%environment
# Edit command prompt so its short and shows you in a container
export PS1="Singularity > "
# Add mpi_hello_world to path
export PATH=/opt/mpitutorial/tutorials/mpi-hello-world/code:$PATH
# to run: "mpirun -n 4 singularity exec mpicontainername.sif mpi_hello_world"

######################################################
%runscript
```

## Collection

 - Name: [monaghaa/hello_openmpi_teton](https://github.com/monaghaa/hello_openmpi_teton)
 - License: None

