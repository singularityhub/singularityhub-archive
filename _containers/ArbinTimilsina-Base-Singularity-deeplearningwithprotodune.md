---
id: 6525
name: "ArbinTimilsina/Base-Singularity"
branch: "master"
tag: "deeplearningwithprotodune"
commit: "3fe23aee8ddf60ad3d1da1c8ab0f6bb68de84ed7"
version: "e249a557d77029851752216cc2456f89"
build_date: "2019-01-24T13:54:59.083Z"
size_mb: 3857
size: 1707327519
sif: "https://datasets.datalad.org/shub/ArbinTimilsina/Base-Singularity/deeplearningwithprotodune/2019-01-24-3fe23aee-e249a557/e249a557d77029851752216cc2456f89.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ArbinTimilsina/Base-Singularity/deeplearningwithprotodune/2019-01-24-3fe23aee-e249a557/
recipe: https://datasets.datalad.org/shub/ArbinTimilsina/Base-Singularity/deeplearningwithprotodune/2019-01-24-3fe23aee-e249a557/Singularity
collection: ArbinTimilsina/Base-Singularity
---

# ArbinTimilsina/Base-Singularity:deeplearningwithprotodune

```bash
$ singularity pull shub://ArbinTimilsina/Base-Singularity:deeplearningwithprotodune
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.9.0-devel-gpu-py3

%labels
Maintainer Arbin Timilsina
Version DeepLearningWithProtoDUNE

%help
A portable Ubuntu 16.04 environment with pre-built ML/DLframeworks including scikit-learn and keras.
Also includes the following:
Development kit : dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip
Utility kit     : git wget emacs vim
Basic python    : wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm jupyter pydot graphviz
ML packages     : numpy matplotlib pandas scikit-image scikit-learn Pillow opencv-python
DL packages     : tensorflow keras

To start the container simply do
singularity exec THIS_CONTAINER.simg bash

To use GPUs, do
singularity exec --nv THIS_CONTAINER.simg bash

%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
			    
%post
    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip git wget emacs vim
    apt-get -y install graphviz

# pip basics- pip3 breaks the build- https://github.com/pypa/pip/issues/5599 so using python -m pip instead
    python -m pip --no-cache-dir install --upgrade pip
    python -m pip --no-cache-dir install --upgrade setuptools
    python -m pip --no-cache-dir install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm
    python -m pip --no-cache-dir install matplotlib pandas scikit-image scikit-learn Pillow opencv-python
    python -m pip --no-cache-dir install jupyter notebook
    python -m pip --no-cache-dir install pydot
    
# keras
    python -m pip --no-cache-dir install keras
```

## Collection

 - Name: [ArbinTimilsina/Base-Singularity](https://github.com/ArbinTimilsina/Base-Singularity)
 - License: None

