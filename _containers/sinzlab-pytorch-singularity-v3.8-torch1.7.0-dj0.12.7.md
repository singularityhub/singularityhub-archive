---
id: 15087
name: "sinzlab/pytorch-singularity"
branch: "main"
tag: "v3.8-torch1.7.0-dj0.12.7"
commit: "cf8f39510fc80a9c4c9af70e032fac9608d47ca3"
version: "e753317c171f13ffa5a52a77b53ac62648402396896cc38ced8eb4b6912d8b74"
build_date: "2021-04-19T21:16:53.275Z"
size_mb: 1548.93359375
size: 1624174592
sif: "https://datasets.datalad.org/shub/sinzlab/pytorch-singularity/v3.8-torch1.7.0-dj0.12.7/2021-04-19-cf8f3951-e753317c/e753317c171f13ffa5a52a77b53ac62648402396896cc38ced8eb4b6912d8b74.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sinzlab/pytorch-singularity/v3.8-torch1.7.0-dj0.12.7/2021-04-19-cf8f3951-e753317c/
recipe: https://datasets.datalad.org/shub/sinzlab/pytorch-singularity/v3.8-torch1.7.0-dj0.12.7/2021-04-19-cf8f3951-e753317c/Singularity
collection: sinzlab/pytorch-singularity
---

# sinzlab/pytorch-singularity:v3.8-torch1.7.0-dj0.12.7

```bash
$ singularity pull shub://sinzlab/pytorch-singularity:v3.8-torch1.7.0-dj0.12.7
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
    exec /bin/sh -c "$@"

%startscript
    jupyter lab
```

## Collection

 - Name: [sinzlab/pytorch-singularity](https://github.com/sinzlab/pytorch-singularity)
 - License: None

