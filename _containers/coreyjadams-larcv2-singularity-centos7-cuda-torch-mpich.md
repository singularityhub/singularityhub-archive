---
id: 6457
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-torch-mpich"
commit: "2770ca0cbd7ba270e39a54a378ea6a06e433b8db"
version: "0c491163b8e2cdeff6a2936327b6b1db"
build_date: "2020-03-03T18:04:42.735Z"
size_mb: 6198
size: 3314708511
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-mpich/2020-03-03-2770ca0c-0c491163/0c491163b8e2cdeff6a2936327b6b1db.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-mpich/2020-03-03-2770ca0c-0c491163/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-mpich/2020-03-03-2770ca0c-0c491163/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-torch-mpich

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-torch-mpich
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cuda-core-mpich


%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : tensorflow keras sc-learn nccl
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python ROOT
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py horovod
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client mpich

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-torch-mpich

#------------
# Global installation
#------------
%environment
 

    # for MPICH:
    export PATH=/usr/local/mpich/install/bin/:${PATH}
    export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:${LD_LIBRARY_PATH}

    # This line is necessary to run on Cooley:
    export NCCL_P2P_DISABLE=1

%post

    scl enable devtoolset-4 bash
    
    # This is a dependency for building horovod from source
    yum install -y eigen3-devel


    # Using the app area to store software:
    mkdir /app
    cd /app

    # Install the necessary hash functions:
    git clone https://github.com/sparsehash/sparsehash.git
    cd sparsehash
    ./configure
    make -j install


    pip --no-cache-dir --disable-pip-verspion-check install torch
    pip --no-cache-dir --disable-pip-version-check install torchvision

    # This is for tensorboardX
    pip --disable-pip-version-check --no-cache-dir install tensorboardX


    # This is a mild hack, but it allows me to install the cuda-built versions
    # of SparseConvNet and Horovod without having cuda available at build time.

    # I made the container without these, built the wheel files, uploaded to github,
    # and then added the prebuilt binaries to this recipe for installation.

    # Definitely a bootstrap method, and not easily maintained since the build is by hand.

    # Download the prebuilt binary:
    wget https://github.com/coreyjadams/larcv2-singularity/raw/centos/wheels/cuda/pytorch/sparseconvnet-0.2-cp27-cp27mu-linux_x86_64.whl
    pip install sparseconvnet-0.2-cp27-cp27mu-linux_x86_64.whl
    rm sparseconvnet-0.2-cp27-cp27mu-linux_x86_64.whl



    # Download prebuilt libraries for horovod:
    wget https://github.com/coreyjadams/larcv2-singularity/raw/centos/wheels/cuda/pytorch/cffi-1.11.5-cp27-cp27mu-manylinux1_x86_64.whl
    wget https://github.com/coreyjadams/larcv2-singularity/raw/centos/wheels/cuda/pytorch/pycparser-2.19-py2.py3-none-any.whl
    wget https://github.com/coreyjadams/larcv2-singularity/raw/centos/wheels/cuda/pytorch/horovod-0.15.2-cp27-cp27mu-linux_x86_64.whl

    pip install cffi-1.11.5-cp27-cp27mu-manylinux1_x86_64.whl
    rm cffi-1.11.5-cp27-cp27mu-manylinux1_x86_64.whl

    pip install pycparser-2.19-py2.py3-none-any.whl
    rm pycparser-2.19-py2.py3-none-any.whl

    pip install horovod-0.15.2-cp27-cp27mu-linux_x86_64.whl
    rm horovod-0.15.2-cp27-cp27mu-linux_x86_64.whl


    # Done!
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

