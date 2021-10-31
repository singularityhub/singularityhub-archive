---
id: 15513
name: "timothyas/data-driven-collab"
branch: "master"
tag: "hera"
commit: "9ba52434df7cdda346805ba81757ca873ee44896"
version: "0c98ab294fd3ea79a36b4754dfc13b72"
build_date: "2021-02-11T03:31:54.277Z"
size_mb: 5649.0
size: 3151859743
sif: "https://datasets.datalad.org/shub/timothyas/data-driven-collab/hera/2021-02-11-9ba52434-0c98ab29/0c98ab294fd3ea79a36b4754dfc13b72.sif"
url: https://datasets.datalad.org/shub/timothyas/data-driven-collab/hera/2021-02-11-9ba52434-0c98ab29/
recipe: https://datasets.datalad.org/shub/timothyas/data-driven-collab/hera/2021-02-11-9ba52434-0c98ab29/Singularity
collection: timothyas/data-driven-collab
---

# timothyas/data-driven-collab:hera

```bash
$ singularity pull shub://timothyas/data-driven-collab:hera
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvcr.io/nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%environment
    # these two are not critical on Hera, oh well
    export CUDA_HOME=/apps/cuda/cuda-10.1
    export XLA_FLAGS=--xla_gpu_cuda_data_dir=/apps/cuda/cuda-10.1

%post
    # Install some basics
    apt-get update -y --fix-missing
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        gnupg \
        wget \
        bzip2 \
        curl \
        git \
        python3.8 \
        python3-pip \
        python3-setuptools \
        python3-dev \
        python3-venv \
        python3-wheel

    # Cleanup
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    # NVIDIA Nsight Systems 2020.3.2
    # this is the version that was on the NVIDIA machine
    wget -qO - https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub | apt-key add -
    echo "deb https://developer.download.nvidia.com/devtools/repo-deb/x86_64/ /" >> /etc/apt/sources.list.d/nsight.list
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        nsight-systems-2020.3.2
    rm -rf /var/lib/apt/lists/*

    # Install all packages via pip
    python3.8 -m pip install --upgrade pip 
    python3.8 -m pip install --upgrade setuptools
    python3.8 -m pip install --upgrade numpy scipy coverage xarray dask future numba
    python3.8 -m pip install --upgrade matplotlib seaborn

    python3.8 -m pip install --upgrade networkx scikit-learn
    python3.8 -m pip install --upgrade cupy-cuda101
    python3.8 -m pip install --upgrade jax jaxlib==0.1.59+cuda101 -f https://storage.googleapis.com/jax-releases/jax_releases.html

    # soft link python -> python3
    ln -s /usr/bin/python3.8 /usr/bin/python
```

## Collection

 - Name: [timothyas/data-driven-collab](https://github.com/timothyas/data-driven-collab)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

