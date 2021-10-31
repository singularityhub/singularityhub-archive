---
id: 2947
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "openpose"
commit: "ecb7077eedb52af1ca91ecaec78e66f4c9fb3ba3"
version: "d4536da09993bd95201b7be9c48ba0cd"
build_date: "2021-04-08T19:54:45.707Z"
size_mb: 4033
size: 1662717983
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/openpose/2021-04-08-ecb7077e-d4536da0/d4536da09993bd95201b7be9c48ba0cd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/RedHenLab/singularity_containers/openpose/2021-04-08-ecb7077e-d4536da0/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/openpose/2021-04-08-ecb7077e-d4536da0/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:openpose

```bash
$ singularity pull shub://RedHenLab/singularity_containers:openpose
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
  build-essential cmake pkg-config libopencv-dev caffe-cpu libgoogle-glog-dev libcaffe-cpu-dev \
  libboost-dev libprotobuf-dev gpg-agent locales language-pack-en
locale-gen en_US.UTF-8 && dpkg-reconfigure locales
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list
apt-get update && apt-get install -y --no-install-recommends intel-mkl-64bit-2018.2

# option caffe-cuda
# http://caffe.berkeleyvision.org/install_apt.html
# In case we need to turn off ssl verify
# RUN  git config --global http.sslVerify false

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
```

## Collection

 - Name: [RedHenLab/singularity_containers](https://github.com/RedHenLab/singularity_containers)
 - License: None

