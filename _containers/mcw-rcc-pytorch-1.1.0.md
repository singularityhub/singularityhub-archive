---
id: 10212
name: "mcw-rcc/pytorch"
branch: "1.1.0"
tag: "1.1.0"
commit: "933fbe3a11114fd004b9330aa353284947853cd2"
version: "35813dc8e396bcdb712f6f7089ae001c"
build_date: "2019-07-03T23:17:59.210Z"
size_mb: 5279
size: 2281877535
sif: "https://datasets.datalad.org/shub/mcw-rcc/pytorch/1.1.0/2019-07-03-933fbe3a-35813dc8/35813dc8e396bcdb712f6f7089ae001c.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/pytorch/1.1.0/2019-07-03-933fbe3a-35813dc8/
recipe: https://datasets.datalad.org/shub/mcw-rcc/pytorch/1.1.0/2019-07-03-933fbe3a-35813dc8/Singularity
collection: mcw-rcc/pytorch
---

# mcw-rcc/pytorch:1.1.0

```bash
$ singularity pull shub://mcw-rcc/pytorch:1.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister

%help
This container runs PyTorch 1.1.0.

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
    export PT_BINARY_URL=https://download.pytorch.org/whl/cu90/torch-1.1.0-cp27-cp27mu-linux_x86_64.whl
    pip install --no-cache-dir --ignore-installed --upgrade $PT_BINARY_URL

    # Install python packages
    pip install --no-binary --upgrade \
        dominate \
        torchvision \
        visdom \
        Pillow \
        Augmentor \
        keras \
        tflearn \
        numpy \
        nibabel \
        h5py \
        scikit-learn \
        pandas \
        scipy \
        matplotlib \
        ipykernel \
        jupyter \
        jupyterlab \
        pydicom \
        opencv-python \
        tables \
        tqdm \
        scikit-image

    # Install PyTorch GPU
    export PT_BINARY_URL=https://download.pytorch.org/whl/cu90/torch-1.1.0-cp35-cp35m-linux_x86_64.whl 
    pip3 install --no-cache-dir --ignore-installed --upgrade $PT_BINARY_URL

    # Install python packages
    pip3 install --no-binary --upgrade \
        dominate \
        torchvision \
        visdom \
        Pillow \
        Augmentor \
        keras \
        tflearn \
        numpy \
        nibabel \
        h5py \
        scikit-learn \
        pandas \
        scipy \
        matplotlib \
        ipykernel \
        jupyter \
        jupyterlab \
        pydicom \
        opencv-python \
        tables \
        tqdm \
        scikit-image
```

## Collection

 - Name: [mcw-rcc/pytorch](https://github.com/mcw-rcc/pytorch)
 - License: [MIT License](https://api.github.com/licenses/mit)

