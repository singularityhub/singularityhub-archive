---
id: 6555
name: "DeepLearnPhysics/larcv2-singularity"
branch: "master"
tag: "ub16.04-pytorchdev10152018-root6.14.04"
commit: "be669c05e76561b11127f7a5bb690329353b8bab"
version: "fabe1d529e68d9d0c7ec493cd3c55984"
build_date: "2019-01-24T17:50:02.592Z"
size_mb: 5838
size: 2795696159
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-pytorchdev10152018-root6.14.04/2019-01-24-be669c05-fabe1d52/fabe1d529e68d9d0c7ec493cd3c55984.simg"
url: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-pytorchdev10152018-root6.14.04/2019-01-24-be669c05-fabe1d52/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-pytorchdev10152018-root6.14.04/2019-01-24-be669c05-fabe1d52/Singularity
collection: DeepLearnPhysics/larcv2-singularity
---

# DeepLearnPhysics/larcv2-singularity:ub16.04-pytorchdev10152018-root6.14.04

```bash
$ singularity pull shub://DeepLearnPhysics/larcv2-singularity:ub16.04-pytorchdev10152018-root6.14.04
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: deeplearnphysics/ml-larcv2:pytorch-dev10152018-scn

%help
Ubuntu16.04 with cuda9.0 cudnn7
ML/DL packages  : pytorch (1.0.0=dev10152018) sc-learn
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
Version ub16.04-pytorchdev10152018-root6.14.04

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

