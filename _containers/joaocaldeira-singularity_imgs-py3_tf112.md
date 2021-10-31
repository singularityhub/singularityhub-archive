---
id: 9879
name: "joaocaldeira/singularity_imgs"
branch: "master"
tag: "py3_tf112"
commit: "e896f5a0ea25e27b56820cea602896190420b42a"
version: "9342e07443ad4f4483f06ca6918dfbf1"
build_date: "2019-06-18T22:10:58.374Z"
size_mb: 4423
size: 2372816927
sif: "https://datasets.datalad.org/shub/joaocaldeira/singularity_imgs/py3_tf112/2019-06-18-e896f5a0-9342e074/9342e07443ad4f4483f06ca6918dfbf1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/joaocaldeira/singularity_imgs/py3_tf112/2019-06-18-e896f5a0-9342e074/
recipe: https://datasets.datalad.org/shub/joaocaldeira/singularity_imgs/py3_tf112/2019-06-18-e896f5a0-9342e074/Singularity
collection: joaocaldeira/singularity_imgs
---

# joaocaldeira/singularity_imgs:py3_tf112

```bash
$ singularity pull shub://joaocaldeira/singularity_imgs:py3_tf112
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
Maintainer caldeira
Version ubuntu16.04-py3-tf112-gpu

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
    python3 -m pip install tensorflow-gpu==1.12.0
    python3 -m pip install h5py
```

## Collection

 - Name: [joaocaldeira/singularity_imgs](https://github.com/joaocaldeira/singularity_imgs)
 - License: None

