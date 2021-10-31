---
id: 2752
name: "gnperdue/singularity_imgs"
branch: "master"
tag: "py2_tf17"
commit: "72181704d5ede18a6d772b2b444198e7e9d7b125"
version: "88b5a3be153a7824c204419fb7e88b6e"
build_date: "2018-08-24T15:31:57.458Z"
size_mb: 3387
size: 1491304479
sif: "https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py2_tf17/2018-08-24-72181704-88b5a3be/88b5a3be153a7824c204419fb7e88b6e.simg"
url: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py2_tf17/2018-08-24-72181704-88b5a3be/
recipe: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py2_tf17/2018-08-24-72181704-88b5a3be/Singularity
collection: gnperdue/singularity_imgs
---

# gnperdue/singularity_imgs:py2_tf17

```bash
$ singularity pull shub://gnperdue/singularity_imgs:py2_tf17
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.7.0-devel-gpu

%help
Ubuntu16.04 with cuda9 cudnn7
ML/DL packages  : tensorflow sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib 
Basic python    : yaml six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

Container based on recipe by drinkingkazu

%labels
Maintainer gnperdue
Version ubuntu16.04-py2-tf17-gpu

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs:${LD_LIBRARY_PATH}
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

%post

    mkdir /scratch /data

    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python-dev python-tk python-pip

    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install --upgrade 'pip<=9.0.3'
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm
    pip --no-cache-dir --disable-pip-version-check install matplotlib pandas scikit-image scikit-learn Pillow
```

## Collection

 - Name: [gnperdue/singularity_imgs](https://github.com/gnperdue/singularity_imgs)
 - License: None

