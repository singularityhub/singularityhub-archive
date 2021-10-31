---
id: 14714
name: "provarepro/mlperf-inference"
branch: "v0.7"
tag: "v0.7-tensorflow-2.1.0-c_intel-python-3.7"
commit: "e3c18f675a7aa2cc48063e789821bc832c145610"
version: "f46a7fbf913496f5cdb2d74bb58465c8712b82034ae16949d72ffb2141e7bc4e"
build_date: "2020-10-31T15:23:06.896Z"
size_mb: 2174.3984375
size: 2280022016
sif: "https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-c_intel-python-3.7/2020-10-31-e3c18f67-f46a7fbf/f46a7fbf913496f5cdb2d74bb58465c8712b82034ae16949d72ffb2141e7bc4e.sif"
url: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-c_intel-python-3.7/2020-10-31-e3c18f67-f46a7fbf/
recipe: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-c_intel-python-3.7/2020-10-31-e3c18f67-f46a7fbf/Singularity
collection: provarepro/mlperf-inference
---

# provarepro/mlperf-inference:v0.7-tensorflow-2.1.0-c_intel-python-3.7

```bash
$ singularity pull shub://provarepro/mlperf-inference:v0.7-tensorflow-2.1.0-c_intel-python-3.7
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: fenz-org/tensorflow:2.1.0-c_intel-python-3.7

%post
    export PATH="/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    
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

