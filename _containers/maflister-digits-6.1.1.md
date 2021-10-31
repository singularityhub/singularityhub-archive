---
id: 2583
name: "maflister/digits"
branch: "master"
tag: "6.1.1"
commit: "855890ef519a2bd58ad4d3988fd2cedf9879e516"
version: "b02de7d7af1b91d0a5b3c7194224697d"
build_date: "2019-08-26T18:12:12.105Z"
size_mb: 4672
size: 1654657055
sif: "https://datasets.datalad.org/shub/maflister/digits/6.1.1/2019-08-26-855890ef-b02de7d7/b02de7d7af1b91d0a5b3c7194224697d.simg"
url: https://datasets.datalad.org/shub/maflister/digits/6.1.1/2019-08-26-855890ef-b02de7d7/
recipe: https://datasets.datalad.org/shub/maflister/digits/6.1.1/2019-08-26-855890ef-b02de7d7/Singularity
collection: maflister/digits
---

# maflister/digits:6.1.1

```bash
$ singularity pull shub://maflister/digits:6.1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version v1.0

%help
This container runs DIGITS server.

%environment
    # nvidia driver libs specific cuda version libs are mounted by --bind command at run
    # required for GPU enabled container
    SHELL=/bin/bash
    CPATH="/cuda/include:$CPATH"
    PATH="/cuda/bin:/nvidia:$PATH"
    LD_LIBRARY_PATH="/cuda/lib64:/nvidia:$LD_LIBRARY_PATH"
    CUDA_HOME="/cuda"
    CAFFE_ROOT="/caffe"
    DIGITS_JOBS_DIR="/scratch/global/$USER/$PBS_JOBID"
    export PATH LD_LIBRARY_PATH CPATH CUDA_HOME CAFFE_ROOT DIGITS_JOBS_DIR

%files
    Makefile.config /root

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    mkdir /cuda /nvidia
    touch /usr/bin/nvidia-smi

    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        libatlas-base-dev \
        libboost-all-dev \
        libhdf5-serial-dev \
        libprotobuf-dev \
        libsnappy-dev \
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
        python3-tk \
        libopencv-dev \
        python-opencv \
        libhdf5-serial-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libleveldb-dev \
        liblmdb-dev \
        wget \
        git \
        cmake
    apt-get clean

    # Update pip
    pip install --no-cache-dir --upgrade pip==9.0.3
    pip3 install --no-cache-dir --upgrade pip==9.0.3

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.8.0-cp27-none-linux_x86_64.whl
    pip install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip install --upgrade keras tflearn numpy nibabel h5py scikit-learn pandas scipy matplotlib

    # Install TensorFlow-GPU
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.8.0-cp35-cp35m-linux_x86_64.whl
    pip3 install --no-cache-dir --ignore-installed --upgrade $TF_BINARY_URL

    # Install python packages
    pip3 install --upgrade keras tflearn numpy nibabel h5py scikit-learn pandas scipy matplotlib

    # Install caffe
    mkdir /caffe
    git clone https://github.com/nvidia/caffe.git /caffe -b 'caffe-0.15'
    cd /caffe
    cp /root/Makefile.config .
    pip install ipython==5.4.1
    pip install -r python/requirements.txt
    mkdir build
    cd build
    cmake .. -DUSE_CUDNN=ON
    make
    make install
    make pycaffe
    cd /

    # Install DIGITS
    #wget https://github.com/NVIDIA/DIGITS/archive/v6.1.1.tar.gz
    pip install https://github.com/NVIDIA/DIGITS/archive/v6.1.1.tar.gz
    #tar -xvf v6.1.1.tar.gz
    #cd DIGITS-6.1.1 && pip install -r requirements.txt && pip install .
```

## Collection

 - Name: [maflister/digits](https://github.com/maflister/digits)
 - License: None

