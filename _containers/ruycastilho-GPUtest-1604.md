---
id: 1141
name: "ruycastilho/GPUtest"
branch: "master"
tag: "1604"
commit: "b178aa0b2d63480bf54cb571c8bd12e297487d67"
version: "adcfa0d7301a17f1897d58fa8d18fb79"
build_date: "2020-06-11T10:06:41.853Z"
size_mb: 2761
size: 1279733791
sif: "https://datasets.datalad.org/shub/ruycastilho/GPUtest/1604/2020-06-11-b178aa0b-adcfa0d7/adcfa0d7301a17f1897d58fa8d18fb79.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ruycastilho/GPUtest/1604/2020-06-11-b178aa0b-adcfa0d7/
recipe: https://datasets.datalad.org/shub/ruycastilho/GPUtest/1604/2020-06-11-b178aa0b-adcfa0d7/Singularity
collection: ruycastilho/GPUtest
---

# ruycastilho/GPUtest:1604

```bash
$ singularity pull shub://ruycastilho/GPUtest:1604
```

## Singularity Recipe

```singularity
# Automatic

BootStrap: docker
From: nvidia/cuda:9.0-devel

# change to cuda-9.0 for Volta
%post
    apt-get update
    apt-get -y install build-essential
    apt-get -y install apt-utils
    apt-get -y install make
    apt-get -y install git
    mkdir /dev/fuse 
    chmod 777 /dev/fuse
    apt-get -y install fuse
	apt-get -y install wget

    cd /tmp
    wget -q "https://cmake.org/files/v3.10/cmake-3.10.1.tar.gz"
    tar -xvf cmake-3.10.1.tar.gz
    cd cmake-3.10.1/
    ./configure
    make --silent
    make install --silent
    
#    wget -q http://download.pgroup.com/secure/pgilinux-2017-1710-x86_64.tar.gz?XackFE9SNRu1LmnSo37o6L2Q5fwXF-IfHjT0ApipA7A-T69ZiIvpwoHcLh4hRF0dbPY383-UKsxoWeF1WXyom9y5UUeusKFWhbJ_d69QU24FS_2TT7-6peQ6wzhEc5D802_Tmx08
#    mv pgilinux-2017-1710-x86_64.tar.gz?XackFE9SNRu1LmnSo37o6L2Q5fwXF-IfHjT0ApipA7A-T69ZiIvpwoHcLh4hRF0dbPY383-UKsxoWeF1WXyom9y5UUeusKFWhbJ_d69QU24FS_2TT7-6peQ6wzhEc5D802_Tmx08 pgilinux-2017-1710-x86_64.tar.gz
#    tar xpfz pgilinux-2017-1710-x86_64.tar.gz
#    export PGI_SILENT=true
#    export PGI_ACCEPT_EULA=true
#    export PGI_INSTALL_DIR=/opt/pgi/
#    export PGI_INSTALL_TYPE=single
#    export PGI_INSTALL_NVIDIA=true
#    export PGI_INSTALL_JAVA=true
#    export PGI_INSTALL_MPI=true
#    export PGI_MPI_GPU_SUPPORT=true
#    ./install
    cd

    apt-get -y install flex
    apt-get -y install automake
    apt-get -y install autoconf
    apt-get -y install autotools-dev
    apt-get -y install libtool

    apt-get -y install software-properties-common  
    add-apt-repository -y ppa:jonathonf/gcc-7.2
    apt-get update
    apt-get -y install gcc-7 g++-7

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

    apt-get install opencl-headers

    # openmpi
    apt-get update
    apt-get install -y libibnetdisc-dev
    cd /tmp
    wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz

    tar -xvf openmpi-3.0.0.tar.gz
    cd openmpi-3.0.0
    ./configure --prefix=/usr/local
    make all install

    export PGI=/opt/pgi
    export LM_LICENSE_FILE=/opt/pgi/license.dat
    export MANPATH=/opt/pgi/linux86-64/17.10/man:/opt/pgi/linux86-64/17.10/mpi/openmpi/man:
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda-8.0/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export PATH=/usr/local/cuda-9.0/bin:/opt/pgi/linux86-64/17.10/bin:/opt/pgi/linux86-64/17.10/bin:/opt/pgi/linux86-64/17.10/mpi/openmpi/bin:${PATH:+:${PATH}}
```

## Collection

 - Name: [ruycastilho/GPUtest](https://github.com/ruycastilho/GPUtest)
 - License: None

