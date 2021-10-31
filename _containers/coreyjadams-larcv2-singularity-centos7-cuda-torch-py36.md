---
id: 6518
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-torch-py36"
commit: "fa0ddaa6e0b94dd9cd5f5749f219a0f5561acf98"
version: "2bbe1f6b84ef5ce471e8abec43439bf0"
build_date: "2019-01-24T23:41:06.118Z"
size_mb: 5820
size: 2963570719
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-py36/2019-01-24-fa0ddaa6-2bbe1f6b/2bbe1f6b84ef5ce471e8abec43439bf0.simg"
url: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-py36/2019-01-24-fa0ddaa6-2bbe1f6b/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-py36/2019-01-24-fa0ddaa6-2bbe1f6b/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-torch-py36

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-torch-py36
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cuda-core-py36

%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : torchnightly sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm 
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-torch-py36

#------------
# Global installation
#------------
%environment

%post
    
    # Using the app area to store software:
    mkdir /app
    cd /app

    scl enable devtoolset-4 bash
    scl enable rh-python36 bash

    # Install the necessary hash functions:
    git clone https://github.com/sparsehash/sparsehash.git
    cd sparsehash
    ./configure
    make -j install

    # This is a mild hack, but it allows me to install the cuda-built versions
    # of SparseConvNet and Horovod without having cuda available at build time.

    # I made the container without these, built the wheel files, uploaded to github,
    # and then added the prebuilt binaries to this recipe for installation.

    # Definitely a bootstrap method, and not easily maintained since the build is by hand.

    # Download the prebuilt binary:
    wget https://github.com/coreyjadams/larcv2-singularity/raw/centos/wheels/cuda/pytorch/sparseconvnet-0.2-cp36-cp36m-linux_x86_64.whl
    pip3 install sparseconvnet-0.2-cp36-cp36m-linux_x86_64.whl 
    rm sparseconvnet-0.2-cp36-cp36m-linux_x86_64.whl



    scl enable rh-python36 bash
    pip3 --no-cache-dir --disable-pip-version-check install torch
    pip3 --no-cache-dir --disable-pip-version-check install torchvision

    # This is for tensorboardX
    pip3 --disable-pip-version-check --no-cache-dir install tensorboardX
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

