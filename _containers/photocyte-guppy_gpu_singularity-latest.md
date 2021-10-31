---
id: 13637
name: "photocyte/guppy_gpu_singularity"
branch: "master"
tag: "latest"
commit: "f6b2028b3818868716006f20ae4f69c03febe179"
version: "d0e782d17998256b1814a672a22050a3"
build_date: "2020-09-04T05:45:15.277Z"
size_mb: 4857.0
size: 2690301983
sif: "https://datasets.datalad.org/shub/photocyte/guppy_gpu_singularity/latest/2020-09-04-f6b2028b-d0e782d1/d0e782d17998256b1814a672a22050a3.sif"
url: https://datasets.datalad.org/shub/photocyte/guppy_gpu_singularity/latest/2020-09-04-f6b2028b-d0e782d1/
recipe: https://datasets.datalad.org/shub/photocyte/guppy_gpu_singularity/latest/2020-09-04-f6b2028b-d0e782d1/Singularity
collection: photocyte/guppy_gpu_singularity
---

# photocyte/guppy_gpu_singularity:latest

```bash
$ singularity pull shub://photocyte/guppy_gpu_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

%labels
MAINTAINER Timothy R. Fallon 

%files

%environment

%post
    PACKAGE_VERSION=4.0.14
    BUILD_PACKAGES="wget apt-utils apt-transport-https"
    DEBIAN_FRONTEND=noninteractive
    PACKAGE_NAME=ont_guppy_${PACKAGE_VERSION}-1~bionic_amd64.deb

    apt-get update
    apt-get install --yes $BUILD_PACKAGES
    apt-get install --yes locales
    locale-gen "en_US.UTF-8"
    dpkg-reconfigure locales
    
    ### guppy dependencies
    apt-get install --yes libzmq5 \
	libhdf5-cpp-100 \
	libboost-atomic1.65.1 \
        libboost-chrono1.65.1 \
        libboost-date-time1.65.1 \
        libboost-filesystem1.65.1 \
        libboost-iostreams1.65.1 \
        libboost-program-options1.65.1 \
        libboost-regex1.65.1 \
        libboost-system1.65.1 \
        libboost-log1.65.1 \
        libcurl4
	
    ### For nvtop https://github.com/Syllo/nvtop
    #cd /tmp
    #apt-get install --yes libncurses5-dev \
    # libncursesw5-dev cmake git
    #git clone https://github.com/Syllo/nvtop.git
    #mkdir -p nvtop/build && cd nvtop/build
    #cmake .. -DNVML_RETRIEVE_HEADER_ONLINE=True
    #make
    #make install
    ### 
    
    ### For guppy
    cd /tmp
    wget -q https://mirror.oxfordnanoportal.com/software/analysis/${PACKAGE_NAME}
    dpkg -I ${PACKAGE_NAME} ##Print some information about the package dependencies
    dpkg -i --ignore-depends=nvidia-driver-418,libcuda1-418 /tmp/${PACKAGE_NAME}
    ###
    
    ### Cleanup
    rm -f *.deb
    apt-get autoremove --purge --yes
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    
%runscript
```

## Collection

 - Name: [photocyte/guppy_gpu_singularity](https://github.com/photocyte/guppy_gpu_singularity)
 - License: None

