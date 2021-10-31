---
id: 14852
name: "cblessing24/pytorch-singularity"
branch: "main"
tag: "v3.8-torch1.5.0-dj0.12.4"
commit: "3d2eec3aa4601d72a91eea950e8f3078f1647b5c"
version: "87bff008fc6935c576f37bb754b079373c8b3dc9304e739f74e1d63f66b5b5b9"
build_date: "2020-12-08T13:22:32.355Z"
size_mb: 1121.3203125
size: 1175789568
sif: "https://datasets.datalad.org/shub/cblessing24/pytorch-singularity/v3.8-torch1.5.0-dj0.12.4/2020-12-08-3d2eec3a-87bff008/87bff008fc6935c576f37bb754b079373c8b3dc9304e739f74e1d63f66b5b5b9.sif"
url: https://datasets.datalad.org/shub/cblessing24/pytorch-singularity/v3.8-torch1.5.0-dj0.12.4/2020-12-08-3d2eec3a-87bff008/
recipe: https://datasets.datalad.org/shub/cblessing24/pytorch-singularity/v3.8-torch1.5.0-dj0.12.4/2020-12-08-3d2eec3a-87bff008/Singularity
collection: cblessing24/pytorch-singularity
---

# cblessing24/pytorch-singularity:v3.8-torch1.5.0-dj0.12.4

```bash
$ singularity pull shub://cblessing24/pytorch-singularity:v3.8-torch1.5.0-dj0.12.4
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04

%labels
MAINTAINER Christoph Blessing <chris24.blessing@gmail.com>

%post
    apt update && apt install -y software-properties-common
    add-apt-repository universe

    apt update && apt install -y \
        build-essential \
        git \
        wget \
        vim \
        curl \
        zip \
        zlib1g-dev \
        unzip \
        pkg-config \
        libblas-dev \
        liblapack-dev \
        python3-tk \
        python3-wheel \
        graphviz \
        libhdf5-dev \
        python3.8 \
        python3.8-dev \
        python3.8-distutils \
        swig
    apt-get clean

    ln -s /usr/bin/python3.8 /usr/local/bin/python
    ln -s /usr/bin/python3.8 /usr/local/bin/python3

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.8 get-pip.py
    rm get-pip.py

    python3.8 -m pip --no-cache-dir install \
        blackcellmagic\
        pytest \
        pytest-cov \
        numpy \
        matplotlib \
        scipy \
        pandas \
        jupyter \
        scikit-learn \
        scikit-image \
        seaborn \
        graphviz \
        gpustat \
        h5py \
        gitpython \
        Pillow==6.2.0 \
        torch==1.5.0 \
        torchvision==0.6.0 \
        jupyterlab \
        datajoint==0.12.4

%environment
    export SHELL=/bin/sh

%runscript
    jupyter lab
```

## Collection

 - Name: [cblessing24/pytorch-singularity](https://github.com/cblessing24/pytorch-singularity)
 - License: None

