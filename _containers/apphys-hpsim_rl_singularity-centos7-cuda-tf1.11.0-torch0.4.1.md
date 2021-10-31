---
id: 5615
name: "apphys/hpsim_rl_singularity"
branch: "master"
tag: "centos7-cuda-tf1.11.0-torch0.4.1"
commit: "c66fc008e068c5caeb53099c5878879eb042372f"
version: "ffebff4451526e218eb0bea64c0fc6d0"
build_date: "2018-11-16T01:38:15.819Z"
size_mb: 5650
size: 2564530207
sif: "https://datasets.datalad.org/shub/apphys/hpsim_rl_singularity/centos7-cuda-tf1.11.0-torch0.4.1/2018-11-16-c66fc008-ffebff44/ffebff4451526e218eb0bea64c0fc6d0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/apphys/hpsim_rl_singularity/centos7-cuda-tf1.11.0-torch0.4.1/2018-11-16-c66fc008-ffebff44/
recipe: https://datasets.datalad.org/shub/apphys/hpsim_rl_singularity/centos7-cuda-tf1.11.0-torch0.4.1/2018-11-16-c66fc008-ffebff44/Singularity
collection: apphys/hpsim_rl_singularity
---

# apphys/hpsim_rl_singularity:centos7-cuda-tf1.11.0-torch0.4.1

```bash
$ singularity pull shub://apphys/hpsim_rl_singularity:centos7-cuda-tf1.11.0-torch0.4.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : tensorflow keras sc-learn
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
Version centos7-tf1.11.0-torch0.4.1

#------------
# Global installation
#------------
%environment
    
    # for system
    export CUDA_DEVICE_ORDER=PCI_BUS_ID


%post
    
    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y epel-release
    yum install -y wget emacs vim 
    yum install -y PyQt4 PyQt4-devel
    yum install -y emacs vim openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools
    yum install -y hdf5


    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  # for python2.7
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook

    # tensorflow
    pip --no-cache-dir --disable-pip-version-check install --upgrade tensorflow-gpu==1.11.0
    pip --no-cache-dir --disable-pip-version-check install tensorboard

    # keras
    pip --no-cache-dir --disable-pip-version-check install keras

    # torch
    pip --no-cache-dir --disable-pip-version-check install torch==0.4.1
    pip --no-cache-dir --disable-pip-version-check install torchvision==0.2.1
```

## Collection

 - Name: [apphys/hpsim_rl_singularity](https://github.com/apphys/hpsim_rl_singularity)
 - License: None

