---
id: 11823
name: "vmichals/simpaux"
branch: "master"
tag: "latest"
commit: "9cbf8147516282b5041340fc1005728643d9763f"
version: "032accfdc68f3ec09c843892280af17e"
build_date: "2021-03-11T16:40:02.394Z"
size_mb: 5032.0
size: 2234044447
sif: "https://datasets.datalad.org/shub/vmichals/simpaux/latest/2021-03-11-9cbf8147-032accfd/032accfdc68f3ec09c843892280af17e.sif"
url: https://datasets.datalad.org/shub/vmichals/simpaux/latest/2021-03-11-9cbf8147-032accfd/
recipe: https://datasets.datalad.org/shub/vmichals/simpaux/latest/2021-03-11-9cbf8147-032accfd/Singularity
collection: vmichals/simpaux
---

# vmichals/simpaux:latest

```bash
$ singularity pull shub://vmichals/simpaux:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: pytorch/pytorch:1.2-cuda10.0-cudnn7-runtime

%post
    apt -y update
    apt -y upgrade
    apt -y install software-properties-common
    apt -y install vim unzip wget sudo
    apt -y install build-essential libssl-dev libffi-dev
    apt -y install libsm6
    apt -y install git

    # clean apt cache
    apt clean
    rm -rf /var/lib/apt/lists/*

    # set conda path
    export PATH="/opt/conda/bin:$PATH"

    conda install numpy scipy opencv matplotlib scikit-learn scikit-image \
    pandas tqdm imageio pytables h5py gitpython tensorboard
    conda install -c conda-forge ipdb
    pip install --no-cache-dir torchmeta future
    pip install --no-cache-dir git+https://github.com/epistimio/orion.git@develop

    # clean conda cache
    conda clean --all -y

%environment
    export PATH=/opt/conda/bin:$PATH

    # This works around a problem in ipdb
    export LC_ALL=C.UTF-8

%runscript
```

## Collection

 - Name: [vmichals/simpaux](https://github.com/vmichals/simpaux)
 - License: None

