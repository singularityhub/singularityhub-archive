---
id: 7920
name: "51N84D/G3DNet_Singularity"
branch: "master"
tag: "latest"
commit: "9d9e777730c57c5bc6f21a2e8bf5db27da9eb1d7"
version: "9423a775f9c38e41fb6c48226498a501"
build_date: "2019-03-24T08:12:38.536Z"
size_mb: 4582
size: 2275192863
sif: "https://datasets.datalad.org/shub/51N84D/G3DNet_Singularity/latest/2019-03-24-9d9e7777-9423a775/9423a775f9c38e41fb6c48226498a501.simg"
url: https://datasets.datalad.org/shub/51N84D/G3DNet_Singularity/latest/2019-03-24-9d9e7777-9423a775/
recipe: https://datasets.datalad.org/shub/51N84D/G3DNet_Singularity/latest/2019-03-24-9d9e7777-9423a775/Singularity
collection: 51N84D/G3DNet_Singularity
---

# 51N84D/G3DNet_Singularity:latest

```bash
$ singularity pull shub://51N84D/G3DNet_Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-devel-ubuntu16.04
# -----------------------------------------------------------------------------------
# This is a port of the Dockerfile maintained at https://github.com/uber/horovod


%environment
# -----------------------------------------------------------------------------------

    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/lib/.libs
    export LC_ALL=C
    export HOROVOD_GPU_ALLREDUCE=NCCL
    export HOROVOD_GPU_ALLGATHER=MPI
    export HOROVOD_GPU_BROADCAST=MPI
    export HOROVOD_NCCL_HOME=/usr/local/cuda/nccl
    export HOROVOD_NCCL_INCLUDE=/usr/local/cuda/nccl/include
    export HOROVOD_NCCL_LIB=/usr/local/cuda/nccl/lib 
    export PYTHON_VERSION=2.7
    export TENSORFLOW_VERSION=1.11.0

    export CUDNN_VERSION=7.3.1.20-1+cuda9.0
    export NCCL_VERSION=2.3.5-2+cuda9.0

%post
# -----------------------------------------------------------------------------------
# this will install all necessary packages and prepare the container

# TensorFlow version is tightly coupled to CUDA and cuDNN so it should be selected carefully
# Python 2.7 or 3.5 is supported by Ubuntu Xenial out of the box


    export PYTHON_VERSION=2.7
    export TENSORFLOW_VERSION=1.11.0
 
    export CUDNN_VERSION=7.3.1.20-1+cuda9.0
    export NCCL_VERSION=2.3.5-2+cuda9.0

    echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

    apt-get -y update && apt-get install -y --no-install-recommends --allow-downgrades --allow-change-held-packages \
        build-essential \
        cmake \
        git \
        curl \
        vim \
        wget \
        ca-certificates \
        libcudnn7=${CUDNN_VERSION} \
        libnccl2=${NCCL_VERSION} \
        libnccl-dev=${NCCL_VERSION} \
        libjpeg-dev \
        libpng-dev \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev

    ln -s /usr/bin/python${PYTHON_VERSION} /usr/bin/python

    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Install TensorFlow, Keras and PyTorch
    pip install tensorflow-gpu==${TENSORFLOW_VERSION} keras
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools
    pip --no-cache-dir --disable-pip-version-check install future
    pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  # for python2.7
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook
    pip --no-cache-dir --disable-pip-version-check install transforms3d
    pip --no-cache-dir --disable-pip-version-check install pyamg


# Install the IB verbs
    apt install -y --no-install-recommends libibverbs*
    apt install -y --no-install-recommends ibverbs-utils librdmacm* infiniband-diags libmlx4* libmlx5* libnuma*

# install MPICH
   MPICH_VERSION=3.2.1
   mkdir /mpich
   cd /mpich
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1

   # disable the addition of the RPATH to compiled executables
   # this allows us to override the MPI libraries to use those
   # found via LD_LIBRARY_PATH
   ./configure --prefix=/mpich/install --disable-wrapper-rpath --disable-fortran
   make -j 4 install
   # add to local environment to build pi.c
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib

# Install Horovod, temporarily using CUDA stubs
    ldconfig /usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs && \
    HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_WITH_TENSORFLOW=1 pip install --no-cache-dir horovod && \
    ldconfig

# Set default NCCL parameters
    echo NCCL_DEBUG=INFO >> /etc/nccl.conf && \
    echo NCCL_SOCKET_IFNAME=^docker0 >> /etc/nccl.conf
```

## Collection

 - Name: [51N84D/G3DNet_Singularity](https://github.com/51N84D/G3DNet_Singularity)
 - License: None

