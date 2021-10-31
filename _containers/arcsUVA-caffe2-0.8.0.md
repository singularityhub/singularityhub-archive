---
id: 6820
name: "arcsUVA/caffe2"
branch: "master"
tag: "0.8.0"
commit: "70bc20429f0f8972703f468739d1d19a92f11971"
version: "df247ba68f248cae3c535d508b5d85dd"
build_date: "2019-02-24T08:38:39.899Z"
size_mb: 6801
size: 3156656159
sif: "https://datasets.datalad.org/shub/arcsUVA/caffe2/0.8.0/2019-02-24-70bc2042-df247ba6/df247ba68f248cae3c535d508b5d85dd.simg"
url: https://datasets.datalad.org/shub/arcsUVA/caffe2/0.8.0/2019-02-24-70bc2042-df247ba6/
recipe: https://datasets.datalad.org/shub/arcsUVA/caffe2/0.8.0/2019-02-24-70bc2042-df247ba6/Singularity
collection: arcsUVA/caffe2
---

# arcsUVA/caffe2:0.8.0

```bash
$ singularity pull shub://arcsUVA/caffe2:0.8.0
```

## Singularity Recipe

```singularity
BootStrap: shub
From: arcsUVA/anaconda:cuda9.0-cudnn7.4-py3.6


%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    apt-get -y update --fix-missing

    # install cuDNN and accessories
    apt-get install -y --no-install-recommends \
        build-essential \
        build-essential \
        git \
        libgoogle-glog-dev \
        libgtest-dev \
        libiomp-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopenmpi-dev \
        libsnappy-dev \
        libprotobuf-dev \
        openmpi-bin \
        openmpi-doc \
        protobuf-compiler \
        libgflags-dev

    # install other tools and dependencies
    apt-get -y install --allow-downgrades --no-install-recommends \
        dbus \
        wget \
        git \
        mercurial \
        subversion \
        vim \
        nano \
        cmake \
        bzip2 \
        ca-certificates \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1 \
        libboost-all-dev

    apt-get clean
    rm -rf /var/lib/apt/lists/*

    rm /etc/machine-id
    dbus-uuidgen --ensure=/etc/machine-id

    export CUDA_HOME="/usr/local/cuda"
    export CPATH="$CUDA_HOME/include:$CPATH"
    export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH"
    export PATH="$CUDA_HOME/bin:$PATH"

    export PATH="/opt/conda/bin:$PATH"
    unset CONDA_DEFAULT_ENV
    export ANACONDA_HOME=/opt/conda

    # conda update conda
    conda list
    pip install --upgrade \
        pip \
        future \
        protobuf \
        numpy \
        typing \
        hypothesis \
        pydot \
        opencv-python

    # install pytorch
    conda install pytorch=1.0 cudatoolkit=9.0 torchvision -c pytorch

    conda clean --index-cache --tarballs --packages --yes

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
exec python $@

%help
This container is backed by Anaconda version 5.2.0 and provides the Python 3.6 bindings for:
    * PyTorch 1.0
    * Caffe2
    * OpenCV
    * CUDA 9.0
    * CuDNN 7.4

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
```

## Collection

 - Name: [arcsUVA/caffe2](https://github.com/arcsUVA/caffe2)
 - License: None

