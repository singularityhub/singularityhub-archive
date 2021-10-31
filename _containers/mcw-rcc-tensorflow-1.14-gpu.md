---
id: 9902
name: "mcw-rcc/tensorflow"
branch: "1.14-gpu"
tag: "1.14-gpu"
commit: "22684bd06c715bbd445c3a732dbaf3206bb2ebaf"
version: "f0f3ec92284cb15b1c80137b315f8ed8"
build_date: "2020-08-31T12:06:55.780Z"
size_mb: 5776
size: 1855782943
sif: "https://datasets.datalad.org/shub/mcw-rcc/tensorflow/1.14-gpu/2020-08-31-22684bd0-f0f3ec92/f0f3ec92284cb15b1c80137b315f8ed8.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/tensorflow/1.14-gpu/2020-08-31-22684bd0-f0f3ec92/
recipe: https://datasets.datalad.org/shub/mcw-rcc/tensorflow/1.14-gpu/2020-08-31-22684bd0-f0f3ec92/Singularity
collection: mcw-rcc/tensorflow
---

# mcw-rcc/tensorflow:1.14-gpu

```bash
$ singularity pull shub://mcw-rcc/tensorflow:1.14-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 1.14-gpu

%help
This container runs TensorFlow-GPU 1.14.

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
        python3-setuptools \
        python-tk \
        python3-tk 
    apt-get clean

    # Update pip
    pip install --no-cache-dir --upgrade pip==9.0.3
    pip3 install --no-cache-dir --upgrade pip==9.0.3

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.14.0-cp27-none-linux_x86_64.whl
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
        scikit-image \
        SimpleITK

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.14.0-cp35-cp35m-linux_x86_64.whl
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
        scikit-image \
        SimpleITK
```

## Collection

 - Name: [mcw-rcc/tensorflow](https://github.com/mcw-rcc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

