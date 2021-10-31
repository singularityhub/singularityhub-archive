---
id: 6261
name: "keceli/ffn"
branch: "master"
tag: "centos7-mkl_dnn-tf1.11.0-root6.14.04-mpich3.2.1"
commit: "00b86e3498e3c81e0739764ee6f3f00d1a966152"
version: "ef3943ea0b788a6135b1079eb670cad1"
build_date: "2019-01-16T07:21:12.067Z"
size_mb: 2603
size: 898850847
sif: "https://datasets.datalad.org/shub/keceli/ffn/centos7-mkl_dnn-tf1.11.0-root6.14.04-mpich3.2.1/2019-01-16-00b86e34-ef3943ea/ef3943ea0b788a6135b1079eb670cad1.simg"
url: https://datasets.datalad.org/shub/keceli/ffn/centos7-mkl_dnn-tf1.11.0-root6.14.04-mpich3.2.1/2019-01-16-00b86e34-ef3943ea/
recipe: https://datasets.datalad.org/shub/keceli/ffn/centos7-mkl_dnn-tf1.11.0-root6.14.04-mpich3.2.1/2019-01-16-00b86e34-ef3943ea/Singularity
collection: keceli/ffn
---

# keceli/ffn:centos7-mkl_dnn-tf1.11.0-root6.14.04-mpich3.2.1

```bash
$ singularity pull shub://keceli/ffn:centos7-mkl_dnn-tf1.11.0-root6.14.04-mpich3.2.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%help
Centos7 with mkl_dnn tensorflow
ML/DL packages  : tensorflow keras torch sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py horovod
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client openmpi

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-mkldnn-tf1.11.0-torch0.4.1

#------------
# Global installation
#------------
%environment

    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    export LD_LIBRARY_PATH=/usr/local/root/lib/:$LD_LIBRARY_PATH

    # for MPICH:
    export PATH=/usr/local/mpich/install/bin/:$PATH
    export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:$LD_LIBRARY_PATH

%post

    # yum
    yum update -y
    yum groupinstall -y "Development Tools"
    yum install -y epel-release
    yum install -y wget emacs vim 
    yum install -y PyQt4 PyQt4-devel
    yum install -y emacs vim openssh-clients zip 
    yum install -y python-devel python-pip  python-setuptools
    yum install -y hdf5

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

    # ROOT
    wget https://root.cern.ch/download/root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    tar -xzf root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    rm root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    mv root /usr/local/root
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

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
```

## Collection

 - Name: [keceli/ffn](https://github.com/keceli/ffn)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

