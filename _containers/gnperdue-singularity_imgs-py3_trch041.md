---
id: 4675
name: "gnperdue/singularity_imgs"
branch: "master"
tag: "py3_trch041"
commit: "1da39fd694ece6fd2483f200193e2100ae1f1fef"
version: "81395287f88b77bce9bf2890abca4dc2"
build_date: "2018-11-24T04:49:41.195Z"
size_mb: 4848
size: 2916507679
sif: "https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_trch041/2018-11-24-1da39fd6-81395287/81395287f88b77bce9bf2890abca4dc2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gnperdue/singularity_imgs/py3_trch041/2018-11-24-1da39fd6-81395287/
recipe: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_trch041/2018-11-24-1da39fd6-81395287/Singularity
collection: gnperdue/singularity_imgs
---

# gnperdue/singularity_imgs:py3_trch041

```bash
$ singularity pull shub://gnperdue/singularity_imgs:py3_trch041
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
Version ubuntu16.04-py3-trch041

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
    python3 -m pip install torch torchvision
    python3 -m pip install h5py matplotlib pandas scikit-image scikit-learn Pillow tqdm
```

## Collection

 - Name: [gnperdue/singularity_imgs](https://github.com/gnperdue/singularity_imgs)
 - License: None

