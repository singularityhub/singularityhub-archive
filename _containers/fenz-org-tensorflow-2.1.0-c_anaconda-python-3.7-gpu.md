---
id: 14777
name: "fenz-org/tensorflow"
branch: "master"
tag: "2.1.0-c_anaconda-python-3.7-gpu"
commit: "ff28cd209dcfc12f68bc0eead076db1c799ea0fb"
version: "49ba0ebb43136d11b0bbdf7b5bf34fee3499d7b1efcb1665573825e45747a37a"
build_date: "2020-10-31T14:48:26.206Z"
size_mb: 5010.8515625
size: 5254258688
sif: "https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-c_anaconda-python-3.7-gpu/2020-10-31-ff28cd20-49ba0ebb/49ba0ebb43136d11b0bbdf7b5bf34fee3499d7b1efcb1665573825e45747a37a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fenz-org/tensorflow/2.1.0-c_anaconda-python-3.7-gpu/2020-10-31-ff28cd20-49ba0ebb/
recipe: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-c_anaconda-python-3.7-gpu/2020-10-31-ff28cd20-49ba0ebb/Singularity
collection: fenz-org/tensorflow
---

# fenz-org/tensorflow:2.1.0-c_anaconda-python-3.7-gpu

```bash
$ singularity pull shub://fenz-org/tensorflow:2.1.0-c_anaconda-python-3.7-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    export CUDNN_VERSION=7.6.5.32
    export CUDA_PKG_VERSION=10-1=10.1.243-1
    export CUDA_VERSION=10.1.243
    export NCCL_VERSION=2.7.8
    export NVIDIA_REQUIRE_CUDA="cuda>=10.1 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419"
    export LIBRARY_PATH=/usr/local/cuda/lib64/stubs
    export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    export NVIDIA_DRIVER_CAPABILITIES=compute,utility
    export PATH=/opt/conda/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export DEBIAN_FRONTEND=noninteractive
    export PYTHON_VERSION=3.7
    export PY_VER=py37
    export CONDA_VERSION=4.8.2
    export CONDA_CNL=anaconda
    export CONDA_PROFILE=base

    apt-get update --fix-missing

    apt-get install -y --no-install-recommends \
        wget \
        bzip2 \
        ca-certificates \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1 \
        git \
        mercurial \
        subversion

    apt-get clean

    wget --quiet \
        https://repo.anaconda.com/miniconda/Miniconda3-${PY_VER}_${CONDA_VERSION}-Linux-x86_64.sh -O ~/miniconda.sh
    /bin/bash ~/miniconda.sh -b -p /opt/conda
    rm ~/miniconda.sh
    /opt/conda/bin/conda clean -tipsy
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate $CONDA_PROFILE" >> ~/.bashrc
    echo "conda ${CONDA_VERSION}" >> /opt/conda/conda-meta/pinned
    conda config --system --prepend channels ${CONDA_CNL}
    conda config --system --set auto_update_conda false
    conda config --system --set show_channel_urls true
    find /opt/conda/ -follow -type f -name '*.a' -delete
    find /opt/conda/ -follow -type f -name '*.js.map' -delete
    /opt/conda/bin/conda clean -afy

    export TENSORFLOW_VERSION=2.1.0
    export USE_DAAL4PY_SKLEARN=YES

    conda install -y -c ${CONDA_CNL} \
        cudatoolkit=${CUDA_VERSION} \
        cudnn=7.6.5 \
        tensorflow-gpu=${TENSORFLOW_VERSION}

%environment
    export CUDNN_VERSION=7.6.5.32
    export CUDA_PKG_VERSION=10-1=10.1.243-1
    export CUDA_VERSION=10.1.243
    export NCCL_VERSION=2.7.8
    export NVIDIA_REQUIRE_CUDA="cuda>=10.1 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419"
    export LIBRARY_PATH=/usr/local/cuda/lib64/stubs
    export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    export NVIDIA_DRIVER_CAPABILITIES=compute,utility
    export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    export PYTHON_VERSION=3.7.7
    export CONDA_EXE=/opt/conda/bin/conda
    export CONDA_PREFIX=/opt/conda
    export CONDA_PYTHON_EXE=/opt/conda/bin/python
    export USE_DAAL4PY_SKLEARN=YES
    export CONDA_PROFILE=base
    . /opt/conda/etc/profile.d/conda.sh
    conda activate $CONDA_PROFILE
```

## Collection

 - Name: [fenz-org/tensorflow](https://github.com/fenz-org/tensorflow)
 - License: None

