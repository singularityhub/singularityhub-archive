---
id: 4118
name: "AmirMoMo/tensorflow"
branch: "master"
tag: "latest"
commit: "f8792d8195229caadca0653d76175616b45bf5be"
version: "e51ffa19d133b09dc53def20c3f9fb49"
build_date: "2018-09-04T14:36:37.135Z"
size_mb: 6676
size: 3025371167
sif: "https://datasets.datalad.org/shub/AmirMoMo/tensorflow/latest/2018-09-04-f8792d81-e51ffa19/e51ffa19d133b09dc53def20c3f9fb49.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/AmirMoMo/tensorflow/latest/2018-09-04-f8792d81-e51ffa19/
recipe: https://datasets.datalad.org/shub/AmirMoMo/tensorflow/latest/2018-09-04-f8792d81-e51ffa19/Singularity
collection: AmirMoMo/tensorflow
---

# AmirMoMo/tensorflow:latest

```bash
$ singularity pull shub://AmirMoMo/tensorflow:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
#From: nvidia/cuda:8.0-cudnn6-devel
From: nvidia/cuda:9.0-cudnn7-devel

%labels
Maintainer Ismail Elezi

%help
This container runs Tensorflow-GPU.
    
# Add CUDA to the path
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda/lib64
ENV CUDA_HOME /usr/local/cuda

WORKDIR /root

# Pick up some TF dependencies
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cuda-command-line-tools-9-0 \
        cuda-cublas-9-0 \
        cuda-cufft-9-0 \
        cuda-curand-9-0 \
        cuda-cusolver-9-0 \
        cuda-cusparse-9-0 \
        curl \
        libcudnn7=7.1.4.18-1+cuda9.0 \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        rsync \
        software-properties-common \
        unzip
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    
%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    
    # NVIDIA driver mount points
    mkdir /nvidia /cuda
    touch /usr/bin/nvidia-smi

    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
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
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.1-cp27-none-linux_x86_64.whl
    pip install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip install --upgrade keras tflearn numpy nibabel h5py scikit-learn pandas scipy matplotlib ipykernel jupyter image PyYAML pillow easydict

    # Install TensorFlow-GPU
    # export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.1-cp35-cp35m-linux_x86_64.whl
    # pip3 install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL
    pip3 install --upgrade tensorflow-gpu

    # Install python packages
    pip3 install --upgrade keras tflearn numpy nibabel h5py scikit-learn pandas scipy matplotlib ipykernel jupyter

    pip3 install tqdm Augmentor foolbox requests randomgen scikit-image opencv-python
    apt-get install curl
```

## Collection

 - Name: [AmirMoMo/tensorflow](https://github.com/AmirMoMo/tensorflow)
 - License: None

