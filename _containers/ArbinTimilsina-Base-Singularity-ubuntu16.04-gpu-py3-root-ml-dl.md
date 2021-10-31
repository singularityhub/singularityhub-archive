---
id: 3790
name: "ArbinTimilsina/Base-Singularity"
branch: "master"
tag: "ubuntu16.04-gpu-py3-root-ml-dl"
commit: "6e35a0a02aac56f4e21e0a052aff934609b77d58"
version: "ae4e9b286ee49b578286d60cbe3029ff"
build_date: "2018-07-31T15:32:55.938Z"
size_mb: 4173
size: 1827639327
sif: "https://datasets.datalad.org/shub/ArbinTimilsina/Base-Singularity/ubuntu16.04-gpu-py3-root-ml-dl/2018-07-31-6e35a0a0-ae4e9b28/ae4e9b286ee49b578286d60cbe3029ff.simg"
url: https://datasets.datalad.org/shub/ArbinTimilsina/Base-Singularity/ubuntu16.04-gpu-py3-root-ml-dl/2018-07-31-6e35a0a0-ae4e9b28/
recipe: https://datasets.datalad.org/shub/ArbinTimilsina/Base-Singularity/ubuntu16.04-gpu-py3-root-ml-dl/2018-07-31-6e35a0a0-ae4e9b28/Singularity
collection: ArbinTimilsina/Base-Singularity
---

# ArbinTimilsina/Base-Singularity:ubuntu16.04-gpu-py3-root-ml-dl

```bash
$ singularity pull shub://ArbinTimilsina/Base-Singularity:ubuntu16.04-gpu-py3-root-ml-dl
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.9.0-devel-gpu-py3

%labels
Maintainer Arbin Timilsina
Version Ubuntu16.04-ROOT6.14.02-GPU-Py3

%help
A portable Ubuntu 16.04 environment with pre-built ML/DLframeworks including scikit-learn and keras.
Also includes ROOTv6.14.02 and the following:
Development kit : dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip
Utility kit     : git wget emacs vim
Basic python    : wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm jupyter
ML packages     : numpy matplotlib pandas scikit-image scikit-learn Pillow opencv-python
DL packages     : tensorflow keras

To start the container simply do
singularity exec THIS_CONTAINER.simg bash

To use GPUs, do
singularity exec --nv THIS_CONTAINER.simg bash

%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER

    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
			    
%post
    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip git wget emacs vim

# ROOT
    wget https://root.cern.ch/download/root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    tar -xzf root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    rm root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    mv root /usr/local/root
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

# pip basics- pip3 breaks the build- https://github.com/pypa/pip/issues/5599 so using python -m pip instead
    python -m pip --no-cache-dir install --upgrade pip
    python -m pip --no-cache-dir install --upgrade setuptools
    python -m pip --no-cache-dir install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm
    python -m pip --no-cache-dir install matplotlib pandas scikit-image scikit-learn Pillow opencv-python
    python -m pip --no-cache-dir install jupyter notebook

# keras
    python -m pip --no-cache-dir install keras
```

## Collection

 - Name: [ArbinTimilsina/Base-Singularity](https://github.com/ArbinTimilsina/Base-Singularity)
 - License: None

