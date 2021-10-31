---
id: 6519
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cuda-core-mpich-py36"
commit: "2770ca0cbd7ba270e39a54a378ea6a06e433b8db"
version: "6aa58f703ba678f5b46f2a2f6f330e52"
build_date: "2019-01-24T23:41:06.092Z"
size_mb: 5392
size: 2798333983
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-mpich-py36/2019-01-24-2770ca0c-6aa58f70/6aa58f703ba678f5b46f2a2f6f330e52.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-mpich-py36/2019-01-24-2770ca0c-6aa58f70/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cuda-core-mpich-py36/2019-01-24-2770ca0c-6aa58f70/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cuda-core-mpich-py36

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cuda-core-mpich-py36
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cuda-core-py36


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
Version centos7-cuda-core-mpich-py36

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
    scl enable rh-python36 bash

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
    pip3 --no-cache-dir --disable-pip-version-check install mpi4py
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

