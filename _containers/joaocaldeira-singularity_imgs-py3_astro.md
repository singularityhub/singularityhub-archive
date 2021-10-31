---
id: 9086
name: "joaocaldeira/singularity_imgs"
branch: "master"
tag: "py3_astro"
commit: "2e311edab8168365a4288e0a394a21fc550c5d08"
version: "caeccb4b06f15b6e4535faa07831dad8"
build_date: "2019-09-05T18:09:25.468Z"
size_mb: 3129
size: 1791741983
sif: "https://datasets.datalad.org/shub/joaocaldeira/singularity_imgs/py3_astro/2019-09-05-2e311eda-caeccb4b/caeccb4b06f15b6e4535faa07831dad8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/joaocaldeira/singularity_imgs/py3_astro/2019-09-05-2e311eda-caeccb4b/
recipe: https://datasets.datalad.org/shub/joaocaldeira/singularity_imgs/py3_astro/2019-09-05-2e311eda-caeccb4b/Singularity
collection: joaocaldeira/singularity_imgs
---

# joaocaldeira/singularity_imgs:py3_astro

```bash
$ singularity pull shub://joaocaldeira/singularity_imgs:py3_astro
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
Version ubuntu16.04-py3-astropy

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
    python3 -m pip install h5py astropy numpy
```

## Collection

 - Name: [joaocaldeira/singularity_imgs](https://github.com/joaocaldeira/singularity_imgs)
 - License: None

