---
id: 10839
name: "AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN"
branch: "master"
tag: "latest"
commit: "3ab1354e49a56aa188fd99562b6775c4998efcc6"
version: "86abef07927f39ac39920891d2a80bc0"
build_date: "2019-10-17T06:37:21.795Z"
size_mb: 6561.0
size: 3183738911
sif: "https://datasets.datalad.org/shub/AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN/latest/2019-10-17-3ab1354e-86abef07/86abef07927f39ac39920891d2a80bc0.sif"
url: https://datasets.datalad.org/shub/AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN/latest/2019-10-17-3ab1354e-86abef07/
recipe: https://datasets.datalad.org/shub/AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN/latest/2019-10-17-3ab1354e-86abef07/Singularity
collection: AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN
---

# AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN:latest

```bash
$ singularity pull shub://AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04
 

%environment
    SHELL=/bin/bash

    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
    unset CONDA_DEFAULT_ENV
    export ANACONDA_HOME=/opt/conda
    export CONDA_PREFIX='/opt/conda'
    export CONDA_SHLVL='1'
    export CONDA_DEFAULT_ENV='base'
    export CONDA_PROMPT_MODIFIER='(base) '
    export CONDA_EXE='/opt/conda/bin/conda'

    . /opt/conda/etc/profile.d/conda.sh
    conda activate thesis

%runscript


%post
    mkdir /thesis-singularity
    mkdir /project /scratch
    touch /usr/bin/nvidia-smi

    apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
    apt-get clean

    cd /thesis-singularity
    apt-get install -y libopenslide-dev openslide-tools
    wget https://github.com/computationalpathologygroup/ASAP/releases/download/1.9/ASAP-1.9-Linux-Ubuntu1604.deb
    apt-get install /thesis-singularity/ASAP-1.9-Linux-Ubuntu1604.deb -y

    wget  https://repo.anaconda.com/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh -O /thesis-singularity/miniconda.sh && \
    /bin/bash /thesis-singularity/miniconda.sh -b -p /opt/conda && \
    rm /thesis-singularity/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> /thesis-singularity/.bashrc && \
    echo "conda activate base" >> /thesis-singularity/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

   

    export PATH=/opt/conda/bin:/opt/conda/condabin:$PATH
    /opt/conda/bin/conda create -n thesis python=3.6 cudatoolkit=10.0.130 tensorflow-gpu numpy scipy scikit-learn opencv conda-build matplotlib pip
    
    conda init
    
    . activate
    conda activate thesis
    /opt/conda/bin/conda develop /opt/ASAP/bin
    pip install -q git+https://github.com/tensorflow/examples.git
```

## Collection

 - Name: [AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN](https://github.com/AlistairSymonds/Breast-Cancer-WSI-Histopathology-NN)
 - License: None

