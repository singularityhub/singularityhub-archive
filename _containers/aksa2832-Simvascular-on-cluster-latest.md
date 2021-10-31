---
id: 13646
name: "aksa2832/Simvascular-on-cluster"
branch: "master"
tag: "latest"
commit: "ce86266f57c261cec93acb8f9203f47339ef2126"
version: "612823e4dcb6890ec6a00f682a43890d47e1d5f29e36322e532c6d04984e616d"
build_date: "2020-11-27T20:09:31.371Z"
size_mb: 619.84765625
size: 649957376
sif: "https://datasets.datalad.org/shub/aksa2832/Simvascular-on-cluster/latest/2020-11-27-ce86266f-612823e4/612823e4dcb6890ec6a00f682a43890d47e1d5f29e36322e532c6d04984e616d.sif"
url: https://datasets.datalad.org/shub/aksa2832/Simvascular-on-cluster/latest/2020-11-27-ce86266f-612823e4/
recipe: https://datasets.datalad.org/shub/aksa2832/Simvascular-on-cluster/latest/2020-11-27-ce86266f-612823e4/Singularity
collection: aksa2832/Simvascular-on-cluster
---

# aksa2832/Simvascular-on-cluster:latest

```bash
$ singularity pull shub://aksa2832/Simvascular-on-cluster:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:centos:centos7

%files
quick-build-centos7-open-mpi.sh /opt
quick-build-linux.sh /opt

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
yum install -y cmake3
yum install -y gmp-devel
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
rm -Rf /openmpi-2.0.1.tar.gz

# install cmake3 (needed for raxml-ng installation)
yum install -y cmake3
cd /usr/bin/
ln -sf cmake3 cmake

# install svSolver
cd /opt
git clone https://github.com/SimVascular/svSolver.git
cd svSolver
cd BuildWithMake/
cp /opt/quick-build-centos7-open-mpi.sh .
cp /opt/quick-build-linux.sh .
yum install -y tcl
source quick-build-centos7-open-mpi.sh >&log

######################################################
%environment
# Edit command prompt so its short and shows you in a container
export PS1="Singularity > "
# Add raxml-ng to path
export PATH=/opt/rh/devtoolset-7/root/usr/bin:$PATH
export LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7:$LD_LIBRARY_PATH

######################################################
%runscript
```

## Collection

 - Name: [aksa2832/Simvascular-on-cluster](https://github.com/aksa2832/Simvascular-on-cluster)
 - License: None

