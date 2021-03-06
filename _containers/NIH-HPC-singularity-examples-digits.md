---
id: 873
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "digits"
commit: "57e92739d77fdc0b9a2374f8d2fa8dd1f6924694"
version: "240a885e7841258731bdd9fe9d27fcf3"
build_date: "2019-08-23T19:57:55.467Z"
size_mb: 4492
size: 1918017567
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/digits/2019-08-23-57e92739-240a885e/240a885e7841258731bdd9fe9d27fcf3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NIH-HPC/singularity-examples/digits/2019-08-23-57e92739-240a885e/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/digits/2019-08-23-57e92739-240a885e/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:digits

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:digits
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

%post
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
mkdir /protobuf
export PROTOBUF_ROOT=/protobuf
cd /protobuf

git clone -b '3.2.x' https://github.com/google/protobuf.git .
    ./autogen.sh
    ./configure --prefix=/usr/local/protobuf
    make "-j$(nproc)"
    make install
    cd python
    python setup.py install --cpp_implementation
apt-get update
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
        python-sklearn

# Build pip
curl -O https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    pip install --upgrade --no-cache-dir pip
apt-get -y install libprotobuf-dev protobuf-compiler

# Build caffe
mkdir /caffe
export CAFFE_ROOT=/caffe
git clone https://github.com/nvidia/caffe.git /caffe -b 'caffe-0.15'
    cd /caffe
    pip install ipython==5.4.1
    pip install -r python/requirements.txt
#    cat python/requirements.txt | xargs -n1 pip install
    mkdir build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/caffe -DUSE_NCCL=ON \
-DUSE_CUDNN=ON -DCUDA_ARCH_NAME=Manual -DCUDA_ARCH_BIN="35 52 60 61" \
-DCUDA_ARCH_PTX="61" ..
    make -j"$(nproc)"
    make install
    make pycaffe
    cd /


# Install the packages to get pip installed or else we run into numpy problems
apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        python

# Build pip, need to do this before DIGITS packages or else we get numpy problems
curl -O https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    pip install --upgrade --no-cache-dir pip

apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        graphviz \
        gunicorn \
        libatlas3-base \
        libboost-filesystem1.58.0 \
        bboost-python1.58.0 \
        libboost-system1.58.0 \
        libboost-thread1.58.0 \
        libfreetype6-dev \
        libgoogle-glog0v5 \
        libhdf5-serial-dev \
        libleveldb1v5 \
        libnccl1=1.2.3-1+cuda8.0 \
        libopencv-core2.4v5 \
        libopencv-highgui2.4v5 \
        libopencv-imgproc2.4v5 \
        libpng12-dev \
        libzmq5 \
        nginx \
        pkg-config \
        python-dev \
        python-flask \
        python-flaskext.socketio \
        python-flaskext.wtf \
        python-gevent \
        python-lmdb \
        python-opencv \
        python-pil \
        python-pydot \
        python-requests \
        python-six \
        python-skimage \
        python-tk \
        python-wtforms \
        rsync \
        software-properties-common
        rm -rf /var/lib/apt/lists/*

pip install https://github.com/NVIDIA/DIGITS/archive/v6.0.1.tar.gz

pip install --no-cache-dir \
        setuptools\>=18.5 \
        tensorflow-gpu==1.2.1 \
        protobuf==3.2.0

mkdir /gpfs /gs2 /gs3 /gs4 /gs5 /gs6 /gs7 /gs8 /gs9 /gs10 /gs11 /gs12 /spin1 /data /scratch /fdb /lscratch
apt-get clean

%environment
export DIGITS_JOBS_DIR=/mnt
export DIGITS_LOGFILE_FILENAME=/mnt/digits.log
export PYTHONPATH=/usr/local/python
export DIGITS_VERSION=6.0
export PATH=/usr/local/caffe/bin/:$PATH
export PYTHONPATH=/usr/local/caffe/python/:$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/protobuf/lib:$LD_LIBRARY_PATH
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

