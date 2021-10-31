---
id: 8490
name: "gaohao95/pocl-singularity"
branch: "master"
tag: "def"
commit: "a0075326e0321eae90da1346ba27753365de38f8"
version: "184fb7d3a06b393dc098753d18b41dfd"
build_date: "2019-04-18T21:44:23.951Z"
size_mb: 957
size: 411054111
sif: "https://datasets.datalad.org/shub/gaohao95/pocl-singularity/def/2019-04-18-a0075326-184fb7d3/184fb7d3a06b393dc098753d18b41dfd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gaohao95/pocl-singularity/def/2019-04-18-a0075326-184fb7d3/
recipe: https://datasets.datalad.org/shub/gaohao95/pocl-singularity/def/2019-04-18-a0075326-184fb7d3/Singularity
collection: gaohao95/pocl-singularity
---

# gaohao95/pocl-singularity:def

```bash
$ singularity pull shub://gaohao95/pocl-singularity:def
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://ubuntu.cs.utah.edu/ubuntu
OSVersion: xenial

%labels

    APPLICATION_NAME ubuntu + mvapich2
    APPLICATION_VERSION 16.04 + 2.1

    SYSTEM_NAME comet
    SYSTEM_SINGULARITY_VERSION 2.6.1
    SYSTEM_URL http://www.sdsc.edu/support/user_guides/comet.html

    SINGULARITY_IMAGE_SIZE 4096

%setup

%environment

    # Set system locale
    export LC_ALL=C

%post -c /bin/bash

    # Set system locale
    export LC_ALL=C

    # Install system metapackages
    apt-get -y install ubuntu-standard
    apt-get -y install ubuntu-server

    # Add repositories
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION} main"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION} universe"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION} multiverse"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION} restricted"

    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-updates main"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-updates universe"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-updates multiverse"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-updates restricted"

    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-backports main"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-backports universe"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-backports multiverse"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-backports restricted"

    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-security main"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-security universe"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-security multiverse"
    add-apt-repository -y -s "deb ${MIRRORURL} ${OSVERSION}-security restricted"

    # Upgrade all packages to their latest versions
    apt-get -y update && apt-get -y upgrade

    # Install common packages from 'main'
    apt-get -y install autoconf
    apt-get -y install automake
    apt-get -y install build-essential
    apt-get -y install cmake
    apt-get -y install libtool
    apt-get -y install pkg-config
    apt-get -y install gfortran
    apt-get -y install zip
    apt-get -y install git
    apt-get -y install wget

    # Install expect to automate responses for interactive build questions
    apt-get -y install expect

    # Make filesystem mount points
    mkdir /cvmfs /oasis /projects /scratch

    # Use /tmp to store temporary files within the container during the
    # bootstraping process
    cd /tmp

    # Install miniconda3
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3

    # Install basic drivers for user space access to Ethernet, RDMA,
    # and Infiniband. See https://community.mellanox.com/docs/DOC-2431
    apt-get -y install dkms
    apt-get -y install infiniband-diags
    apt-get -y install libibverbs-dev
    apt-get -y install ibacm
    apt-get -y install librdmacm-dev
    apt-get -y install libmlx4-dev
    apt-get -y install libmlx5-dev
    apt-get -y install mstflint
    apt-get -y install libibcm-dev
    apt-get -y install libibmad-dev
    apt-get -y install libibumad-dev
    apt-get -y install opensm
    apt-get -y install srptools

    # Install additional tools
    apt-get -y install ibutils
    apt-get -y install ibverbs-utils
    apt-get -y install rdmacm-utils
    apt-get -y install perftest
    apt-get -y install numactl
    apt-get -y install libnuma-dev

    # Install libnl
    apt-get -y install libnl-3-200
    apt-get -y install libnl-route-3-200
    apt-get -y install libnl-route-3-dev
    apt-get -y install libnl-utils

    # Install mvapich2 (build) dependencies
    apt-get -y install bison

    # Download, build, and install mvapich2
    wget http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-2.1.tar.gz
    tar -xzvf mvapich2-2.1.tar.gz
    cd mvapich2-2.1
    ./configure --prefix=/opt/mvapich2
    make
    make install

    # Install llvm and clang
    echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main" >> /etc/apt/sources.list.d/llvm.list
	echo "deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main" >> /etc/apt/sources.list.d/llvm.list
	wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
	apt-get update
	apt-get -y install libllvm-8-ocaml-dev libllvm8 llvm-8 llvm-8-dev llvm-8-runtime
	apt-get -y install clang-8 clang-tools-8 libclang-common-8-dev libclang-8-dev libclang1-8 clang-format-8 python-clang-8
	
	# Install additional depencies for pocl
	apt-get -y install zlib1g-dev libtinfo-dev libltdl3-dev hwloc libhwloc-dev

    # Install pyopencl
    apt-get -y install ocl-icd-dev ocl-icd-libopencl1 ocl-icd-opencl-dev

    # Build Pocl
    cd /projects/
    git clone https://github.com/pocl/pocl.git && cd pocl
    mkdir build && cd build
    POCL_PREFIX=/opt/miniconda3/
    cmake -D CMAKE_BUILD_TYPE="Debug" -D CMAKE_INSTALL_PREFIX="${POCL_PREFIX}" -D CMAKE_PREFIX_PATH="${POCL_PREFIX}" -D POCL_INSTALL_ICD_VENDORDIR="${POCL_PREFIX}/etc/OpenCL/vendors" -D INSTALL_OPENCL_HEADERS="off" -D ENABLE_ICD=on -DWITH_LLVM_CONFIG=llvm-config-8 ..
    make -j4
    make install
    make check

    # Configure env
    export PATH="/opt/mvapich2/bin:${PATH}"
    export LD_LIBRARY_PATH="/opt/mvapich2/lib:${LD_LIBRARY_PATH}"
    export PATH="/opt/miniconda3/bin:${PATH}"

    # Configure pyopencl
    conda config --add channels conda-forge
    conda install -y pyopencl

    # Set container environment variables
    cd /.singularity.d/env
    echo 'export PATH="/opt/mvapich2/bin:${PATH}"' >> 90-environment.sh
    echo 'export LD_LIBRARY_PATH="/opt/mvapich2/lib:${LD_LIBRARY_PATH}"' >> 90-environment.sh
    echo 'export PATH="/opt/miniconda3/bin:${PATH}"' >> 90-environment.sh

    # Update database for mlocate
    updatedb

%files

%runscript

%test

    #export PATH="/opt/mvapich2/bin:${PATH}"
    #export LD_LIBRARY_PATH="/opt/mvapich2/lib:${LD_LIBRARY_PATH}"
    #mpirun --version
```

## Collection

 - Name: [gaohao95/pocl-singularity](https://github.com/gaohao95/pocl-singularity)
 - License: None

