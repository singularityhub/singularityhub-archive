---
id: 1840
name: "AaronTHolt/openmpi_singularity"
branch: "master"
tag: "spack_base"
commit: "48d237a26698ff300eb2cdc94bd0ee5bf70fd19a"
version: "15ca18f67d757affb30358a307bc9c53"
build_date: "2019-09-04T22:45:12.462Z"
size_mb: 1020
size: 356454431
sif: "https://datasets.datalad.org/shub/AaronTHolt/openmpi_singularity/spack_base/2019-09-04-48d237a2-15ca18f6/15ca18f67d757affb30358a307bc9c53.simg"
url: https://datasets.datalad.org/shub/AaronTHolt/openmpi_singularity/spack_base/2019-09-04-48d237a2-15ca18f6/
recipe: https://datasets.datalad.org/shub/AaronTHolt/openmpi_singularity/spack_base/2019-09-04-48d237a2-15ca18f6/Singularity
collection: AaronTHolt/openmpi_singularity
---

# AaronTHolt/openmpi_singularity:spack_base

```bash
$ singularity pull shub://AaronTHolt/openmpi_singularity:spack_base
```

## Singularity Recipe

```singularity
BootStrap:docker
From:centos:centos7


%post

#yum check-update
#yum -y update
#yum -y upgrade

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

# Environment modules
yum install -y Lmod
source /etc/profile.d/z00_lmod.sh

# Other useful libraries
yum install -y pciutils
yum install -y which

# Editors
yum install -y vim emacs

# GCC make bison flex etc
yum groupinstall -y 'Development Tools'
yum install -y wget

## SPACK install GCC, cmake, OpenMPI
# Define versions
#export gcc_ver=6.4.0
#export cmake_ver=3.10.1
#export openmpi_ver=2.1.0

# Environment for Spack/Mfix
mkdir -p /app
cd /app

useradd spack
chown -R spack:spack /app

# Install Spack
su - spack
whoami
cd /app

git clone https://github.com/spack/spack.git
export SPACK_ROOT=/app/spack
export PATH=$SPACK_ROOT/bin:$PATH
spack bootstrap
source $SPACK_ROOT/share/spack/setup-env.sh

# Configure Spack Modules
cp -r $SPACK_ROOT/etc/spack/defaults/* $SPACK_ROOT/etc/spack/
sed -i '/prefix_inspections:/ i \ \ tcl: \
    hash_length: 0' $SPACK_ROOT/etc/spack/modules.yaml

# Exit spack user
exit

# Edit command prompt so its short and shows you in a container
export PS1="Singularity > "



######################################################
%environment

source /etc/profile
SPACK_ROOT=/app/spack
export SPACK_ROOT
source $SPACK_ROOT/share/spack/setup-env.sh





#
```

## Collection

 - Name: [AaronTHolt/openmpi_singularity](https://github.com/AaronTHolt/openmpi_singularity)
 - License: None

