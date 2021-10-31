---
id: 2269
name: "ucr-singularity/cuda-9.0-base"
branch: "master"
tag: "latest"
commit: "b47b3275624ff92a20191887bf3cddbd1e157011"
version: "be9088092a7922c9b8ee570a038edbb1"
build_date: "2020-12-18T16:39:57.346Z"
size_mb: 6773
size: 3361841183
sif: "https://datasets.datalad.org/shub/ucr-singularity/cuda-9.0-base/latest/2020-12-18-b47b3275-be908809/be9088092a7922c9b8ee570a038edbb1.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/cuda-9.0-base/latest/2020-12-18-b47b3275-be908809/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cuda-9.0-base/latest/2020-12-18-b47b3275-be908809/Singularity
collection: ucr-singularity/cuda-9.0-base
---

# ucr-singularity/cuda-9.0-base:latest

```bash
$ singularity pull shub://ucr-singularity/cuda-9.0-base:latest
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
    apt-get install -y unrar
   
    # Add PPA for ffmpeg
    add-apt-repository -y ppa:jonathonf/ffmpeg-3
    apt-get update
    apt-get install -y ffmpeg

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

 - Name: [ucr-singularity/cuda-9.0-base](https://github.com/ucr-singularity/cuda-9.0-base)
 - License: None

