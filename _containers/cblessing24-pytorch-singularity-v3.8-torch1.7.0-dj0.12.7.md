---
id: 15084
name: "cblessing24/pytorch-singularity"
branch: "main"
tag: "v3.8-torch1.7.0-dj0.12.7"
commit: "0c96d7655c052ffc73924e9c71ea530872b7f34b"
version: "003ab62c995e7e02f9ebc2c5de0b3dba35d6a768afb042853a29da37e5e9e4ec"
build_date: "2021-02-05T18:09:03.306Z"
size_mb: 1502.4921875
size: 1575477248
sif: "https://datasets.datalad.org/shub/cblessing24/pytorch-singularity/v3.8-torch1.7.0-dj0.12.7/2021-02-05-0c96d765-003ab62c/003ab62c995e7e02f9ebc2c5de0b3dba35d6a768afb042853a29da37e5e9e4ec.sif"
url: https://datasets.datalad.org/shub/cblessing24/pytorch-singularity/v3.8-torch1.7.0-dj0.12.7/2021-02-05-0c96d765-003ab62c/
recipe: https://datasets.datalad.org/shub/cblessing24/pytorch-singularity/v3.8-torch1.7.0-dj0.12.7/2021-02-05-0c96d765-003ab62c/Singularity
collection: cblessing24/pytorch-singularity
---

# cblessing24/pytorch-singularity:v3.8-torch1.7.0-dj0.12.7

```bash
$ singularity pull shub://cblessing24/pytorch-singularity:v3.8-torch1.7.0-dj0.12.7
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
        Pillow==8.0.1 \
        jupyterlab \
        datajoint==0.12.7
    
    python3.8 -m pip --no-cache-dir  install \
        torch==1.7.0+cu110 \
        torchvision==0.8.1+cu110 \
        torchaudio==0.7.0 \
        -f https://download.pytorch.org/whl/torch_stable.html

%environment
    export SHELL=/bin/sh

%runscript
    exec /bin/sh "$@"

%startscript
    jupyter lab
```

## Collection

 - Name: [cblessing24/pytorch-singularity](https://github.com/cblessing24/pytorch-singularity)
 - License: None

