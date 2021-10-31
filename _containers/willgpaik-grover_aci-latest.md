---
id: 12353
name: "willgpaik/grover_aci"
branch: "master"
tag: "latest"
commit: "1e5f7e96f9911719d6bee67b65202b1f55516e84"
version: "e3bd6752bca578bf0642516af5e81fa4"
build_date: "2020-02-26T23:48:36.994Z"
size_mb: 5917.0
size: 2913820703
sif: "https://datasets.datalad.org/shub/willgpaik/grover_aci/latest/2020-02-26-1e5f7e96-e3bd6752/e3bd6752bca578bf0642516af5e81fa4.sif"
url: https://datasets.datalad.org/shub/willgpaik/grover_aci/latest/2020-02-26-1e5f7e96-e3bd6752/
recipe: https://datasets.datalad.org/shub/willgpaik/grover_aci/latest/2020-02-26-1e5f7e96-e3bd6752/Singularity
collection: willgpaik/grover_aci
---

# willgpaik/grover_aci:latest

```bash
$ singularity pull shub://willgpaik/grover_aci:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

%environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export PATH=/opt/conda/bin:/usr/local/nvidia/bin/:$PATH
    export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    export NVIDIA_VISIBLE_DEVICES=all
    export NVIDIA_DRIVER_CAPABILITIES=compute,utility
    export PYTHONPATH=/grover

%post
    apt-get update && apt-get install -y --no-install-recommends \
            build-essential \
            cmake \
            git \
            curl \
            vim \
            ca-certificates \
            libjpeg-dev \
            libpng-dev \
            wget &&\
            rm -rf /var/lib/apt/lists/*

    curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh  && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda install -y python=3.6 tqdm numpy pyyaml scipy ipython mkl mkl-include cython typing h5py pandas && \
    /opt/conda/bin/conda clean -ya && /opt/conda/bin/pip install tensorflow-gpu==1.13.1

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export PATH=/opt/conda/bin:/usr/local/nvidia/bin/:$PATH
    export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    export NVIDIA_VISIBLE_DEVICES=all
    export NVIDIA_DRIVER_CAPABILITIES=compute,utility
    
    mkdir -p grover
    cd /grover

    wget https://raw.githubusercontent.com/rowanz/grover/master/requirements-gpu.txt
    pip install -r requirements-gpu.txt

    export PYTHONPATH=/grover
```

## Collection

 - Name: [willgpaik/grover_aci](https://github.com/willgpaik/grover_aci)
 - License: None

