---
id: 14278
name: "eugtsa/base_singularity"
branch: "master"
tag: "latest"
commit: "bdd6174b68bcc109241049cdbded4b9d0563a2bf"
version: "40e9af8f3c3df154fb4706a360bde5e64f7b9eb41bab3852a818de23c0828c60"
build_date: "2021-02-26T14:52:37.491Z"
size_mb: 4479.62109375
size: 4697223168
sif: "https://datasets.datalad.org/shub/eugtsa/base_singularity/latest/2021-02-26-bdd6174b-40e9af8f/40e9af8f3c3df154fb4706a360bde5e64f7b9eb41bab3852a818de23c0828c60.sif"
url: https://datasets.datalad.org/shub/eugtsa/base_singularity/latest/2021-02-26-bdd6174b-40e9af8f/
recipe: https://datasets.datalad.org/shub/eugtsa/base_singularity/latest/2021-02-26-bdd6174b-40e9af8f/Singularity
collection: eugtsa/base_singularity
---

# eugtsa/base_singularity:latest

```bash
$ singularity pull shub://eugtsa/base_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:latest

%help

    Container with packages on top of base 3.6 with anaconda

%files
  ./requirements.txt /requirements.txt

%post
  
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    build-essential \
    wget \
    tmux \
    tree \
    vim \
    git \
    zip \
    unzip \
    graphviz \
    libsndfile1 \
    libasound2 \
    curl \
    ca-certificates \
    apt-utils \
    postgresql-server.dev

  rm -rf /var/lib/apt/lists/*
  apt-get clean

  wget -c https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    /bin/bash Anaconda3-2019.03-Linux-x86_64.sh -bfp /usr/local

  #Conda configuration of channels from .condarc file

  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels pytorch
  conda config --add channels menpo
  conda update conda
  pip install --upgrade pip
  rm -rf /usr/local/lib/python3/site-packages/llvmlite*
  
  #Install environment
  rm -rf ~/anaconda3/lib/python3.6/site-packages/llvmlite*
  pip install -I -r requirements.txt
  pip uninstall matplotlib -y
  conda install nodejs pyqt
  conda install matplotlib --force-reinstall
#  jupyter labextension install @jupyter-widgets/jupyterlab-manager
#  conda install xeus-python -c conda-forge
#  jupyter labextension install @jupyterlab/debugger
```

## Collection

 - Name: [eugtsa/base_singularity](https://github.com/eugtsa/base_singularity)
 - License: None

