---
id: 4240
name: "DeepLearnPhysics/playground-singularity"
branch: "master"
tag: "ub16.04-step3"
commit: "f10ff40cd0c7d1efe9d18742a999dbbcc4342c55"
version: "11264e22fcbd638ba08c1915f08605cd"
build_date: "2018-09-02T17:27:42.361Z"
size_mb: 5865
size: 2737967135
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step3/2018-09-02-f10ff40c-11264e22/11264e22fcbd638ba08c1915f08605cd.simg"
url: https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step3/2018-09-02-f10ff40c-11264e22/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step3/2018-09-02-f10ff40c-11264e22/Singularity
collection: DeepLearnPhysics/playground-singularity
---

# DeepLearnPhysics/playground-singularity:ub16.04-step3

```bash
$ singularity pull shub://DeepLearnPhysics/playground-singularity:ub16.04-step3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%help
Ubuntu16.04
DL/ML packages  : sc-learn keras tf-1.7 torch-0.4
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ub16.04-step3

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER

%post
    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev git wget emacs vim openssh-client
    apt-get -y install python-dev python-tk python-pip python-qt4 python-setuptools
    apt-get -y install python3-setuptools
    apt-get -y install libhdf5-dev

    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install matplotlib pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook

    # tensorflow
    pip --no-cache-dir --disable-pip-version-check install --upgrade tensorflow-gpu==1.7.1
    pip --no-cache-dir --disable-pip-version-check install tensorboard

    # keras
    pip --no-cache-dir --disable-pip-version-check install keras

    # torch
    pip --no-cache-dir --disable-pip-version-check install torch==0.4.1
    pip --no-cache-dir --disable-pip-version-check install torchvision==0.2.1
```

## Collection

 - Name: [DeepLearnPhysics/playground-singularity](https://github.com/DeepLearnPhysics/playground-singularity)
 - License: None

