---
id: 1730
name: "UMNAgoe/singularity"
branch: "master"
tag: "latest"
commit: "d2d13a8356ab785295d9508181c45586c0af04cb"
version: "03bfd6d73605efd88c6725f58bd98498"
build_date: "2018-02-16T17:20:20.324Z"
size_mb: 4932
size: 2086461471
sif: "https://datasets.datalad.org/shub/UMNAgoe/singularity/latest/2018-02-16-d2d13a83-03bfd6d7/03bfd6d73605efd88c6725f58bd98498.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/UMNAgoe/singularity/latest/2018-02-16-d2d13a83-03bfd6d7/
recipe: https://datasets.datalad.org/shub/UMNAgoe/singularity/latest/2018-02-16-d2d13a83-03bfd6d7/Singularity
collection: UMNAgoe/singularity
---

# UMNAgoe/singularity:latest

```bash
$ singularity pull shub://UMNAgoe/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.3.0-gpu-py3

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip
    apt-get clean
    apt-get install -y build-essential automake autoconf libtool

    apt-get install -y libcupti-dev
    apt-get install -y cuda-drivers
    pip3 install --upgrade pip
    pip3 install keras
    
    pip3 --no-cache-dir install \
            h5py \
            ipykernel \
            jupyter \
            matplotlib \
            bokeh \
            cython \
            numpy \
            pandas \
            Pillow \
            scipy \
            sklearn \
            odl
    python3 -m ipykernel.kernelspec

    #############################
    # install astra-toolbox
    apt-get install -y libboost-all-dev
    wget https://github.com/astra-toolbox/astra-toolbox/archive/v1.8.3.tar.gz
    tar xzf v1.8.3.tar.gz
    rm v1.8.3.tar.gz
    cd astra-toolbox-1.8.3
    cd build/linux
    ./autogen.sh   # when building a git version
    ./configure --with-cuda=/usr/local/cuda \
            --with-python=/usr/bin/python3 \
            --with-install-type=module
    make
    make install
```

## Collection

 - Name: [UMNAgoe/singularity](https://github.com/UMNAgoe/singularity)
 - License: None

