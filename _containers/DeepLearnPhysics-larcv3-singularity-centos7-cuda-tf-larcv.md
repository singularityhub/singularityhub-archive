---
id: 10036
name: "DeepLearnPhysics/larcv3-singularity"
branch: "master"
tag: "centos7-cuda-tf-larcv"
commit: "8c86bd90e0225b2db3d9e92246ab612e9dcd1433"
version: "1934a05e8313713cbc4cf514e1cd5865"
build_date: "2020-05-08T10:08:57.381Z"
size_mb: 6269
size: 2900660255
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-tf-larcv/2020-05-08-8c86bd90-1934a05e/1934a05e8313713cbc4cf514e1cd5865.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-tf-larcv/2020-05-08-8c86bd90-1934a05e/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv3-singularity/centos7-cuda-tf-larcv/2020-05-08-8c86bd90-1934a05e/Singularity
collection: DeepLearnPhysics/larcv3-singularity
---

# DeepLearnPhysics/larcv3-singularity:centos7-cuda-tf-larcv

```bash
$ singularity pull shub://DeepLearnPhysics/larcv3-singularity:centos7-cuda-tf-larcv
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: DeepLearnPhysics/larcv3-singularity:centos7-cuda-tf

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
Version centos7-cuda-tf-larcv

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

