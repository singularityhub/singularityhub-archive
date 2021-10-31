---
id: 6570
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-torch-mpich-root"
commit: "2770ca0cbd7ba270e39a54a378ea6a06e433b8db"
version: "72409a037ab71e09c59fd631c271bf97"
build_date: "2019-01-24T23:41:06.079Z"
size_mb: 6842
size: 3519803423
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-mpich-root/2019-01-24-2770ca0c-72409a03/72409a037ab71e09c59fd631c271bf97.simg"
url: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-mpich-root/2019-01-24-2770ca0c-72409a03/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-torch-mpich-root/2019-01-24-2770ca0c-72409a03/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-torch-mpich-root

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-torch-mpich-root
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cuda-torch-mpich


%help
Centos7 with cuda9.0 cudnn7, larcv
ML/DL packages  : torch keras sc-learn nccl
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python ROOT larcv
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py horovod
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client mpich

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-torch-mpich-py36

#------------
# Global installation
#------------
%environment
 
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    export LD_LIBRARY_PATH=/usr/local/root/lib/:${LD_LIBRARY_PATH}

    source /app/larcv2/configure.sh -q

%post

    # For root, need to build from source unfortunately to get pyroot for python3.6
    scl enable devtoolset-4 bash

    # ROOT
    wget https://root.cern.ch/download/root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    tar -xzf root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    rm root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    mv root /usr/local/root
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

    # larcv2
    cd /app
    git clone https://github.com/DeepLearnPhysics/larcv2
    source larcv2/configure.sh
    cd $LARCV_BASEDIR && make -j4
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

