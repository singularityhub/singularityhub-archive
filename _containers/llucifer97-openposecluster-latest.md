---
id: 9815
name: "llucifer97/openposecluster"
branch: "master"
tag: "latest"
commit: "87b8ddd2daa2ad3b1f33c729c619a5a0cb048f24"
version: "39ff178f7c5b34f7ed1d30d4d07b106e"
build_date: "2020-01-13T19:08:23.793Z"
size_mb: 4741
size: 1917321247
sif: "https://datasets.datalad.org/shub/llucifer97/openposecluster/latest/2020-01-13-87b8ddd2-39ff178f/39ff178f7c5b34f7ed1d30d4d07b106e.simg"
url: https://datasets.datalad.org/shub/llucifer97/openposecluster/latest/2020-01-13-87b8ddd2-39ff178f/
recipe: https://datasets.datalad.org/shub/llucifer97/openposecluster/latest/2020-01-13-87b8ddd2-39ff178f/Singularity
collection: llucifer97/openposecluster
---

# llucifer97/openposecluster:latest

```bash
$ singularity pull shub://llucifer97/openposecluster:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:ubuntu:18.04

%labels
AUTHOR Peter Uhrig
BASED_ON https://github.com/rianders/docker-openpose/blob/master/Dockerfile

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
apt-get update && apt-get install -y --no-install-recommends software-properties-common wget
add-apt-repository universe
apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates curl git nano less \
  build-essential cmake cmake-gui pkg-config libopencv-dev caffe-cpu libgoogle-glog-dev libcaffe-cpu-dev \
  libboost-dev libprotobuf-dev gpg-agent locales language-pack-en
locale-gen en_US.UTF-8 && dpkg-reconfigure locales
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list
apt-get update && apt-get install -y --no-install-recommends intel-mkl-64bit-2018.2

# option caffe-cuda
# http://caffe.berkeleyvision.org/install_apt.html
# In case we need to turn off ssl verify
# RUN
apt install -y python3-pip
apt install -y git-all 
apt update	

  git config --global http.sslVerify false
         
# Installing some Python packages that are needed for pre-processing
  apt install -y python3 python3-matplotlib python3-numpy
  pip3 install pillow numpy opencv-python image sklearn statistics beautifulsoup4 ipaddress ipykernel ipython ipython-genutils ipywidgets jsonschema jupyter jupyter-client jupyter-console jupyter-core natsort notebook bqplot pandas scikit-image scikit-learn seaborn plotly requests appmode 

mkdir /localdata
cd /localdata
mkdir src
cd src
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
cd openpose
mkdir build
cd build
export MKLVARS_ARCHITECTURE=intel64
. /opt/intel/mkl/bin/mklvars.sh
# Apparently not all shells allow parameters with source.
#. /opt/intel/mkl/bin/mklvars.sh intel64

cmake -DGPU_MODE=CPU_ONLY -DBUILD_CAFFE=OFF -DCaffe_INCLUDE_DIRS=/usr/include/caffe/ -DCaffe_LIBS=/usr/lib/x86_64-linux-gnu/libcaffe.so ..
make
make install
apt update	
         
%runscript
git clone https://github.com/llucifer97/openposecluster.git
cd openposecluster

python3 pose.py
```

## Collection

 - Name: [llucifer97/openposecluster](https://github.com/llucifer97/openposecluster)
 - License: None

