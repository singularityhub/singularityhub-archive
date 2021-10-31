---
id: 9255
name: "gnperdue/singularity_imgs"
branch: "master"
tag: "py3_tf2gnt"
commit: "7af2da88c575ea35408c3bb04b585c7b3937e583"
version: "3058b97fa940a932db3a66c24bf0e4dd"
build_date: "2019-05-23T15:31:33.040Z"
size_mb: 4240
size: 1945292831
sif: "https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_tf2gnt/2019-05-23-7af2da88-3058b97f/3058b97fa940a932db3a66c24bf0e4dd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gnperdue/singularity_imgs/py3_tf2gnt/2019-05-23-7af2da88-3058b97f/
recipe: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_tf2gnt/2019-05-23-7af2da88-3058b97f/Singularity
collection: gnperdue/singularity_imgs
---

# gnperdue/singularity_imgs:py3_tf2gnt

```bash
$ singularity pull shub://gnperdue/singularity_imgs:py3_tf2gnt
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-devel-ubuntu16.04

%help
To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

Container based on recipe by drinkingkazu

%labels
Maintainer gnperdue
Version ubuntu16.04-py3-tf2-alpha-gpu

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
    python3 -m pip install --no-cache-dir --upgrade tf-nightly-gpu-2.0-preview tf-agents-nightly tfp-nightly tensorflow-datasets
    python3 -m pip install --no-cache-dir matplotlib seaborn scikit-image
    python3 -m pip install --no-cache-dir 'gym[atari,box2d,classic_control]'
```

## Collection

 - Name: [gnperdue/singularity_imgs](https://github.com/gnperdue/singularity_imgs)
 - License: None

