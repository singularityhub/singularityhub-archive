---
id: 4065
name: "ucr-singularity/cs171"
branch: "master"
tag: "latest"
commit: "30f146a2521c96ff3e7cbe068486f9e84310c4e9"
version: "23abe670773f3726dc0f8d1ef6e07498"
build_date: "2020-01-14T20:06:29.549Z"
size_mb: 14057
size: 6937972767
sif: "https://datasets.datalad.org/shub/ucr-singularity/cs171/latest/2020-01-14-30f146a2-23abe670/23abe670773f3726dc0f8d1ef6e07498.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/cs171/latest/2020-01-14-30f146a2-23abe670/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cs171/latest/2020-01-14-30f146a2-23abe670/Singularity
collection: ucr-singularity/cs171
---

# ucr-singularity/cs171:latest

```bash
$ singularity pull shub://ucr-singularity/cs171:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%environment

PATH=/opt/conda/bin:$PATH
export PATH

# Path additions
export MKL_NUM_THREADS=3
export NUMEXPR_NUM_THREADS=3
export OMP_NUM_THREADS=3

%post
  
# Set up the PATH for other commands
export PATH=/opt/conda/bin:$PATH

# Update list of packages then upgrade them
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

# Workaround for https://github.com/-team/keras/issues/9567
apt-get install -y --allow-downgrades --no-install-recommends \
    --allow-change-held-packages \
    libcudnn7=7.0.5.15-1+cuda9.0 libcudnn7-dev=7.0.5.15-1+cuda9.0 
        
# Install dependencies
apt-get install -y --no-install-recommends build-essential cmake git curl vim ca-certificates libjpeg-dev libpng-dev
apt-get install -y screen terminator tmux vim wget 
apt-get install -y aptitude build-essential cmake g++ gfortran git pkg-config python-pip python-dev software-properties-common
apt-get install -y unrar
 
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

# Add PPA for ffmpeg
add-apt-repository -y ppa:jonathonf/ffmpeg-3
apt-get update
apt-get install -y ffmpeg

# More utilities
apt-get install -y graphviz libatlas-dev libfreetype6 libfreetype6-dev \
    libgraphviz-dev liblapack-dev swig libxft-dev libxml2-dev \
    libxslt-dev zlib1g-dev
 
# Gnuplot
apt-get install -y gnuplot-x11
    
# Clean up
apt-get -y autoremove
rm -rvf /var/lib/apt/lists/*

# Install miniconda
cd /opt
curl -o /opt/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x /opt/miniconda.sh
/opt/miniconda.sh -b -p /opt/conda 
rm /opt/miniconda.sh

# Install some packages
conda install numpy pyyaml scipy ipython mkl mkl-include
conda install -c soumith magma-cuda90
conda clean -ya
    
# Install the released version of Pytorch.
# Pytorch is (temporarily?) broken as of 2018-09-28
#conda install torchvision cuda90 -c pytorch
#conda install -c pytorch pytorch 

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

# TensorFlow, from conda instead of pip (pip is not working for it right now)
conda install -y -c anaconda tensorflow-gpu
#pip install --no-cache-dir tensorflow-gpu==1.8
    
# Deep Mind Sonnet
pip install --no-cache-dir dm-sonnet-gpu==1.17

# Theano
pip install --no-cache-dir Theano==1.0.1

# Keras
pip install --no-cache-dir keras==2.2.1
    
# OpenCV from pip, including contrib.  This makes the install MUCH faster.
# See https://pypi.python.org/pypi/opencv-contrib-python for capabilities 
# and limitations.  
pip install --no-cache-dir opencv-contrib-python    

# Install Pydensecrf
#pip install git+https://github.com/lucasb-eyer/pydensecrf.git

# Set locale in environment
echo 'export LC_ALL=C' >>$SINGULARITY_ENVIRONMENT
    
#Keras ml package
pip install --no-cache-dir keras_vggface
    
#For keras generator
pip install --no-cache-dir bcolz
    
#Neuro-Imaging package
pip install --no-cache-dir nibabel
pip install --no-cache-dir niftynet
pip install --no-cache-dir SimpleITK
    
#Parallel Processing
pip install --no-cache-dir joblib
    
#Progess
pip install --no-cache-dir tqdm
    
#Sklearn update
pip install --no-cache-dir scikit-learn==0.19.2

# For integration with JupyterHub
pip install --no-cache-dir ipykernel
    
# Workaround for Tensorflow from Anaconda looking for libcuda.so.1
ln -s /usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs/libcuda.so /usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs/libcuda.so.1

# Add packages that are also in system python via conda or pip
conda install -y -c anaconda scipy nose h5py scikit-image scikit-learn matplotlib pandas sympy virtualenv pygments sphinx

echo 'export PATH=/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs/' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ucr-singularity/cs171](https://github.com/ucr-singularity/cs171)
 - License: None

