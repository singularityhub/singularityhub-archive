---
id: 3523
name: "mcw-rcc/pytorch"
branch: "master"
tag: "0.4.0"
commit: "74bdc6257e334696aa0dee206ab6762435a90f26"
version: "7ca6c733bd1d448c979dbeaccd1db690"
build_date: "2018-07-13T21:19:59.509Z"
size_mb: 4034
size: 1718243359
sif: "https://datasets.datalad.org/shub/mcw-rcc/pytorch/0.4.0/2018-07-13-74bdc625-7ca6c733/7ca6c733bd1d448c979dbeaccd1db690.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/pytorch/0.4.0/2018-07-13-74bdc625-7ca6c733/
recipe: https://datasets.datalad.org/shub/mcw-rcc/pytorch/0.4.0/2018-07-13-74bdc625-7ca6c733/Singularity
collection: mcw-rcc/pytorch
---

# mcw-rcc/pytorch:0.4.0

```bash
$ singularity pull shub://mcw-rcc/pytorch:0.4.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version v18.06.06

%help
This container runs PyTorch.

%environment
    # nvidia driver libs specific cuda version libs are mounted by --bind command at run
    # required for GPU enabled container
    SHELL=/bin/bash
    CPATH="/cuda/include:$CPATH"
    PATH="/cuda/bin:/nvidia:$PATH"
    LD_LIBRARY_PATH="/cuda/lib64:/nvidia:$LD_LIBRARY_PATH"
    CUDA_HOME="/cuda"
    export PATH LD_LIBRARY_PATH CPATH CUDA_HOME

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # NVIDIA dirver mount points
    mkdir /nvidia /cuda
    touch /usr/bin/nvidia-smi

    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        libatlas-base-dev \
        libboost-all-dev \
        libhdf5-serial-dev \
        libprotobuf-dev \
        protobuf-compiler \
        libopenblas-dev \
        liblapack-dev \
        gfortran \
        libcurl4-openssl-dev \
        python-pip \
        python3-pip \
        pkg-config \
        python-dev \
        python3-dev \
        python-setuptools \
        python3-setuptools
    apt-get clean

    # Update pip
    pip install --no-cache-dir --upgrade pip==9.0.3
    pip3 install --no-cache-dir --upgrade pip==9.0.3

    # Install PyTorch GPU
    export PT_BINARY_URL=http://download.pytorch.org/whl/cu90/torch-0.4.0-cp27-cp27mu-linux_x86_64.whl
    pip install --no-cache-dir --ignore-installed --upgrade $PT_BINARY_URL

    # Install python packages
    pip install --upgrade dominate torchvision visdom numpy jupyter

    # Install PyTorch GPU
    export PT_BINARY_URL=http://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-linux_x86_64.whl 
    pip3 install --no-cache-dir --ignore-installed --upgrade $PT_BINARY_URL

    # Install python packages
    pip3 install --upgrade dominate torchvision visdom numpy jupyter
```

## Collection

 - Name: [mcw-rcc/pytorch](https://github.com/mcw-rcc/pytorch)
 - License: [MIT License](https://api.github.com/licenses/mit)

