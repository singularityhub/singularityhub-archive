---
id: 2394
name: "aizjForever/darch_recipe"
branch: "master"
tag: "cuda"
commit: "41dbe7ba4de9a7a947d1582419ba52c3be4b2fda"
version: "5e6f03306a226c108e2a89ad9494cc4b"
build_date: "2018-04-05T16:53:48.370Z"
size_mb: 6748
size: 3340107807
sif: "https://datasets.datalad.org/shub/aizjForever/darch_recipe/cuda/2018-04-05-41dbe7ba-5e6f0330/5e6f03306a226c108e2a89ad9494cc4b.simg"
url: https://datasets.datalad.org/shub/aizjForever/darch_recipe/cuda/2018-04-05-41dbe7ba-5e6f0330/
recipe: https://datasets.datalad.org/shub/aizjForever/darch_recipe/cuda/2018-04-05-41dbe7ba-5e6f0330/Singularity
collection: aizjForever/darch_recipe
---

# aizjForever/darch_recipe:cuda

```bash
$ singularity pull shub://aizjForever/darch_recipe:cuda
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel

%post

    # Update list of available packages, then upgrade them
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

    # Workaround for https://github.com/keras-team/keras/issues/9567
    apt-get install -y --allow-downgrades --no-install-recommends \
        libcudnn7=7.0.5.15-1+cuda9.0 libcudnn7-dev=7.0.5.15-1+cuda9.0 
    
    # Utility and support packages
    apt-get install -y screen terminator tmux vim wget 
    apt-get install -y aptitude build-essential cmake g++ gfortran git \
        pkg-config python-pip python-dev software-properties-common
   
    # More utilities
    apt-get install -y graphviz libatlas-dev libfreetype6 libfreetype6-dev \
        libgraphviz-dev liblapack-dev swig libxft-dev libxml2-dev \
        libxslt-dev zlib1g-dev
 
    # Python modules from system package manager
    apt-get install -y python-numpy python-scipy python-nose python-h5py \
        python-skimage python-matplotlib python-pandas python-sklearn \
        python-sympy python-virtualenv
   
    # More dependencies/useful software from system package manager
    apt-get install -v libopenblas-dev libfreetype7-dev libpng12-dev \
        libglib2.0-0 libsm6 libxext6 libxrender1
    
    # Caffe dependencies  
    apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev \
        libhdf5-serial-dev protobuf-compiler
    apt-get install --no-install-recommends -y libboost-all-dev
    apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev

    # Theano dependencies not already installed
    apt-get install -y python-pygments python-sphinx 

    # Dense Flow dependencies
    apt-get install -y libzip-dev

    # OpenCV build dependencies not already installed  
    apt-get install -y checkinstall yasm libjpeg-dev libjpeg8-dev \
        libjasper-dev libavcodec-dev libavformat-dev libswscale-dev \
        libdc1394-22-dev libgstreamer0.10-dev \
        libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy \
        libtbb-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev \
        libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev \
        libxvidcore-dev x264 v4l-utils libgtk-3-dev

    # PIL (actually Pillow)
    pip install --no-cache-dir Pillow
    
    # Jupyter and jupyterlab
    pip install --no-cache-dir jupyter
    pip install --no-cache-dir jupyterlab

    # Various useful Python packages
    pip install --no-cache-dir pygraphviz
    pip install --no-cache-dir networkx
    pip install --no-cache-dir numexpr
    pip install --no-cache-dir pymc
    pip install --no-cache-dir patsy
    pip install --no-cache-dir Cython
    pip install --no-cache-dir statsmodels
    pip install --no-cache-dir restview
    pip install --no-cache-dir tinkerer
    pip install --no-cache-dir Pweave
    pip install --no-cache-dir numba

    # Gnuplot
    apt-get install -y gnuplot-x11

    # Clean up
    apt-get -y autoremove
    rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [aizjForever/darch_recipe](https://github.com/aizjForever/darch_recipe)
 - License: None

