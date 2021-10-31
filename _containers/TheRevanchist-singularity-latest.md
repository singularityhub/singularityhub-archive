---
id: 5625
name: "TheRevanchist/singularity"
branch: "master"
tag: "latest"
commit: "fce4cd998007eb44f6668173762187e224a21a8c"
version: "2f934eda95acbbbf1eabdc31e92c4d5f"
build_date: "2018-11-17T04:47:34.261Z"
size_mb: 6168
size: 2421297183
sif: "https://datasets.datalad.org/shub/TheRevanchist/singularity/latest/2018-11-17-fce4cd99-2f934eda/2f934eda95acbbbf1eabdc31e92c4d5f.simg"
url: https://datasets.datalad.org/shub/TheRevanchist/singularity/latest/2018-11-17-fce4cd99-2f934eda/
recipe: https://datasets.datalad.org/shub/TheRevanchist/singularity/latest/2018-11-17-fce4cd99-2f934eda/Singularity
collection: TheRevanchist/singularity
---

# TheRevanchist/singularity:latest

```bash
$ singularity pull shub://TheRevanchist/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-cudnn6-devel

%labels
Maintainer Ismail Elezi

%help
This container runs Tensorflow-GPU.
    
# Add CUDA to the path
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda/lib64
ENV CUDA_HOME /usr/local/cuda

WORKDIR /root
    

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    
    # NVIDIA driver mount points
    mkdir /nvidia /cuda
    touch /usr/bin/nvidia-smi

    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        tmux \
        vim \
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
        python3-setuptools\
        python-opencv \
        python-tk \
        libjpeg-dev \
        libfreetype6 \
        libfreetype6-dev \
        zlib1g-dev \
        cmake \
        wget \
        cython \
        git
    apt-get clean

    # Update pip
    pip install --no-cache-dir --upgrade pip==9.0.3
    pip3 install --no-cache-dir --upgrade pip==9.0.3

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.12.0-cp27-none-linux_x86_64.whl
    pip install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip install --upgrade keras tflearn numpy nibabel h5py scikit-learn pandas scipy matplotlib ipykernel jupyter image PyYAML pillow easydict

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.12.0-cp35-cp35m-linux_x86_64.whl
    pip3 install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip3 install --upgrade keras tflearn numpy nibabel h5py scikit-learn pandas scipy matplotlib ipykernel jupyter
    
    pip install absl-py
    pip3 install absl-py
```

## Collection

 - Name: [TheRevanchist/singularity](https://github.com/TheRevanchist/singularity)
 - License: None

