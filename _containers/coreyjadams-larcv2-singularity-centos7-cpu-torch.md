---
id: 5971
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cpu-torch"
commit: "55b4f705ea03e1d2485b7c214d19ce5aea78b379"
version: "bb1ef2f1831fb398632b932bedfa7977"
build_date: "2018-12-15T06:55:31.221Z"
size_mb: 3131
size: 1290100767
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch/2018-12-15-55b4f705-bb1ef2f1/bb1ef2f1831fb398632b932bedfa7977.simg"
url: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch/2018-12-15-55b4f705-bb1ef2f1/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch/2018-12-15-55b4f705-bb1ef2f1/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cpu-torch

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cpu-torch
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos


%help
Centos7 with pytorch
ML/DL packages  : torch sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cpu-torch1.0

#------------
# Global installation
#------------
%environment
    

    source scl_source enable devtoolset-4

%post


    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y centos-release-scl
    yum install -y devtoolset-4
    yum install -y epel-release
    yum install -y wget emacs vim 
    yum install -y PyQt4 PyQt4-devel
    yum install -y emacs vim openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools
    yum install -y hdf5


    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  # for python2.7
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook



    # Using the app area to store software:
    mkdir /app
    cd /app

    scl enable devtoolset-4 bash
    # Install the necessary hash functions:
    git clone https://github.com/sparsehash/sparsehash.git
    cd sparsehash
    ./configure
    make -j install

    cd

    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install future
    pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  # for python2.7
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook

    pip --disable-pip-version-check  install https://download.pytorch.org/whl/cpu/torch-1.0.0-cp27-cp27mu-linux_x86_64.whl


    # This is for tensorboardX
    pip --disable-pip-version-check --no-cache-dir install tensorboardX


    # Install the Submanifold Sparse convolutional extension for CPU:
    cd /app
    git clone https://github.com/facebookresearch/SparseConvNet.git
    cd SparseConvNet
    python setup.py build
    python setup.py install
    cd -
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

