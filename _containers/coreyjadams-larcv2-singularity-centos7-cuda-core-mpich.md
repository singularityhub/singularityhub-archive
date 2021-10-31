---
id: 6449
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-core-mpich"
commit: "fa0ddaa6e0b94dd9cd5f5749f219a0f5561acf98"
version: "8db2ca8f76a10320dfd2571d2898726c"
build_date: "2019-01-24T17:50:06.094Z"
size_mb: 4887
size: 2632130591
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-mpich/2019-01-24-fa0ddaa6-8db2ca8f/8db2ca8f76a10320dfd2571d2898726c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-mpich/2019-01-24-fa0ddaa6-8db2ca8f/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-mpich/2019-01-24-fa0ddaa6-8db2ca8f/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-core-mpich

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-core-mpich
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cuda-core


%help
Centos7 with cuda9.0 cudnn7, mpich, nccl
ML/DL packages  : keras sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python ROOT
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client mpich

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cuda-core-mpich

#------------
# Global installation
#------------
%environment
 

    # for MPICH:
    export PATH=/usr/local/mpich/install/bin/:${PATH}
    export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:${LD_LIBRARY_PATH}

    # This line is necessary to run on Cooley:
    export NCCL_P2P_DISABLE=1

%post

    scl enable devtoolset-4 bash

    # install MPICH
    wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
    tar xf mpich-3.2.1.tar.gz
    rm mpich-3.2.1.tar.gz
    cd mpich-3.2.1
    # disable the addition of the RPATH to compiled executables
    # this allows us to override the MPI libraries to use those
    # found via LD_LIBRARY_PATH
    ./configure --prefix=/usr/local/mpich/install --disable-wrapper-rpath
    make -j 4 install
    # add to local environment to build pi.c
    export PATH=$PATH:/usr/local/mpich//install/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpich//install/lib
    env | sort
    cd ..
    rm -rf mpich-3.2.1


    # nccl2
    git clone https://github.com/NVIDIA/nccl.git
    cd nccl;
    make -j src.build
    make pkg.redhat.build
    rpm -i build/pkg/rpm/x86_64/libnccl* 
    cd -


    # Add mpi4py and horovod:
    pip --no-cache-dir --disable-pip-version-check install mpi4py
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

