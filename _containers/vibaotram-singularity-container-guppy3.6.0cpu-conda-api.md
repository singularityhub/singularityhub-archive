---
id: 14730
name: "vibaotram/singularity-container"
branch: "master"
tag: "guppy3.6.0cpu-conda-api"
commit: "d93b4306ee881618baee43dfce1520f63407a302"
version: "dc69aa89e6ad9ba0a3ddb7310164345969ada2115239ef1fa2de88502a211a36"
build_date: "2021-03-25T04:16:50.211Z"
size_mb: 2647.8828125
size: 2776506368
sif: "https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy3.6.0cpu-conda-api/2021-03-25-d93b4306-dc69aa89/dc69aa89e6ad9ba0a3ddb7310164345969ada2115239ef1fa2de88502a211a36.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vibaotram/singularity-container/guppy3.6.0cpu-conda-api/2021-03-25-d93b4306-dc69aa89/
recipe: https://datasets.datalad.org/shub/vibaotram/singularity-container/guppy3.6.0cpu-conda-api/2021-03-25-d93b4306-dc69aa89/Singularity
collection: vibaotram/singularity-container
---

# vibaotram/singularity-container:guppy3.6.0cpu-conda-api

```bash
$ singularity pull shub://vibaotram/singularity-container:guppy3.6.0cpu-conda-api
```

## Singularity Recipe

```singularity
Bootstrap: docker
#From: tensorflow/tensorflow:1.13.1-py3
From: nvidia/cuda:10.2-cudnn7-devel-ubuntu16.04

# Using an image based on Ubuntu 16.04 (required for Guppy to install...)

%labels
MAINTAINER vibaotram

%help
  A container to hold the nanopore barcode demultiplexer guppy cpu version and Miniconda3.

%post
    echo 'export LC_ALL=C.UTF-8' >> /environment
    echo 'export LANG=C.UTF-8' >> /environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    apt update
    apt install -y git wget rsync tzdata dpkg python3-pip zlib1g-dev

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

    # activate conda
    #eval "$(/opt/conda/bin/conda shell.bash hook)"
    # configuring channels
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge


#### GUPPY CPU
    GUPPY_VERSION=3.6.0
    apt update && \
    apt-get install --yes apt-transport-https && \
    cd /tmp && \
    wget -q https://mirror.oxfordnanoportal.com/software/analysis/ont_guppy_cpu_${GUPPY_VERSION}-1~xenial_amd64.deb && \
    apt-get install --yes libzmq5 libhdf5-cpp-11 \
                          libcurl4-openssl-dev libssl-dev libhdf5-10 \
                          libboost-regex1.58.0 libboost-log1.58.0 \
                          libboost-atomic1.58.0 libboost-chrono1.58.0 \
                          libboost-date-time1.58.0 libboost-filesystem1.58.0 \
                          libboost-program-options1.58.0 libboost-iostreams1.58.0 && \
    dpkg -i *.deb && \
    rm *.deb && \
    apt-get autoremove --purge --yes && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


#### GUPPY CPU ONT_FAST5_API
    # pip3 install git+https://github.com/nanoporetech/ont_fast5_api
    pip install ont-fast5-api==3.1.3


%environment
  export PATH="/opt/conda/bin:$PATH"
```

## Collection

 - Name: [vibaotram/singularity-container](https://github.com/vibaotram/singularity-container)
 - License: None

