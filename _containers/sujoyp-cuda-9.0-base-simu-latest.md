---
id: 4945
name: "sujoyp/cuda-9.0-base-simu"
branch: "master"
tag: "latest"
commit: "c447c059c000b34e617eef6175bb30d4a4b38eb8"
version: "9349c95bef421302f22a02e4f0eb3c0e"
build_date: "2018-09-24T07:21:06.638Z"
size_mb: 6508
size: 3367157791
sif: "https://datasets.datalad.org/shub/sujoyp/cuda-9.0-base-simu/latest/2018-09-24-c447c059-9349c95b/9349c95bef421302f22a02e4f0eb3c0e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sujoyp/cuda-9.0-base-simu/latest/2018-09-24-c447c059-9349c95b/
recipe: https://datasets.datalad.org/shub/sujoyp/cuda-9.0-base-simu/latest/2018-09-24-c447c059-9349c95b/Singularity
collection: sujoyp/cuda-9.0-base-simu
---

# sujoyp/cuda-9.0-base-simu:latest

```bash
$ singularity pull shub://sujoyp/cuda-9.0-base-simu:latest
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
        --allow-change-held-packages \
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
 
    # Python modules from stem package manager
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

    # simulation dependencies
    apt-get install -y cmake cmake-curses-gui
    apt-get install -y libxaw7-dev libxt-dev
    apt-get install -y freeglut3-dev
    apt-get install -y libfreetype6-dev
    apt-get install -y libxrandr-dev
    apt-get install -y --no-install-recommends libboost-all-dev
    apt-get install -y zlib1g-dev libfreeimage-dev libois-dev libtinyxml-dev libzzip-dev libcppunit-dev libglew-dev libdevil-dev
    apt-get install -y libeigen3-dev

    # PIL (actually Pillow)
    pip install --no-cache-dir Pillow
    
    # Jupyter and jupyterlab
    pip install --no-cache-dir jupyter
    # Jupyterlab doesn't support Python 2.7 
    #pip install --no-cache-dir jupyterlab
    

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
    #pip install --no-cache-dir Pweave
    pip install --no-cache-dir numba

    # Gnuplot
    apt-get install -y gnuplot-x11

    # Clean up
    apt-get -y autoremove
rm -rvf /var/lib/apt/lists/*
```

## Collection

 - Name: [sujoyp/cuda-9.0-base-simu](https://github.com/sujoyp/cuda-9.0-base-simu)
 - License: None

