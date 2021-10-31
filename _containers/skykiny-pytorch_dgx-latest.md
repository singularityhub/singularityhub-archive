---
id: 15599
name: "skykiny/pytorch_dgx"
branch: "singularity"
tag: "latest"
commit: "b3221909212850edd62027d132f47775a863820c"
version: "503d6f30d696e142316c5438a5b414c5"
build_date: "2021-02-26T00:40:05.678Z"
size_mb: 6509.0
size: 3007098911
sif: "https://datasets.datalad.org/shub/skykiny/pytorch_dgx/latest/2021-02-26-b3221909-503d6f30/503d6f30d696e142316c5438a5b414c5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/skykiny/pytorch_dgx/latest/2021-02-26-b3221909-503d6f30/
recipe: https://datasets.datalad.org/shub/skykiny/pytorch_dgx/latest/2021-02-26-b3221909-503d6f30/Singularity
collection: skykiny/pytorch_dgx
---

# skykiny/pytorch_dgx:latest

```bash
$ singularity pull shub://skykiny/pytorch_dgx:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.2-cudnn7-runtime-ubuntu16.04

%environment
    export PATH="/opt/conda/bin":$PATH

%post
    apt-get update --fix-missing && apt upgrade -y && apt-get install -y \
        gcc g++ build-essential\
        curl wget \
        ca-certificates \
        sudo \
        git subversion \
        bzip2 \
        libx11-6 \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1 \
        mercurial \
        htop zsh vim zip \
        python3-openslide \
     && apt-get clean && rm -rf /var/lib/apt/lists/*
     
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh -O ~/anaconda.sh && \
        /bin/bash ~/anaconda.sh -b -p /opt/conda && \
        rm ~/anaconda.sh && \
        ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
        echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
        echo "conda activate base" >> ~/.bashrc && \
        find /opt/conda/ -follow -type f -name '*.a' -delete && \
        find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
        /opt/conda/bin/conda clean -afy
    . /opt/conda/etc/profile.d/conda.sh && \
        conda activate base
    conda install -y -c pytorch torchvision torchaudio cudatoolkit=9.2 cudnn \
        && conda clean -ya
    pip install openslide-python opencv-contrib-python pretrainedmodels kornia tensorboardX staintools spams gpustat

%runscript
	exec "$@"
```

## Collection

 - Name: [skykiny/pytorch_dgx](https://github.com/skykiny/pytorch_dgx)
 - License: None

