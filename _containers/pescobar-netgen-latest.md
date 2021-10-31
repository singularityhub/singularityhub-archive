---
id: 540
name: "pescobar/netgen"
branch: "master"
tag: "latest"
commit: "8ea4ae5b072a3ab5df5908285f2fddd87486960a"
version: "df287205927d59d0bb1acf1e6e5dcd84"
build_date: "2018-03-04T20:03:49.300Z"
size_mb: 745
size: 251428895
sif: "https://datasets.datalad.org/shub/pescobar/netgen/latest/2018-03-04-8ea4ae5b-df287205/df287205927d59d0bb1acf1e6e5dcd84.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/netgen/latest/2018-03-04-8ea4ae5b-df287205/
recipe: https://datasets.datalad.org/shub/pescobar/netgen/latest/2018-03-04-8ea4ae5b-df287205/Singularity
collection: pescobar/netgen
---

# pescobar/netgen:latest

```bash
$ singularity pull shub://pescobar/netgen:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install locales curl
    locale-gen en_US.UTF-8
    apt-get -y install tcl8.5-dev tk8.5-dev libtogl-dev mesa-common-dev libglu1-mesa-dev libxmu-dev tix-dev
    apt-get clean
    curl -sSL -O "https://sourceforge.net/projects/netgen-mesher/files/netgen-mesher/5.3/netgen-5.3.1.tar.gz"
    tar xf netgen-5.3.1.tar.gz
    cd netgen-*
    ./configure --with-tcl=/usr/lib/tcl8.5/ --with-tk=/usr/lib/tk8.5/
    make
    make install

%environment
    LANG=en_US.UTF-8
    LANGUAGE=en_US:en
    LC_ALL=en_US.UTF-8
    export LANG LANGUAGE LC_ALL
    export LD_LIBRARY_PATH=/opt/netgen/lib:$LD_LIBRARY_PATH
    export PATH=/opt/netgen/bin:$PATH
    export NETGENDIR=/opt/netgen/bin

%runscript
    netgen
```

## Collection

 - Name: [pescobar/netgen](https://github.com/pescobar/netgen)
 - License: None

