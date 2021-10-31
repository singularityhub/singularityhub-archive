---
id: 14731
name: "vibaotram/singularity-container"
branch: "master"
tag: "guppy3.6.0gpu-conda-api"
commit: "d93b4306ee881618baee43dfce1520f63407a302"
version: "79a2db0e0e5c7ef7422dc8f34a387d1f5529cce09255931f1e2bdd4201a8c8b8"
build_date: "2020-10-27T05:26:31.402Z"
size_mb: 2147.91796875
size: 2252255232
sif: "https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy3.6.0gpu-conda-api/2020-10-27-d93b4306-79a2db0e/79a2db0e0e5c7ef7422dc8f34a387d1f5529cce09255931f1e2bdd4201a8c8b8.sif"
url: https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy3.6.0gpu-conda-api/2020-10-27-d93b4306-79a2db0e/
recipe: https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy3.6.0gpu-conda-api/2020-10-27-d93b4306-79a2db0e/Singularity
collection: vibaotram/singularity-container
---

# vibaotram/singularity-container:guppy3.6.0gpu-conda-api

```bash
$ singularity pull shub://vibaotram/singularity-container:guppy3.6.0gpu-conda-api
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
    GUPPY_VERSION=3.6.0
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

