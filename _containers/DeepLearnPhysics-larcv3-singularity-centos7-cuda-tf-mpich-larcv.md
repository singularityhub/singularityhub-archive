---
id: 10037
name: "DeepLearnPhysics/larcv3-singularity"
branch: "master"
tag: "centos7-cuda-tf-mpich-larcv"
commit: "440d078e1c843dfdf9aad32a4d4fa97f7a057054"
version: "894bc1330b231e28405f0db605fc2d67"
build_date: "2020-05-07T01:17:54.050Z"
size_mb: 7409
size: 3585843231
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-tf-mpich-larcv/2020-05-07-440d078e-894bc133/894bc1330b231e28405f0db605fc2d67.simg"
url: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-tf-mpich-larcv/2020-05-07-440d078e-894bc133/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-tf-mpich-larcv/2020-05-07-440d078e-894bc133/Singularity
collection: DeepLearnPhysics/larcv3-singularity
---

# DeepLearnPhysics/larcv3-singularity:centos7-cuda-tf-mpich-larcv

```bash
$ singularity pull shub://DeepLearnPhysics/larcv3-singularity:centos7-cuda-tf-mpich-larcv
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: DeepLearnPhysics/larcv3-singularity:centos7-cuda-tf-mpich

%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : torchnightly sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm 
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client swig larrcv

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-tf-mpich-larcv

#------------
# Global installation
#------------
%environment

%post
    
    # Using the app area to store software:
    mkdir /app
    cd /app

    scl enable devtoolset-4 bash
    scl enable rh-python36 bash

    pip3 install ninja

    #Install the latest larcv3:
    git clone https://github.com/DeepLearnPhysics/larcv3.git
    cd larcv3/
    python setup.py install --cmake-executable cmake3
    cd -
```

## Collection

 - Name: [DeepLearnPhysics/larcv3-singularity](https://github.com/DeepLearnPhysics/larcv3-singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

