---
id: 4095
name: "gnperdue/singularity_imgs"
branch: "master"
tag: "py2_tf110"
commit: "3a51c432890daf541bd29c8d7bff0e061d9a8c62"
version: "839adcbfa3d2a6ab20b217f5c04e82cd"
build_date: "2019-08-22T19:47:05.801Z"
size_mb: 4119
size: 2175664159
sif: "https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py2_tf110/2019-08-22-3a51c432-839adcbf/839adcbfa3d2a6ab20b217f5c04e82cd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gnperdue/singularity_imgs/py2_tf110/2019-08-22-3a51c432-839adcbf/
recipe: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py2_tf110/2019-08-22-3a51c432-839adcbf/Singularity
collection: gnperdue/singularity_imgs
---

# gnperdue/singularity_imgs:py2_tf110

```bash
$ singularity pull shub://gnperdue/singularity_imgs:py2_tf110
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
Version ubuntu16.04-py2-tf110-gpu

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
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python-dev python-tk python-pip

    # pip
    python -m pip install --upgrade setuptools pip
    python -m pip install tensorflow-gpu==1.10.0
    python -m pip install h5py
```

## Collection

 - Name: [gnperdue/singularity_imgs](https://github.com/gnperdue/singularity_imgs)
 - License: None

