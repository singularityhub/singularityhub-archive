---
id: 935
name: "ruycastilho/GPUtest"
branch: "master"
tag: "automatic"
commit: "cfc116fb6bac0436d8936e1c152defdc830af9f6"
version: "4f873f070a693794b0ec190cb70d40da"
build_date: "2017-12-13T18:55:31.755Z"
size_mb: 2052
size: 1086468127
sif: "https://datasets.datalad.org/shub/ruycastilho/GPUtest/automatic/2017-12-13-cfc116fb-4f873f07/4f873f070a693794b0ec190cb70d40da.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ruycastilho/GPUtest/automatic/2017-12-13-cfc116fb-4f873f07/
recipe: https://datasets.datalad.org/shub/ruycastilho/GPUtest/automatic/2017-12-13-cfc116fb-4f873f07/Singularity
collection: ruycastilho/GPUtest
---

# ruycastilho/GPUtest:automatic

```bash
$ singularity pull shub://ruycastilho/GPUtest:automatic
```

## Singularity Recipe

```singularity
# Automatic

BootStrap: docker
From: nvidia/cuda:8.0-devel-ubuntu14.04

# change to cuda-9.0 for Volta
%post
    apt-get update
    apt-get -y install build-essential
    apt-get -y install apt-utils
    apt-get -y install make
    apt-get -y install cmake
    apt-get -y install git
    mkdir /dev/fuse 
    chmod 777 /dev/fuse
    apt-get -y install fuse
	apt-get -y install wget
    apt-get -y install flex
    apt-get -y install automake
    apt-get -y install autoconf
    apt-get -y install autotools-dev
    apt-get -y install libtool
    apt-get -y install gcc
    export TERM=xterm
    apt-get install -y linux-headers-generic
    apt-get -y install clinfo
    apt-get -y install tar
    apt-get -y install zip
    apt-get -y install unzip
    apt-get install -y libxcb-dri3-0 libxcb-dri2-0
    apt-get install -y --no-install-recommends alien

# Download the Intel OpenCL 2.0 development headers
    export DEVEL_URL="https://software.intel.com/file/531197/download" \
    && wget ${DEVEL_URL} -q -O download.zip --no-check-certificate \
    && unzip download.zip \
    && rm -f download.zip *.tar.xz* \
    && alien --to-deb *dev*.rpm \
    && dpkg -i *dev*.deb \
    && rm *.rpm *.deb

# Download the Intel OpenCL CPU runtime and convert to .deb packages
    export RUNTIME_URL="http://registrationcenter-download.intel.com/akdlm/irc_nas/9019/opencl_runtime_16.1.1_x64_ubuntu_6.4.0.25.tgz" \
    && export TAR=$(basename ${RUNTIME_URL}) \
    && export DIR=$(basename ${RUNTIME_URL} .tgz) \
    && wget -q ${RUNTIME_URL} \
    && tar -xf ${TAR} \
    && for i in ${DIR}/rpm/*.rpm; do alien --to-deb $i; done \
    && rm -rf ${DIR} ${TAR} \
    && dpkg -i *.deb \
    && rm *.deb

    mkdir -p /etc/OpenCL/vendors/ \
    && echo "/opt/intel/opencl-1.2-6.4.0.25/lib64/libintelocl.so" > /etc/OpenCL/vendors/intel.icd

# Let the system know where to find the OpenCL library at runtime
    OCL_INC=/opt/intel/opencl/include
    OCL_LIB=/opt/intel/opencl-1.2-6.4.0.25/lib64
    LD_LIBRARY_PATH=$OCL_LIB:$LD_LIBRARY_PATH

    # openmpi
    apt-get update
    apt-get install -y libibnetdisc-dev
    cd /tmp
    wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz

    tar -xvf openmpi-3.0.0.tar.gz
    cd openmpi-3.0.0
    ./configure --prefix=/usr/local
    make all install

    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda-8.0/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
```

## Collection

 - Name: [ruycastilho/GPUtest](https://github.com/ruycastilho/GPUtest)
 - License: None

