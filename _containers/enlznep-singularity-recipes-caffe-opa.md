---
id: 8908
name: "enlznep/singularity-recipes"
branch: "master"
tag: "caffe-opa"
commit: "9ea4718067645dd71b3ca8eb3a43650be51c35ff"
version: "89719fd68b467791c96412e10d16ac99"
build_date: "2019-05-07T14:45:54.344Z"
size_mb: 2394
size: 1007673375
sif: "https://datasets.datalad.org/shub/enlznep/singularity-recipes/caffe-opa/2019-05-07-9ea47180-89719fd6/89719fd68b467791c96412e10d16ac99.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/enlznep/singularity-recipes/caffe-opa/2019-05-07-9ea47180-89719fd6/
recipe: https://datasets.datalad.org/shub/enlznep/singularity-recipes/caffe-opa/2019-05-07-9ea47180-89719fd6/Singularity
collection: enlznep/singularity-recipes
---

# enlznep/singularity-recipes:caffe-opa

```bash
$ singularity pull shub://enlznep/singularity-recipes:caffe-opa
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-7/7.6.1810/os/x86_64/
Include: yum

%help
    Containerized Intel Caffe and Intel Omni-Path Architecture

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

    # Intel Omni-Path Architecture
    yum -y install perl atlas libpsm2 infinipath-psm libibverbs qperf pciutils tcl tcsh
    yum -y install expect sysfsutils librdmacm libibcm perftest rdma bc
    yum -y install elfutils-libelf-developenssh-clients openssh-server
    yum -y install libstdc++-devel gcc-gfortran rpm-buildx
    yum -y install compat-rdma-devel libibmad libibumad ibacm-devel
    yum -y install libibumad-devel libibumad-static libuuid-devel
    yum -y install irqbalance openssl openssl-devel

    # Intel Omni-Path Architecture
    mkdir /opt/tempdir
    cd /opt/tempdir
    wget -O OPA https://downloadmirror.intel.com/28721/eng/IntelOPA-Basic.RHEL76-x86_64.10.9.2.0.9.tgz
    tar -xvf OPA
    cd IntelOPA-Basic.RHEL76-x86_64.10.9.2.0.9
    ./INSTALL --user-space -n

    rm -rf /opt/tempdir

    # CAFFE
    cd /opt
    git clone https://github.com/intel/caffe.git intel-caffe
    cd intel-caffe
    cp Makefile.config.example Makefile.config
    NUM_THREADS=$(($(grep 'core id' /proc/cpuinfo | sort -u | wc -l)*2))
    make -j $NUM_THREADS

%environment
    source /opt/intel-caffe/external/mlsl/l_mlsl_2018.1.005/intel64/bin/mlslvars.sh
    CAFFE_ROOT=/opt/intel-caffe/build/tools/caffe
    export CAFFE_ROOT

%runscript
    exec $CAFFE_ROOT
```

## Collection

 - Name: [enlznep/singularity-recipes](https://github.com/enlznep/singularity-recipes)
 - License: None

