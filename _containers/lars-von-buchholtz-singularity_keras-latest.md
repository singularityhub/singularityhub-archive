---
id: 878
name: "lars-von-buchholtz/singularity_keras"
branch: "master"
tag: "latest"
commit: "294f031c3fe846b38f89e5d632ed32e512874714"
version: "679fe18db268b5236e94c6ea8245c4c3"
build_date: "2019-05-15T16:11:36.314Z"
size_mb: 3722
size: 1769246751
sif: "https://datasets.datalad.org/shub/lars-von-buchholtz/singularity_keras/latest/2019-05-15-294f031c-679fe18d/679fe18db268b5236e94c6ea8245c4c3.simg"
url: https://datasets.datalad.org/shub/lars-von-buchholtz/singularity_keras/latest/2019-05-15-294f031c-679fe18d/
recipe: https://datasets.datalad.org/shub/lars-von-buchholtz/singularity_keras/latest/2019-05-15-294f031c-679fe18d/Singularity
collection: lars-von-buchholtz/singularity_keras
---

# lars-von-buchholtz/singularity_keras:latest

```bash
$ singularity pull shub://lars-von-buchholtz/singularity_keras:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04

################################################################################
%labels
################################################################################
MAINTAINER Wolfgang Resch/Lars von Buchholtz
VERSION v3

################################################################################
%environment
################################################################################
export PATH=/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:

################################################################################
%post
################################################################################

###
### install keras + tensorflow + other useful packages
###

echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
apt-get update 
apt-get install -y software-properties-common python-software-properties
add-apt-repository main
add-apt-repository universe
add-apt-repository multiverse
apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        ca-certificates \
        curl \
        g++ \
        git \
        libtool \
        make \
        python-dev \
        python-setuptools \
        unzip doxygen

apt-get install -y --no-install-recommends \
        ca-certificates \
        cmake \
        curl \
        g++ \
        git \
        libatlas-base-dev \
        libboost-filesystem-dev \
        libboost-python-dev \
        libboost-system-dev \
        libboost-thread-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libnccl-dev=1.2.3-1+cuda8.0 \
        libopencv-dev \
        libsnappy-dev \
        python-all-dev \
        python-h5py \
        python-matplotlib \
        python-opencv \
        python-pil \
        python-pydot \
        python-scipy \
        python-skimage \
        python-sklearn libhdf5-dev graphviz locales python3-dev python3-pip

locale-gen en_US.UTF-8
apt-get clean

pip3 install --upgrade setuptools
pip3 install tensorflow-gpu==1.3.0
pip3 install keras==2.0.8
pip3 install -U Pillow scikit-learn pandas matplotlib notebook ipython numpy nibabel scipy Cython six tqdm 
pip3 install -U opencv-python
pip3 install git+https://github.com/aleju/imgaug
pip3 install git+https://github.com/matterport/Mask_RCNN
### 
###
### destination for NIH HPC bind mounts
###

mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /gs7 /gs8 /data /scratch /fdb /lscratch
```

## Collection

 - Name: [lars-von-buchholtz/singularity_keras](https://github.com/lars-von-buchholtz/singularity_keras)
 - License: None

