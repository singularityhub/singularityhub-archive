---
id: 8637
name: "DeepLearnPhysics/larcv2-singularity"
branch: "master"
tag: "ub18.04-cuda100-py3-pytorch1.0.1-scn"
commit: "9c4cf389dd498c669e836103ec2f29722f956de9"
version: "cf7d2d90658054f93770d08a9b8e3b82"
build_date: "2020-06-10T13:46:33.614Z"
size_mb: 7021
size: 3307765791
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub18.04-cuda100-py3-pytorch1.0.1-scn/2020-06-10-9c4cf389-cf7d2d90/cf7d2d90658054f93770d08a9b8e3b82.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/larcv2-singularity/ub18.04-cuda100-py3-pytorch1.0.1-scn/2020-06-10-9c4cf389-cf7d2d90/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub18.04-cuda100-py3-pytorch1.0.1-scn/2020-06-10-9c4cf389-cf7d2d90/Singularity
collection: DeepLearnPhysics/larcv2-singularity
---

# DeepLearnPhysics/larcv2-singularity:ub18.04-cuda100-py3-pytorch1.0.1-scn

```bash
$ singularity pull shub://DeepLearnPhysics/larcv2-singularity:ub18.04-cuda100-py3-pytorch1.0.1-scn
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

%help
Ubuntu18.04 with cuda10 cudnn7
ML/DL packages  : torch sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ubuntu16.04-root06.08.06-gpu-py3

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    export CUDA_DEVICE_ORDER=PCI_BUS_ID
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH="${ROOTSYS}/lib:${LD_LIBRARY_PATH}"
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

    export LARCV_BASEDIR=/app/larcv2
    export LARCV_BUILDDIR="${LARCV_BASEDIR}/build"
    export LARCV_COREDIR="${LARCV_BASEDIR}/larcv/core"
    export LARCV_APPDIR="${LARCV_BASEDIR}/larcv/app"
    export LARCV_LIBDIR="${LARCV_BUILDDIR}/lib"
    export LARCV_INCDIR="${LARCV_BUILDDIR}/include"
    export LARCV_BINDIR="${LARCV_BUILDDIR}/bin"
    export LARCV_ROOT6=1
    export LARCV_CXX=g++

# with numpy
    export LARCV_NUMPY=1
    export LARCV_INCLUDES="-I/app/larcv2/build/include -I/usr/include/python3.6m -I/usr/include/python3.6m -I/usr/local/lib/python3.6/dist-packages/numpy/core/include"
    export LARCV_LIBS="-L/usr/lib/ -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu -L/usr/lib -lpython3.6m -lpthread -ldl -lutil -lm -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions -L/app/larcv2/build/lib -llarcv"

# set bin and lib path
    export PATH=${LARCV_BASEDIR}/bin:${LARCV_BINDIR}:${PATH}
    export LD_LIBRARY_PATH=${LARCV_LIBDIR}:${LD_LIBRARY_PATH}:
    export PYTHONPATH=${LARCV_BASEDIR}/python:${PYTHONPATH}
    
%post
    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip git wget emacs vim
    apt-get -y install zsh dpkg-dev g++ gcc binutils cmake libqt4-dev screen tmux
    apt-get -y install python3-dev python3-tk python3-pip python3-setuptools 
    apt-get -y install git wget emacs vim openssh-client curl
    apt-get -y install libsparsehash-dev libhdf5-dev

    # asciinema
    apt-get install -y locales
    locale-gen en_US.UTF-8 
    apt-get -y install software-properties-common #python-software-properties
    apt-add-repository -y ppa:zanchey/asciinema
    apt-get -y update
    apt-get -y install asciinema

    # pip basics
    pip3 --no-cache-dir install --upgrade setuptools
    pip3 --no-cache-dir install numpy wheel zmq six pygments pyyaml cython
    pip3 --no-cache-dir install gputil psutil humanize h5py tqdm
    pip3 --no-cache-dir install scipy tables pandas scikit-image scikit-learn Pillow opencv-python
    pip3 --no-cache-dir install matplotlib seaborn plotly cufflinks
    pip3 --no-cache-dir install ipython #'ipython<6.0'
    pip3 --no-cache-dir install ipykernel
    pip3 --no-cache-dir install jupyter notebook

    # pytorch
    pip3 --no-cache-dir install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl
    pip3 --no-cache-dir install torchvision

    # ROOT
    apt-get -y install libxpm-dev libxft-dev libxext-dev libssl-dev libftgl-dev libfftw3-dev libxml2-dev libkrb5-dev
    #wget https://root.cern.ch/download/root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    #wget https://web.stanford.edu/~kterao/ub18.04-py3-rootv6.16.00.tgz
    wget https://www.nevis.columbia.edu/~kazuhiro/ub18.04-py3-rootv6.16.00.tgz
    tar -xzf ub18.04-py3-rootv6.16.00.tgz
    rm ub18.04-py3-rootv6.16.00.tgz
    mv root.v6.16.00 /usr/local/root
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

    # larcv
    mkdir -p /app
    cd /app
    git clone https://github.com/DeepLearnPhysics/larcv2
    cd larcv2
    git checkout python3
    export LARCV_BASEDIR=/app/larcv2
    export LARCV_BUILDDIR="${LARCV_BASEDIR}/build"
    export LARCV_COREDIR="${LARCV_BASEDIR}/larcv/core"
    export LARCV_APPDIR="${LARCV_BASEDIR}/larcv/app"
    export LARCV_LIBDIR="${LARCV_BUILDDIR}/lib"
    export LARCV_INCDIR="${LARCV_BUILDDIR}/include"
    export LARCV_BINDIR="${LARCV_BUILDDIR}/bin"
    export LARCV_ROOT6=1
    export LARCV_CXX=g++
    export LARCV_NUMPY=1
    export LARCV_PYTHON=/usr/bin/python3
    export LARCV_PYTHON_CONFIG=python3.6-config
    export LARCV_INCLUDES=" -I/app/larcv2/build/include -I/usr/include/python3.6m -I/usr/include/python3.6m -I/usr/local/lib/python3.6/dist-packages/numpy/core/include"
    export LARCV_LIBS=" -L/usr/lib/ -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu -L/usr/lib -lpython3.6m -lpthread -ldl -lutil -lm -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions -L/app/larcv2/build/lib -llarcv"

    # set bin and lib path
    export PATH=${LARCV_BASEDIR}/bin:${LARCV_BINDIR}:${PATH}
    export LD_LIBRARY_PATH=${LARCV_LIBDIR}:${LD_LIBRARY_PATH}:
    export PYTHONPATH=${LARCV_BASEDIR}/python:${PYTHONPATH}
    mkdir -p $LARCV_BUILDDIR
    mkdir -p $LARCV_LIBDIR
    mkdir -p $LARCV_BINDIR
    make -j4

    # scn
    #mkdir -p /app && cd /app
    #git clone https://github.com/facebookresearch/SparseConvNet
    #git clone https://github.com/DeepLearnPhysics/SparseConvNet
    #cd SparseConvNet
    #git checkout pytorch_dev20181225
    #python3 setup.py install 
    pip3 --no-cache-dir install -i https://test.pypi.org/simple/ scn-cuda10-py3
```

## Collection

 - Name: [DeepLearnPhysics/larcv2-singularity](https://github.com/DeepLearnPhysics/larcv2-singularity)
 - License: None

