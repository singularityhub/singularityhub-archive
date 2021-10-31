---
id: 8909
name: "enlznep/singularity-recipes"
branch: "master"
tag: "opa"
commit: "0a43ad11b74bdb757d0fc827fefebac5a22fc6a3"
version: "382908d3aa47037b8afcbf9c8ec83efa"
build_date: "2019-05-07T14:45:54.338Z"
size_mb: 1431
size: 455122975
sif: "https://datasets.datalad.org/shub/enlznep/singularity-recipes/opa/2019-05-07-0a43ad11-382908d3/382908d3aa47037b8afcbf9c8ec83efa.simg"
url: https://datasets.datalad.org/shub/enlznep/singularity-recipes/opa/2019-05-07-0a43ad11-382908d3/
recipe: https://datasets.datalad.org/shub/enlznep/singularity-recipes/opa/2019-05-07-0a43ad11-382908d3/Singularity
collection: enlznep/singularity-recipes
---

# enlznep/singularity-recipes:opa

```bash
$ singularity pull shub://enlznep/singularity-recipes:opa
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-7/7.6.1810/os/x86_64/
Include: yum

%help
    Containerized Intel Omni-Path Architecture

%labels
    Maintainer Ray Marc Marcellones
    Version v0.1

%post
    yum -y install epel-release
    yum -y update
    yum -y groupinstall "Development Tools"
    yum -y install wget cmake git
    yum -y install protobuf-devel protobuf-compiler boost-devel
    yum -y install snappy-devel opencv-devel atlas-devel
    yum -y install gflags-devel glog-devel lmdb-devel leveldb-devel hdf5-devel

    yum -y install perl atlas libpsm2 infinipath-psm libibverbs qperf pciutils tcl tcsh
    yum -y install expect sysfsutils librdmacm libibcm perftest rdma bc
    yum -y install elfutils-libelf-developenssh-clients openssh-server
    yum -y install libstdc++-devel gcc-gfortran rpm-buildx
    yum -y install compat-rdma-devel libibmad libibumad ibacm-devel
    yum -y install libibumad-devel libibumad-static libuuid-devel
    yum -y install irqbalance openssl openssl-devel

    mkdir /opt/tempdir
    cd /opt/tempdir
    wget -O OPA https://downloadmirror.intel.com/28721/eng/IntelOPA-Basic.RHEL76-x86_64.10.9.2.0.9.tgz
    tar -xvf OPA
    cd IntelOPA-Basic.RHEL76-x86_64.10.9.2.0.9
    ./INSTALL --user-space -n

    rm -rf /opt/tempdir
```

## Collection

 - Name: [enlznep/singularity-recipes](https://github.com/enlznep/singularity-recipes)
 - License: None

