---
id: 7457
name: "georgevanderson/SingularityTest"
branch: "master"
tag: "testing"
commit: "6a650a82ec323fc41615e11530654ac8ea69a58f"
version: "ea7b1f6e3e0f9177639adf7d1f26bfc5"
build_date: "2019-04-08T08:50:14.164Z"
size_mb: 573
size: 201183263
sif: "https://datasets.datalad.org/shub/georgevanderson/SingularityTest/testing/2019-04-08-6a650a82-ea7b1f6e/ea7b1f6e3e0f9177639adf7d1f26bfc5.simg"
url: https://datasets.datalad.org/shub/georgevanderson/SingularityTest/testing/2019-04-08-6a650a82-ea7b1f6e/
recipe: https://datasets.datalad.org/shub/georgevanderson/SingularityTest/testing/2019-04-08-6a650a82-ea7b1f6e/Singularity
collection: georgevanderson/SingularityTest
---

# georgevanderson/SingularityTest:testing

```bash
$ singularity pull shub://georgevanderson/SingularityTest:testing
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7
%post
    . /.singularity.d/env/10-docker.sh


%setup
	mkdir -p inputs
	touch testingSETUP.txt
# Mellanox OFED version 3.4-1.0.0.0
%post
    yum install -y \
        libnl \
        libnl3 \
        numactl-libs \
        wget
    rm -rf /var/cache/yum/*
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp http://content.mellanox.com/ofed/MLNX_OFED-3.4-1.0.0.0/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64.tgz
    mkdir -p /var/tmp && tar -x -f /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64.tgz -C /var/tmp -z
    rpm --install /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibverbs-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibverbs-devel-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibverbs-utils-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibmad-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibmad-devel-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibumad-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libibumad-devel-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libmlx4-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libmlx4-devel-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libmlx5-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/libmlx5-devel-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/librdmacm-devel-*.x86_64.rpm /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64/RPMS/librdmacm-*.x86_64.rpm
    rm -rf /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64.tgz /var/tmp/MLNX_OFED_LINUX-3.4-1.0.0.0-rhel7.2-x86_64

%post
    yum install -y \
        ca-certificates \
        cmake \
        git
    rm -rf /var/cache/yum/*

# GNU compiler
%post
    yum install -y centos-release-scl
    yum install -y \
        devtoolset-6-gcc \
        devtoolset-6-gcc-c++ \
        devtoolset-6-gcc-gfortran
    rm -rf /var/cache/yum/*
%environment
    export PATH=/opt/rh/devtoolset-6/root/usr/bin:$PATH
%post
    export PATH=/opt/rh/devtoolset-6/root/usr/bin:$PATH

# OpenMPI version 1.8.8
%post
    yum install -y \
        bzip2 \
        file \
        hwloc \
        make \
        numactl-devel \
        openssh-clients \
        perl \
        tar \
        wget
    rm -rf /var/cache/yum/*
%post
    cd /
    mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://www.open-mpi.org/software/ompi/v1.8/downloads/openmpi-1.8.8.tar.bz2
    mkdir -p /var/tmp && tar -x -f /var/tmp/openmpi-1.8.8.tar.bz2 -C /var/tmp -j
    cd /var/tmp/openmpi-1.8.8 &&  CC=gcc CXX=g++ F77=gfortran F90=gfortran FC=gfortran ./configure --prefix=/usr/local/openmpi --disable-getpwuid --enable-orterun-prefix-by-default --without-cuda --with-verbs
    make -j$(nproc)
    make -j$(nproc) install
    rm -rf /var/tmp/openmpi-1.8.8.tar.bz2 /var/tmp/openmpi-1.8.8
%environment
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/openmpi/bin:$PATH
%post
    export LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/openmpi/bin:$PATH

%post
    cd /
    git clone --depth=1 https://github.com/georgevanderson/RXMD.git RXMD && cd RXMD
	make all


%runscript
	echo "Running RXMD..."
	
	/RXMD/rxmd "$@"
```

## Collection

 - Name: [georgevanderson/SingularityTest](https://github.com/georgevanderson/SingularityTest)
 - License: None

