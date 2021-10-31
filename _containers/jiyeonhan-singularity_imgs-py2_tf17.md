---
id: 6373
name: "jiyeonhan/singularity_imgs"
branch: "master"
tag: "py2_tf17"
commit: "0f1b687b2f6143e376f2d71e5a6bbf771b728a7a"
version: "3427255aadf8f3b0bee64362bfb10856"
build_date: "2019-01-21T15:26:42.082Z"
size_mb: 3348
size: 1479684127
sif: "https://datasets.datalad.org/shub/jiyeonhan/singularity_imgs/py2_tf17/2019-01-21-0f1b687b-3427255a/3427255aadf8f3b0bee64362bfb10856.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jiyeonhan/singularity_imgs/py2_tf17/2019-01-21-0f1b687b-3427255a/
recipe: https://datasets.datalad.org/shub/jiyeonhan/singularity_imgs/py2_tf17/2019-01-21-0f1b687b-3427255a/Singularity
collection: jiyeonhan/singularity_imgs
---

# jiyeonhan/singularity_imgs:py2_tf17

```bash
$ singularity pull shub://jiyeonhan/singularity_imgs:py2_tf17
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
Maintainer jiyeonhan
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

 - Name: [jiyeonhan/singularity_imgs](https://github.com/jiyeonhan/singularity_imgs)
 - License: None

