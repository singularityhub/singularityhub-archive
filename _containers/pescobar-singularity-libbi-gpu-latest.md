---
id: 11140
name: "pescobar/singularity-libbi-gpu"
branch: "master"
tag: "latest"
commit: "8d964e66c4bd3cae6891815fcdb2fc5d66507481"
version: "b15760b912ce2a370822845e89f3dc24"
build_date: "2020-02-26T12:38:40.264Z"
size_mb: 4125.0
size: 2253307935
sif: "https://datasets.datalad.org/shub/pescobar/singularity-libbi-gpu/latest/2020-02-26-8d964e66-b15760b9/b15760b912ce2a370822845e89f3dc24.sif"
url: https://datasets.datalad.org/shub/pescobar/singularity-libbi-gpu/latest/2020-02-26-8d964e66-b15760b9/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-libbi-gpu/latest/2020-02-26-8d964e66-b15760b9/Singularity
collection: pescobar/singularity-libbi-gpu
---

# pescobar/singularity-libbi-gpu:latest

```bash
$ singularity pull shub://pescobar/singularity-libbi-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04

%environment
    LC_ALL=C
    export LC_ALL
    # workaround for https://stackoverflow.com/a/30663908
    CXX="g++ -std=c++11"
    export CXX
    
%post
    export LC_ALL=C
    # Update list of available packages, then upgrade them
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

    # Install Libbi dependencies
    DEBIAN_FRONTEND=noninteractive apt-get -y install \
    libblas-dev \
    liblapack-dev \
    libqrupdate-dev \
    libboost-all-dev \
    libgsl0-dev \
    libnetcdf-dev \
    autoconf \
    automake \
    wget

    # download and install LibBi
    export LIBBI_VERSION=1.4.5
    cd /usr/local/src
    wget -O libbi-${LIBBI_VERSION}.tar.gz -nc https://github.com/lawmurray/LibBi/archive/${LIBBI_VERSION}.tar.gz
    tar -xf libbi-${LIBBI_VERSION}.tar.gz
    cd /usr/local/src/LibBi-${LIBBI_VERSION}/
    # reply yes in perl. required to use cpan in non interactive session 
    export PERL_MM_USE_DEFAULT=1
    cpan .

%runscript
    /usr/local/bin/libbi "$@"

%apprun libbi
    /usr/local/bin/libbi "$@"
```

## Collection

 - Name: [pescobar/singularity-libbi-gpu](https://github.com/pescobar/singularity-libbi-gpu)
 - License: None

