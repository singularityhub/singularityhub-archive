---
id: 14792
name: "provarepro/mlperf-inference"
branch: "v0.7"
tag: "v0.7-tensorflow-2.1.0-p-python-3.7-gpu"
commit: "407e25092a203a4eff1a8daadd6fc0e022477da3"
version: "9b067d58fa12b67a89720332f7dec72e812f3b7715d8211b5daf5237fb9bb052"
build_date: "2020-10-31T10:10:57.414Z"
size_mb: 3410.12890625
size: 3575779328
sif: "https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-p-python-3.7-gpu/2020-10-31-407e2509-9b067d58/9b067d58fa12b67a89720332f7dec72e812f3b7715d8211b5daf5237fb9bb052.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-p-python-3.7-gpu/2020-10-31-407e2509-9b067d58/
recipe: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-p-python-3.7-gpu/2020-10-31-407e2509-9b067d58/Singularity
collection: provarepro/mlperf-inference
---

# provarepro/mlperf-inference:v0.7-tensorflow-2.1.0-p-python-3.7-gpu

```bash
$ singularity pull shub://provarepro/mlperf-inference:v0.7-tensorflow-2.1.0-p-python-3.7-gpu
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: fenz-org/tensorflow:2.1.0-p-python-3.7-gpu

%post
    
    apt-get update
    apt-get install -y --no-install-recommends \
        git \
        build-essential
#        libglib2.0-dev \
#        software-properties-common \
#        ca-certificates \
#        wget \
#        curl \
#        htop \
#        zip \
#        unzip 
#        && \
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    python -m pip install --ignore-installed \
        absl-py \
        numpy \
        certifi \
        opencv-python-headless \
        pycocotools \
        pybind11 \
        Cython

    export LOADER_VER=0.5a0

    git clone \
        --recurse-submodules \
        --depth 1 \
        --single-branch \
        -b v0.7 \
        https://github.com/mlperf/inference.git /mlperf_inference
    cd /mlperf_inference/loadgen
    CFLAGS="-std=c++14 -O3" python setup.py bdist_wheel
    python -m pip install --force-reinstall \
        dist/mlperf_loadgen-${LOADER_VER}-*.whl
    rm dist/mlperf_loadgen-${LOADER_VER}-*.whl
```

## Collection

 - Name: [provarepro/mlperf-inference](https://github.com/provarepro/mlperf-inference)
 - License: None

