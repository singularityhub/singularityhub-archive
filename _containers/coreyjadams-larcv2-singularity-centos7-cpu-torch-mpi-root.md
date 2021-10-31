---
id: 6465
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cpu-torch-mpi-root"
commit: "34cc9a4755ca1d3213b1fdce1bc0a1b9730a75d8"
version: "afaec0461f92fcf2ee7e0a6650415e53"
build_date: "2019-01-23T06:03:10.691Z"
size_mb: 3549
size: 1446187039
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch-mpi-root/2019-01-23-34cc9a47-afaec046/afaec0461f92fcf2ee7e0a6650415e53.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch-mpi-root/2019-01-23-34cc9a47-afaec046/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch-mpi-root/2019-01-23-34cc9a47-afaec046/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cpu-torch-mpi-root

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cpu-torch-mpi-root
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cpu-torch-mpi

#Bootstrap: localimage
#From: /home/cadams/DeepLearnPhysics/larcv2-singularity/centos7-cpu-torch1.0rc-mpich3.2.1


%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : torch keras sc-learn nccl
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python ROOT
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py horovod
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client mpich

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cpu-torch1.0rc-mpich3.2.1-root6.14.04

#------------
# Global installation
#------------
%environment
 
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    export LD_LIBRARY_PATH=/usr/local/root/lib/:${LD_LIBRARY_PATH}

%post

    # ROOT
    wget https://root.cern.ch/download/root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    tar -xzf root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    rm root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    mv root /usr/local/root
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

