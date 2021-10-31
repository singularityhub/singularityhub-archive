---
id: 13915
name: "vibaotram/singularity-container"
branch: "master"
tag: "guppy4.0.14gpu-conda-api"
commit: "ef4fe0f9b910fd28b0c499bfa5e3e32cdaee34c9"
version: "e1b6605a6927c488d0023f40cd418bc58bf5d0e14732601a3c34e8463e8c8f57"
build_date: "2021-04-01T10:59:47.265Z"
size_mb: 2149.01953125
size: 2253410304
sif: "https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy4.0.14gpu-conda-api/2021-04-01-ef4fe0f9-e1b6605a/e1b6605a6927c488d0023f40cd418bc58bf5d0e14732601a3c34e8463e8c8f57.sif"
url: https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy4.0.14gpu-conda-api/2021-04-01-ef4fe0f9-e1b6605a/
recipe: https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy4.0.14gpu-conda-api/2021-04-01-ef4fe0f9-e1b6605a/Singularity
collection: vibaotram/singularity-container
---

# vibaotram/singularity-container:guppy4.0.14gpu-conda-api

```bash
$ singularity pull shub://vibaotram/singularity-container:guppy4.0.14gpu-conda-api
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.13.1-gpu-py3
#From: nvidia/cuda:10.2-cudnn7-devel-ubuntu16.04

# Using an image based on Ubuntu 16.04 (required for Guppy to install...)

%post
    echo 'export LC_ALL=C.UTF-8' >> /environment
    echo 'export LANG=C.UTF-8' >> /environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    apt update
    apt install -y git wget rsync zlib1g-dev dpkg python3-pip tzdata

#### Miniconda
    # install miniconda
    if [ ! -d /opt/conda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh -O ~/miniconda.sh && \
         bash ~/miniconda.sh -b -p /opt/conda && \
         rm ~/miniconda.sh && \
         /opt/conda/bin/conda clean -tipsy && \
         ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
         echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
         echo "conda activate base" >> ~/.bashrc
    fi
    # set miniconda path
    export PATH="/opt/conda/bin:$PATH"

    # update conda
    conda update -n base -c defaults conda
    # activate conda
    #eval "$(/opt/conda/bin/conda shell.bash hook)"
    # configuring channels
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge


#### GUPPY GPU
    GUPPY_VERSION=4.0.14
      apt-get update && \
      apt-get install --yes \
        apt-transport-https \
        libcurl4-openssl-dev \
        libssl-dev \
        libhdf5-cpp-11 \
        libzmq5 \
        libboost-atomic1.58.0 \
        libboost-chrono1.58.0 \
        libboost-date-time1.58.0 \
        libboost-filesystem1.58.0 \
        libboost-program-options1.58.0 \
        libboost-regex1.58.0 \
        libboost-system1.58.0 \
        libboost-log1.58.0 \
        libboost-iostreams1.58.0 \
        wget && \
        cd /tmp &&\
        wget -q https://mirror.oxfordnanoportal.com/software/analysis/ont_guppy_${GUPPY_VERSION}-1~xenial_amd64.deb && \
        dpkg -i --ignore-depends=nvidia-384,libcuda1-384 /tmp/ont_guppy_${GUPPY_VERSION}-1~xenial_amd64.deb && \
        rm *.deb && \
        apt-get autoremove --purge --yes && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*


#### INSTALL ONT_FAST5_API
    pip install ont-fast5-api==3.1.3

%environment
  export PATH="/opt/conda/bin:$PATH"
```

## Collection

 - Name: [vibaotram/singularity-container](https://github.com/vibaotram/singularity-container)
 - License: None

