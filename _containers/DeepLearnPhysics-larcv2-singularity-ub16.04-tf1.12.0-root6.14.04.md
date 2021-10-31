---
id: 6560
name: "DeepLearnPhysics/larcv2-singularity"
branch: "master"
tag: "ub16.04-tf1.12.0-root6.14.04"
commit: "be669c05e76561b11127f7a5bb690329353b8bab"
version: "7bbac90a1a7de9fd0875e7ad160ec9d8"
build_date: "2019-01-24T17:50:02.579Z"
size_mb: 5750
size: 2498928671
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-tf1.12.0-root6.14.04/2019-01-24-be669c05-7bbac90a/7bbac90a1a7de9fd0875e7ad160ec9d8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-tf1.12.0-root6.14.04/2019-01-24-be669c05-7bbac90a/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-tf1.12.0-root6.14.04/2019-01-24-be669c05-7bbac90a/Singularity
collection: DeepLearnPhysics/larcv2-singularity
---

# DeepLearnPhysics/larcv2-singularity:ub16.04-tf1.12.0-root6.14.04

```bash
$ singularity pull shub://DeepLearnPhysics/larcv2-singularity:ub16.04-tf1.12.0-root6.14.04
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: deeplearnphysics/ml-larcv2:tf-1.12.0

%help
Ubuntu16.04 with cuda9.0 cudnn7
ML/DL packages  : tensorflow (1.12.0) keras sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python root root_numpy
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ub16.04-tf1.12.0-root6.14.04

#------------
# Global installation
#------------
%environment
    export XDG_RUNTIME_DIR=/tmp/$USER
    export CUDA_DEVICE_ORDER=PCI_BUS_ID
```

## Collection

 - Name: [DeepLearnPhysics/larcv2-singularity](https://github.com/DeepLearnPhysics/larcv2-singularity)
 - License: None

