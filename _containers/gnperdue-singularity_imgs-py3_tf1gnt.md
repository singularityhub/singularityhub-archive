---
id: 9256
name: "gnperdue/singularity_imgs"
branch: "master"
tag: "py3_tf1gnt"
commit: "a589ee0649656b1bcc07ddeeea071828fc8f0a0d"
version: "b0bc712897d318d923390c6fb1452c39"
build_date: "2019-08-21T19:05:21.176Z"
size_mb: 4353
size: 1975730207
sif: "https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_tf1gnt/2019-08-21-a589ee06-b0bc7128/b0bc712897d318d923390c6fb1452c39.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gnperdue/singularity_imgs/py3_tf1gnt/2019-08-21-a589ee06-b0bc7128/
recipe: https://datasets.datalad.org/shub/gnperdue/singularity_imgs/py3_tf1gnt/2019-08-21-a589ee06-b0bc7128/Singularity
collection: gnperdue/singularity_imgs
---

# gnperdue/singularity_imgs:py3_tf1gnt

```bash
$ singularity pull shub://gnperdue/singularity_imgs:py3_tf1gnt
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
Version ubuntu16.04-py3-tf-alpha-gpu

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
    python3 -m pip install --no-cache-dir --upgrade tf-nightly-gpu tf-agents-nightly tfp-nightly tensorflow-datasets
    python3 -m pip install --no-cache-dir matplotlib seaborn scikit-image
    python3 -m pip install --no-cache-dir 'gym[atari,box2d,classic_control]'
    python3 -m pip install https://github.com/gnperdue/gym-oscillator/zipball/master
```

## Collection

 - Name: [gnperdue/singularity_imgs](https://github.com/gnperdue/singularity_imgs)
 - License: None

