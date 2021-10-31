---
id: 1712
name: "ozanarkancan/ReGROUND"
branch: "master"
tag: "dgen"
commit: "2356e9a8a628a9ba86d814acd9b5001432661c3f"
version: "5b59c7f602577ae39ae7ade824ab9a01"
build_date: "2018-02-13T08:25:31.587Z"
size_mb: 2338
size: 715391007
sif: "https://datasets.datalad.org/shub/ozanarkancan/ReGROUND/dgen/2018-02-13-2356e9a8-5b59c7f6/5b59c7f602577ae39ae7ade824ab9a01.simg"
url: https://datasets.datalad.org/shub/ozanarkancan/ReGROUND/dgen/2018-02-13-2356e9a8-5b59c7f6/
recipe: https://datasets.datalad.org/shub/ozanarkancan/ReGROUND/dgen/2018-02-13-2356e9a8-5b59c7f6/Singularity
collection: ozanarkancan/ReGROUND
---

# ozanarkancan/ReGROUND:dgen

```bash
$ singularity pull shub://ozanarkancan/ReGROUND:dgen
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty

%environment
    export LANG=C.UTF-8 
    export LC_ALL=C.UTF-8
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib:/usr/local/lib

%post
	apt-get update && apt-get install --no-install-recommends -y \
     libreadline6 \
     libreadline6-dev \
     libncurses5-dev \
     libgmp3-dev \
     libgsl0-dev \
     libgsl0ldbl \
     libboost-all-dev \
     build-essential \
     gdb \
     git \
     vim \
     libxml2 \
     wget \
     curl \
     cmake \
     software-properties-common

    apt-add-repository restricted
    apt-add-repository universe
    apt-add-repository multiverse
    add-apt-repository ppa:ubuntu-toolchain-r/test
    
    apt-get update && apt-get install --no-install-recommends -y \
     g++-4.9 \
     dirmngr \
     gnupg2 \
     && rm -rf /var/lib/apt/lists/*

    echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
	apt-get update && apt-get install --no-install-recommends -y \
     python-rosdep \
     python-rosinstall \
     python-vcstools \
     libgl1-mesa-dev-lts-trusty \
     && rm -rf /var/lib/apt/lists/*

    export LANG=C.UTF-8 
    export LC_ALL=C.UTF-8

    apt-get update
	apt-get install --no-install-recommends -y ros-indigo-desktop-full
	rosdep init
	rosdep update

    cd /bin
    wget http://www.dcc.fc.up.pt/~vsc/Yap/yap-6.2.2.tar.gz
    tar -xzvf /bin/yap-6.2.2.tar.gz \
    && mkdir -p /bin/yap-6.2.2/arch
    cd /bin/yap-6.2.2/arch
    ../configure --enable-tabling=yes --enable-dynamic-loading \
    && make \
    && make install \
    && make install_library \

    mkdir -p /workdir/rg/src
    chmod -R 777 /workdir
```

## Collection

 - Name: [ozanarkancan/ReGROUND](https://github.com/ozanarkancan/ReGROUND)
 - License: None

