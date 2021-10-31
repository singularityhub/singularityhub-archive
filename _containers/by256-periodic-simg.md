---
id: 9529
name: "by256/periodic"
branch: "master"
tag: "simg"
commit: "7f6c2525c43831a758be475a9c5197248831d7da"
version: "56f50bd95ab4565b8f3f9889140a9ee0"
build_date: "2019-06-05T15:20:41.410Z"
size_mb: 5678
size: 2672082975
sif: "https://datasets.datalad.org/shub/by256/periodic/simg/2019-06-05-7f6c2525-56f50bd9/56f50bd95ab4565b8f3f9889140a9ee0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/by256/periodic/simg/2019-06-05-7f6c2525-56f50bd9/
recipe: https://datasets.datalad.org/shub/by256/periodic/simg/2019-06-05-7f6c2525-56f50bd9/Singularity
collection: by256/periodic
---

# by256/periodic:simg

```bash
$ singularity pull shub://by256/periodic:simg
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%help
Centos7 with cuda9.0 cudnn7

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash


%environment

    # for system
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

    # Add cupti to the path for profiling:
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64

    source scl_source enable devtoolset-4

    export PATH=/usr/local/mpich/install/bin/:${PATH}
    export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:${LD_LIBRARY_PATH}

%post

    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y epel-release
    yum install -y centos-release-scl
    yum install -y devtoolset-4
    yum install -y wget emacs vim
    yum install -y emacs vim openssh-clients zip
    yum install -y python36-devel python36-setuptools python36-pip
    yum install -y hdf5

    # pip basics
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install future
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install pandas scikit-image scikit-learn Pillow opencv-python
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install jupyter notebook

    # tensorflow
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install --upgrade tensorflow-gpu==1.12.0
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install tensorboard
    
    # keras
    python3.6 -m pip --no-cache-dir --disable-pip-version-check install keras


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
```

## Collection

 - Name: [by256/periodic](https://github.com/by256/periodic)
 - License: [MIT License](https://api.github.com/licenses/mit)

