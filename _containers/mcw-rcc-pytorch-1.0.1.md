---
id: 7470
name: "mcw-rcc/pytorch"
branch: "1.0.1"
tag: "1.0.1"
commit: "c51f38d3adf8a8374d076a73029ba4ea65dd4f51"
version: "e7c43ef18cc015bc1942f331f05cb8bd"
build_date: "2020-06-08T20:04:54.855Z"
size_mb: 4852
size: 2128818207
sif: "https://datasets.datalad.org/shub/mcw-rcc/pytorch/1.0.1/2020-06-08-c51f38d3-e7c43ef1/e7c43ef18cc015bc1942f331f05cb8bd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/pytorch/1.0.1/2020-06-08-c51f38d3-e7c43ef1/
recipe: https://datasets.datalad.org/shub/mcw-rcc/pytorch/1.0.1/2020-06-08-c51f38d3-e7c43ef1/Singularity
collection: mcw-rcc/pytorch
---

# mcw-rcc/pytorch:1.0.1

```bash
$ singularity pull shub://mcw-rcc/pytorch:1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister

%help
This container runs PyTorch 1.0.1.

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
    export PT_BINARY_URL=https://download.pytorch.org/whl/cu90/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl
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
    export PT_BINARY_URL=https://download.pytorch.org/whl/cu90/torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl 
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

