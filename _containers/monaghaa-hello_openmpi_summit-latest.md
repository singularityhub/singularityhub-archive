---
id: 8809
name: "monaghaa/hello_openmpi_summit"
branch: "master"
tag: "latest"
commit: "2efca62cbb93edd2f059eb4b97dafdac7b608200"
version: "5f59c605fabdffa8280e698cf6b2129a"
build_date: "2021-03-04T23:01:38.506Z"
size_mb: 1382
size: 430456863
sif: "https://datasets.datalad.org/shub/monaghaa/hello_openmpi_summit/latest/2021-03-04-2efca62c-5f59c605/5f59c605fabdffa8280e698cf6b2129a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/hello_openmpi_summit/latest/2021-03-04-2efca62c-5f59c605/
recipe: https://datasets.datalad.org/shub/monaghaa/hello_openmpi_summit/latest/2021-03-04-2efca62c-5f59c605/Singularity
collection: monaghaa/hello_openmpi_summit
---

# monaghaa/hello_openmpi_summit:latest

```bash
$ singularity pull shub://monaghaa/hello_openmpi_summit:latest
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

# Omnipath and OpenMPI user libraries for Summit
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

# GCC 7.2 (default system GCC is OLD, use newer version)
yum install -y centos-release-scl
yum install -y devtoolset-7-gcc*
#yum-config-manager --enable rhel-server-rhscl-7-rpms
scl enable devtoolset-7 bash

export LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7:$LD_LIBRARY_PATH
export PATH=/opt/rh/devtoolset-7/root/usr/bin:$PATH

# openmpi 2.0.1
# Explicitly use the GCC 7 compilers to compile
wget https://download.open-mpi.org/release/open-mpi/v2.0/openmpi-2.0.1.tar.gz
tar -xf openmpi-2.0.1.tar.gz
cd openmpi-2.0.1/
./configure \
--with-verbs \
--with-psm2 \
--enable-mpi-thread-multiple \
CXX=/opt/rh/devtoolset-7/root/usr/bin/g++ \
CC=/opt/rh/devtoolset-7/root/usr/bin/gcc \
FC=/opt/rh/devtoolset-7/root/usr/bin/gfortran
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

 - Name: [monaghaa/hello_openmpi_summit](https://github.com/monaghaa/hello_openmpi_summit)
 - License: None

