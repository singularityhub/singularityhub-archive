---
id: 6260
name: "keceli/ffn"
branch: "master"
tag: "horovod"
commit: "eb12c9fdc093c88fa6459ec26a278f63105e378c"
version: "2d348c314b1c437bb41f091a285ed1e9"
build_date: "2019-01-16T12:24:38.518Z"
size_mb: 4430
size: 2020831263
sif: "https://datasets.datalad.org/shub/keceli/ffn/horovod/2019-01-16-eb12c9fd-2d348c31/2d348c314b1c437bb41f091a285ed1e9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/ffn/horovod/2019-01-16-eb12c9fd-2d348c31/
recipe: https://datasets.datalad.org/shub/keceli/ffn/horovod/2019-01-16-eb12c9fd-2d348c31/Singularity
collection: keceli/ffn
---

# keceli/ffn:horovod

```bash
$ singularity pull shub://keceli/ffn:horovod
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-centos7

%help
Centos7 with cuda9.0 cudnn7
ML/DL packages  : tensorflow keras sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm 
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Modified by keceli
Version centos7-tf1.11.0-torch0.4.1

#------------
# Global installation
#------------
%environment
    
    # for system
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

    # Add cupti to the path for profiling:
#    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
    # for MPICH:
    export PATH=/usr/local/mpich/install/bin/:$PATH
    export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:$LD_LIBRARY_PATH

 #   source scl_source enable devtoolset-4
     export PATH=$PATH:/usr/local/mpich/install/bin
     export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpich/install/lib
%post
    
    # yum basics
    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y epel-release
    yum install -y wget emacs vim 
    yum install -y PyQt4 PyQt4-devel
    yum install -y emacs vim openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools
    yum install -y hdf5

    #mpich
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
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpich/install/lib
    cd -
 

    # pip basics
    pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
    pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    # for python2.7
    pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  # for python2.7
    pip --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables
    pip --no-cache-dir --disable-pip-version-check install  pandas scikit-image scikit-learn Pillow opencv-python
    pip --no-cache-dir --disable-pip-version-check install jupyter notebook


    # tensorflow
    pip --no-cache-dir --disable-pip-version-check install --upgrade tensorflow-gpu==1.11.0
    pip --no-cache-dir --disable-pip-version-check install tensorboard

    # keras
    pip --no-cache-dir --disable-pip-version-check install keras

    # tensorflow with mkl-dnn:
    pip install https://storage.googleapis.com/intel-optimized-tensorflow/tensorflow-1.11.0-cp27-cp27mu-linux_x86_64.whl
  
    # mpi and horovod
    pip --no-cache-dir --disable-pip-version-check install mpi4py
    HOROVOD_WITH_TENSORFLOW=1 pip --no-cache-dir --disable-pip-version-check install horovod==0.15.0
  
   # ffn
    git clone https://github.com/google/ffn.git
    pip --no-cache-dir --disable-pip-version-check install h5py

    git clone https://github.com/wushidonguc/distributed_ffn.git
```

## Collection

 - Name: [keceli/ffn](https://github.com/keceli/ffn)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

