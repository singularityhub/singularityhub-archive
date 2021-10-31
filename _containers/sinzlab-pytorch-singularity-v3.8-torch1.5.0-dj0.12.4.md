---
id: 14868
name: "sinzlab/pytorch-singularity"
branch: "main"
tag: "v3.8-torch1.5.0-dj0.12.4"
commit: "68ad66e0044fe38ea9511adbe006a3d4dcf417b0"
version: "2d8a2780b76d7d9004c72f3326a47bfab1ad7b3177a41ad6232ea1ed72171c60"
build_date: "2021-04-01T13:22:08.492Z"
size_mb: 1121.45703125
size: 1175932928
sif: "https://datasets.datalad.org/shub/sinzlab/pytorch-singularity/v3.8-torch1.5.0-dj0.12.4/2021-04-01-68ad66e0-2d8a2780/2d8a2780b76d7d9004c72f3326a47bfab1ad7b3177a41ad6232ea1ed72171c60.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sinzlab/pytorch-singularity/v3.8-torch1.5.0-dj0.12.4/2021-04-01-68ad66e0-2d8a2780/
recipe: https://datasets.datalad.org/shub/sinzlab/pytorch-singularity/v3.8-torch1.5.0-dj0.12.4/2021-04-01-68ad66e0-2d8a2780/Singularity
collection: sinzlab/pytorch-singularity
---

# sinzlab/pytorch-singularity:v3.8-torch1.5.0-dj0.12.4

```bash
$ singularity pull shub://sinzlab/pytorch-singularity:v3.8-torch1.5.0-dj0.12.4
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

 - Name: [sinzlab/pytorch-singularity](https://github.com/sinzlab/pytorch-singularity)
 - License: None

