---
id: 6444
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-core"
commit: "fa0ddaa6e0b94dd9cd5f5749f219a0f5561acf98"
version: "c2f9b6b9596db19cd302d1c5ea89e546"
build_date: "2019-01-24T23:41:06.112Z"
size_mb: 4111
size: 2184720415
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core/2019-01-24-fa0ddaa6-c2f9b6b9/c2f9b6b9596db19cd302d1c5ea89e546.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/coreyjadams/larcv2-singularity/centos7-cuda-core/2019-01-24-fa0ddaa6-c2f9b6b9/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core/2019-01-24-fa0ddaa6-c2f9b6b9/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-core

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-core
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%help
Centos7 with cuda9.0 cudnn7, and basic development tools
ML/DL packages  : sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm 
Development kit : g++/gcc cython nvcc python3-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-core

#------------
# Global installation
#------------
%environment
    
    # for system
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

    # Add cupti to the path for profiling:
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64

    source scl_source enable devtoolset-4


%post
    
    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    # Install gcc, etc:
    yum install -y centos-release-scl
    yum install -y epel-release
    yum install -y devtoolset-4
    yum install -y python-devel python-pip  python-setuptools



    # Common development tools:
    yum install -y wget emacs vim cmake3
    yum install -y emacs vim openssh-clients zip 
    yum install -y hdf5

    # pip basics

    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install future
    pip --no-cache-dir --disable-pip-version-check install numpy h5py 
    # pip --no-cache-dir --disable-pip-version-check install wheel zmq six pygments pyyaml cython gputil psutil humanize tqdm scipy seaborn tables
    # pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    # pip --no-cache-dir --disable-pip-version-check install jupyter notebook
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

