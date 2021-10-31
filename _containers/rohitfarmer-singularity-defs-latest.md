---
id: 3746
name: "rohitfarmer/singularity-defs"
branch: "master"
tag: "latest"
commit: "de59e3770edfa316555cc33c914feb6f772152ce"
version: "7a30384d2780f222ab540c396915ff12"
build_date: "2019-07-29T18:06:45.489Z"
size_mb: 6468
size: 3004256287
sif: "https://datasets.datalad.org/shub/rohitfarmer/singularity-defs/latest/2019-07-29-de59e377-7a30384d/7a30384d2780f222ab540c396915ff12.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rohitfarmer/singularity-defs/latest/2019-07-29-de59e377-7a30384d/
recipe: https://datasets.datalad.org/shub/rohitfarmer/singularity-defs/latest/2019-07-29-de59e377-7a30384d/Singularity
collection: rohitfarmer/singularity-defs
---

# rohitfarmer/singularity-defs:latest

```bash
$ singularity pull shub://rohitfarmer/singularity-defs:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%labels

    APPLICATION_NAME tensorflow-gpu and Chemistry
    APPLICATION_VERSION 1.9
    APPLICATION_URL https://www.tensorflow.org

    SYSTEM_NAME Comet, SDSC (XSEDE) (Can't run just now due to old Nvidia drivers)
    NOTE Tested on a laptop with GeForce MX150 GPU

    AUTHOR_NAME Rohit Farmer
    AUTHOR_EMAIL rohit.farmer@gmail.com

    LAST_UPDATED 27 July 2018

%help
    This container conatins:
        Tensorflow-gpu == 1.9.0
        Keras (latest)
        Tflon (A wraper for TensorFlow https://bitbucket.org/mkmatlock/tflon, build 27 July 2018)
        Numpy, Pandas, Scipy, Sklearn, Matplotlib (latest)
        OpenBabel, Pybel, RDKit (latest)

    Untested:
        OpenMpi (Cuda aware) and Horovod

%setup
    # Set system locale
    export LC_ALL=C

%environment

    # Set system locale
    export LC_ALL=C

    LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:/usr/local/cuda-9.0/extras/CUPTI/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/.singularity.d/libs
    PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
  
%post
    
    # Make filesystem mount points
    mkdir /cvmfs /oasis /projects /scratch

    # Change to tmp directory to download temporary files
    cd /tmp

    apt-get -y update --fix-missing
    apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        cmake \
        cuda-9.0 \
        gcc \
        g++ \
        gfortran \
        git \
        libtool \
        libjpeg-dev \
        libpng-dev \
        libatlas-base-dev \
        libxml2-dev \
        zlib1g-dev \
        libcairo2-dev \
        libeigen2-dev \
        libeigen3-dev \
        libcupti-dev \
        libpcre3-dev \
        sqlite3 \
        libsqlite3-dev \
        libboost-dev \
        libboost-system-dev \
        libboost-thread-dev \
        libboost-serialization-dev \
        libboost-python-dev \
        libboost-regex-dev \
        mercurial \
        vim \
        wget \
        pkg-config \
        python \
        python-dev \
        python-pip \
        python-setuptools \
        swig \
        zip


# Additional python packages
    pip --no-cache-dir install numpy==1.14.0
    pip --no-cache-dir install pandas==0.22.0

# Install Tensorflow-gpu
    pip --no-cache-dir install tensorflow-gpu==1.9.0
    pip --no-cache-dir install keras

# Install tflon
    pip --no-cache-dir install dill openopt h5py pyarrow sklearn scikit-image skll FuncDesigner statsmodels matplotlib

    hg clone https://bitbucket.org/mkmatlock/tflon
    cd tflon
    pip install .

# Install RDKit
    apt-get install -y python-rdkit librdkit1 rdkit-data

# Install OpenBabel
    mkdir -p /tmp/openbabel
    cd /tmp/openbabel
    wget -O openbabel-2-4-1.tar.gz https://github.com/openbabel/openbabel/archive/openbabel-2-4-1.tar.gz
    tar zxf openbabel-2-4-1.tar.gz
    mkdir openbabel.build
    cd openbabel.build
    cmake ../openbabel-openbabel-2-4-1 -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON
    make -j $(nproc)
    make install

# Install MPI (Match the version with the cluster)
    mkdir -p /tmp/mpi
    cd /tmp/mpi
    wget -O openmpi-2.1.0.tar.bz2 https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.0.tar.bz2
    tar -xjf openmpi-2.1.0.tar.bz2
    cd openmpi-2.1.0
    ./configure --prefix=/usr/local --with-cuda
    make -j $(nproc)
    make install
    ldconfig

    pip --no-cache-dir install mpi4py
    HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_GPU_ALLGATHER=MPI HOROVOD_GPU_BROADCAST=MPI pip --no-cache-dir install horovod

# Cleanup
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    rm -rf /tmp/openbabel /tmp/mpi /tmp/tflon
```

## Collection

 - Name: [rohitfarmer/singularity-defs](https://github.com/rohitfarmer/singularity-defs)
 - License: [MIT License](https://api.github.com/licenses/mit)

