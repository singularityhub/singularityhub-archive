---
id: 4239
name: "DeepLearnPhysics/playground-singularity"
branch: "master"
tag: "ub16.04-step2"
commit: "3eb3b6a03cb5587bfd22619ef68027587ac32d64"
version: "e1eb6b2f4ed6934e58f2dc5aff5da389"
build_date: "2018-08-28T20:48:17.142Z"
size_mb: 1706
size: 604454943
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step2/2018-08-28-3eb3b6a0-e1eb6b2f/e1eb6b2f4ed6934e58f2dc5aff5da389.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/playground-singularity/ub16.04-step2/2018-08-28-3eb3b6a0-e1eb6b2f/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/playground-singularity/ub16.04-step2/2018-08-28-3eb3b6a0-e1eb6b2f/Singularity
collection: DeepLearnPhysics/playground-singularity
---

# DeepLearnPhysics/playground-singularity:ub16.04-step2

```bash
$ singularity pull shub://DeepLearnPhysics/playground-singularity:ub16.04-step2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Ubuntu16.04
DL/ML packages  : sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ub16.04-step2

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
```

## Collection

 - Name: [DeepLearnPhysics/playground-singularity](https://github.com/DeepLearnPhysics/playground-singularity)
 - License: None

