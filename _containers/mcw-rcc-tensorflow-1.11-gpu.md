---
id: 5511
name: "mcw-rcc/tensorflow"
branch: "1.11-gpu"
tag: "1.11-gpu"
commit: "da2d8d1214071f46d01a0649cb099f23e82e0504"
version: "f9f848d51f7b4ef40cf2972edd0baa6f"
build_date: "2020-09-01T16:39:46.899Z"
size_mb: 4647
size: 1471762463
sif: "https://datasets.datalad.org/shub/mcw-rcc/tensorflow/1.11-gpu/2020-09-01-da2d8d12-f9f848d5/f9f848d51f7b4ef40cf2972edd0baa6f.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/tensorflow/1.11-gpu/2020-09-01-da2d8d12-f9f848d5/
recipe: https://datasets.datalad.org/shub/mcw-rcc/tensorflow/1.11-gpu/2020-09-01-da2d8d12-f9f848d5/Singularity
collection: mcw-rcc/tensorflow
---

# mcw-rcc/tensorflow:1.11-gpu

```bash
$ singularity pull shub://mcw-rcc/tensorflow:1.11-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 11.06.18

%help
This container runs Tensorflow-GPU 1.11.

%environment
    # nvidia driver libs specific cuda version libs are mounted by --bind command at run
    # required for GPU enabled container
    SHELL=/bin/bash
    CPATH="/cuda/include:$CPATH"
    PATH="/cuda/bin:/nvidia:$PATH"
    LD_LIBRARY_PATH="/cuda/lib64:/nvidia:$LD_LIBRARY_PATH"
    CUDA_HOME="/cuda"
    LC_ALL="C"
    export PATH LD_LIBRARY_PATH CPATH CUDA_HOME LC_ALL

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    
    # NVIDIA driver mount points
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

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.11.0-cp27-none-linux_x86_64.whl
    pip install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip install --no-binary --upgrade \
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

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.11.0-cp35-cp35m-linux_x86_64.whl
    pip3 install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip3 install --no-binary --upgrade \
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

 - Name: [mcw-rcc/tensorflow](https://github.com/mcw-rcc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

