---
id: 11268
name: "igfuw/UWLCM"
branch: "master"
tag: "latest"
commit: "a27303e98442362059fcaa33d2852e5399e5e578"
version: "d4ed2a10d6c7e4a0432fe8ea7e75e92a719d09502b522e5ca02a9676fed777d3"
build_date: "2019-11-26T10:51:27.550Z"
size_mb: 1522.171875
size: 1596112896
sif: "https://datasets.datalad.org/shub/igfuw/UWLCM/latest/2019-11-26-a27303e9-d4ed2a10/d4ed2a10d6c7e4a0432fe8ea7e75e92a719d09502b522e5ca02a9676fed777d3.sif"
url: https://datasets.datalad.org/shub/igfuw/UWLCM/latest/2019-11-26-a27303e9-d4ed2a10/
recipe: https://datasets.datalad.org/shub/igfuw/UWLCM/latest/2019-11-26-a27303e9-d4ed2a10/Singularity
collection: igfuw/UWLCM
---

# igfuw/UWLCM:latest

```bash
$ singularity pull shub://igfuw/UWLCM:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-devel-ubuntu18.04

%post
export DEBIAN_FRONTEND=noninteractive
export  TZ=America/Los_Angeles
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt-get update -qq \
    && apt-get install -yq --no-install-recommends \
        sudo \
        apt-utils \
        build-essential \
        pkg-config \
        git \
        ca-certificates \
        software-properties-common \
        vim \
        curl \
        language-pack-en-base

add-apt-repository ppa:ubuntu-toolchain-r/test
apt-get update

add-apt-repository ppa:ubuntu-toolchain-r/test
apt-get update -qq \
    && apt-get install -yq --no-install-recommends \
        wget \
        gnuplot-nox \
        libgnuplot-iostream-dev \
        libhdf5-dev \
        hdf5-tools \
        python-dev \
        python-h5py \
        python-numpy \
        python-scipy \
        python-matplotlib \
        python-pytest \
        libthrust-dev \
        libboost-all-dev

wget https://github.com/Kitware/CMake/releases/download/v3.13.2/cmake-3.13.2-Linux-x86_64.sh
sudo sh cmake-3.13.2-Linux-x86_64.sh --prefix=/usr/local --exclude-subdir

git clone --depth=1 git://github.com/thrust/thrust.git
sudo ln -s `pwd`/thrust/thrust /usr/local/include/thrust

git clone --depth=1 git://github.com/blitzpp/blitz.git
cd blitz
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make
sudo make install
cd ../../
```

## Collection

 - Name: [igfuw/UWLCM](https://github.com/igfuw/UWLCM)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

