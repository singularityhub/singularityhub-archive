---
id: 4185
name: "gnperdue/singularity_imgs"
branch: "master"
tag: "py3_tf110"
commit: "d0e409e200e301bf5846af10be963a65a1056961"
version: "5e6c8f5d9e714d785c16e06d6c30c585"
build_date: "2019-08-22T19:46:46.312Z"
size_mb: 4134
size: 2188075039
sif: "https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_tf110/2019-08-22-d0e409e2-5e6c8f5d/5e6c8f5d9e714d785c16e06d6c30c585.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gnperdue/singularity_imgs/py3_tf110/2019-08-22-d0e409e2-5e6c8f5d/
recipe: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_tf110/2019-08-22-d0e409e2-5e6c8f5d/Singularity
collection: gnperdue/singularity_imgs
---

# gnperdue/singularity_imgs:py3_tf110

```bash
$ singularity pull shub://gnperdue/singularity_imgs:py3_tf110
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%help
To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

Container based on recipe by drinkingkazu

%labels
Maintainer gnperdue
Version ubuntu16.04-py3-tf110-gpu

#------------
# Global installation
#------------
%environment
    export XDG_RUNTIME_DIR=/tmp/$USER
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs:${LD_LIBRARY_PATH}
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

%post
    # add wilson cluster mount points
    mkdir /scratch /data /lfstev

    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip

    # pip
    python3 -m pip install --upgrade setuptools pip
    python3 -m pip install tensorflow-gpu==1.10.0
    python3 -m pip install h5py
```

## Collection

 - Name: [gnperdue/singularity_imgs](https://github.com/gnperdue/singularity_imgs)
 - License: None

