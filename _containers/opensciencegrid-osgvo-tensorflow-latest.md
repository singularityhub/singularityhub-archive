---
id: 413
name: "opensciencegrid/osgvo-tensorflow"
branch: "master"
tag: "latest"
commit: "2bf9c39ae79d855667a48906f79203362d51d04b"
version: "db46c50ae6b356ed46a7aa4b7612fe87"
build_date: "2021-04-19T07:34:10.942Z"
size_mb: 3287
size: 1072812063
sif: "https://datasets.datalad.org/shub/opensciencegrid/osgvo-tensorflow/latest/2021-04-19-2bf9c39a-db46c50a/db46c50ae6b356ed46a7aa4b7612fe87.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/opensciencegrid/osgvo-tensorflow/latest/2021-04-19-2bf9c39a-db46c50a/
recipe: https://datasets.datalad.org/shub/opensciencegrid/osgvo-tensorflow/latest/2021-04-19-2bf9c39a-db46c50a/Singularity
collection: opensciencegrid/osgvo-tensorflow
---

# opensciencegrid/osgvo-tensorflow:latest

```bash
$ singularity pull shub://opensciencegrid/osgvo-tensorflow:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ubuntu:16.04

%post

# to find pip
export PATH=/usr/local/bin:/usr/local/sbin:/bin:/usr/bin:/usr/sbin:/bin:/sbin

apt-get update && apt-get upgrade -y --allow-unauthenticated

export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --allow-unauthenticated \
        build-essential \
        cmake \
        curl \
        git \
        libfreetype6-dev \
        libpng12-dev \
        libssl-dev \
        libzmq3-dev \
        module-init-tools \
        pkg-config \
        python \
        python-dev \
        python-tk \
        python3 \
        python3-dev \
        python3-tk \
        rsync \
        software-properties-common \
        unzip \
        zip \
        zlib1g-dev \
        openjdk-8-jdk \
        openjdk-8-jre-headless \
        vim \
        wget \
        libxpm-dev

apt-get clean 
rm -rf /var/lib/apt/lists/*

# bazel is required for some TensorFlow projects
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" >/etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | apt-key add -

export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated \
        bazel

curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

pip --no-cache-dir install \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        Pillow \
        scipy \
        sklearn

python -m ipykernel.kernelspec

# Install TensorFlow
pip uninstall tensorflow || true
pip install --upgrade tensorflow==1.4

# keras
pip install --upgrade keras


#############################
# now do the same for python3

curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

pip3 --no-cache-dir install \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        Pillow \
        scipy \
        sklearn

python3 -m ipykernel.kernelspec

# Install TensorFlow
pip3 uninstall tensorflow || true
pip3 install --upgrade tensorflow==1.4

# keras
pip3 install --upgrade keras

# required directories
mkdir -p /cvmfs

# root
cd /opt && \
    wget -nv https://root.cern.ch/download/root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \
    tar xzf root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \
    rm -f root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz

# xrootd
cd /opt && \
    wget http://xrootd.org/download/v4.7.1/xrootd-4.7.1.tar.gz && \
    tar xzf xrootd-4.7.1.tar.gz && \
    cd xrootd-4.7.1 && \
    mkdir build && \
    cd  build && \
    cmake /opt/xrootd-4.7.1 -DCMAKE_INSTALL_PREFIX=/opt/xrootd -DENABLE_PERL=FALSE && \
    make && \
    make install && \
    cd /opt && \
    rm -rf xrootd-4.7.1.tar.gz xrootd-4.7.1

# stashcp
cd /opt && \
    git clone https://github.com/opensciencegrid/StashCache.git

# build info
echo "Timestamp:" `date --utc` | tee /image-build-info.txt
```

## Collection

 - Name: [opensciencegrid/osgvo-tensorflow](https://github.com/opensciencegrid/osgvo-tensorflow)
 - License: None

