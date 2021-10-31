---
id: 6456
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-torch"
commit: "55e681b6a1d4c1ecf64329cd384604b450bcd858"
version: "c0f0e8a163fe0cb0ab43f499145d7606"
build_date: "2019-01-24T23:41:06.105Z"
size_mb: 5324
size: 2799763487
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch/2019-01-24-55e681b6-c0f0e8a1/c0f0e8a163fe0cb0ab43f499145d7606.simg"
url: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch/2019-01-24-55e681b6-c0f0e8a1/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch/2019-01-24-55e681b6-c0f0e8a1/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-torch

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-torch
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cuda-core

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
Version centos7-cuda-torch

#------------
# Global installation
#------------
%environment

%post
    
    # Using the app area to store software:
    mkdir /app
    cd /app

    scl enable devtoolset-4 bash

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

    pip --no-cache-dir --disable-pip-version-check install torch
    pip --no-cache-dir --disable-pip-version-check install torchvision

    # This is for tensorboardX
    pip --disable-pip-version-check --no-cache-dir install tensorboardX

    # Download the prebuilt binary:
    wget https://github.com/coreyjadams/larcv2-singularity/raw/centos/wheels/cuda/pytorch/sparseconvnet-0.2-cp27-cp27mu-linux_x86_64.whl
    pip install sparseconvnet-0.2-cp27-cp27mu-linux_x86_64.whl
    rm sparseconvnet-0.2-cp27-cp27mu-linux_x86_64.whl
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

