---
id: 9212
name: "DeepLearnPhysics/larcv3-singularity"
branch: "master"
tag: "centos7-cuda-torch-mpich"
commit: "75ee35d5a810e5656e9107771be288ab0b893b01"
version: "ca28df7416b3ba18910a7cbca1c16b64"
build_date: "2019-08-29T19:30:08.175Z"
size_mb: 7482
size: 3842347039
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-torch-mpich/2019-08-29-75ee35d5-ca28df74/ca28df7416b3ba18910a7cbca1c16b64.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-torch-mpich/2019-08-29-75ee35d5-ca28df74/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-torch-mpich/2019-08-29-75ee35d5-ca28df74/Singularity
collection: DeepLearnPhysics/larcv3-singularity
---

# DeepLearnPhysics/larcv3-singularity:centos7-cuda-torch-mpich

```bash
$ singularity pull shub://DeepLearnPhysics/larcv3-singularity:centos7-cuda-torch-mpich
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: DeepLearnPhysics/larcv3-singularity:centos7-cuda-core-mpich

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
Version centos7-cuda-torch-mpich-py36

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
    scl enable rh-python36 bash
    
    # This is a dependency for building horovod from source
    yum install -y eigen3-devel


    # Using the app area to store software:
    mkdir /app
    cd /app

    scl enable devtoolset-4 bash
    # Install the necessary hash functions:
    git clone https://github.com/sparsehash/sparsehash.git
    cd sparsehash
    ./configure
    make -j install
    cd -

    pip3 --no-cache-dir --disable-pip-version-check install torch
    pip3 --no-cache-dir --disable-pip-version-check install torchvision

    # This is for tensorboardX
    pip3 --disable-pip-version-check --no-cache-dir install tensorboardX


    # This is a mild hack, but it allows me to install the cuda-built versions
    # of SparseConvNet and Horovod without having cuda available at build time.

    # I made the container without these, built the wheel files, uploaded to github,
    # and then added the prebuilt binaries to this recipe for installation.

    # Definitely a bootstrap method, and not easily maintained since the build is by hand.

    # Download the prebuilt binary:
    wget https://github.com/DeepLearnPhysics/larcv3-singularity/raw/master/wheels/cuda/pytorch/scn_cuda10-0.2.12182018-cp36-cp36m-linux_x86_64.whl
    pip3 --no-cache-dir --disable-pip-version-check install scn_cuda10-0.2.12182018-cp36-cp36m-linux_x86_64.whl 
    rm scn_cuda10-0.2.12182018-cp36-cp36m-linux_x86_64.whl


    # Install all of the horovod dependencies:
    pip3 --disable-pip-version-check --no-cache-dir install cffi pycparser cloudpickle


    # Download prebuilt libraries for horovod:
    wget https://github.com/DeepLearnPhysics/larcv3-singularity/raw/master/wheels/cuda/pytorch/horovod-0.16.2-cp36-cp36m-linux_x86_64.whl


    pip3 install horovod-0.16.2-cp36-cp36m-linux_x86_64.whl
    rm horovod-0.16.2-cp36-cp36m-linux_x86_64.whl


    # Done!
```

## Collection

 - Name: [DeepLearnPhysics/larcv3-singularity](https://github.com/DeepLearnPhysics/larcv3-singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

