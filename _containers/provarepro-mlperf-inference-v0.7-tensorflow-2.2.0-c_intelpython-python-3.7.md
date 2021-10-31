---
id: 14727
name: "provarepro/mlperf-inference"
branch: "v0.7"
tag: "v0.7-tensorflow-2.2.0-c_intelpython-python-3.7"
commit: "e3c18f675a7aa2cc48063e789821bc832c145610"
version: "c4b0a0ccf3f0a3508cbcbbcb0cc799bc9e38aa5eae156b9773aa0d7de644471a"
build_date: "2020-10-27T20:34:12.884Z"
size_mb: 2858.52734375
size: 2997383168
sif: "https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.2.0-c_intelpython-python-3.7/2020-10-27-e3c18f67-c4b0a0cc/c4b0a0ccf3f0a3508cbcbbcb0cc799bc9e38aa5eae156b9773aa0d7de644471a.sif"
url: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.2.0-c_intelpython-python-3.7/2020-10-27-e3c18f67-c4b0a0cc/
recipe: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.2.0-c_intelpython-python-3.7/2020-10-27-e3c18f67-c4b0a0cc/Singularity
collection: provarepro/mlperf-inference
---

# provarepro/mlperf-inference:v0.7-tensorflow-2.2.0-c_intelpython-python-3.7

```bash
$ singularity pull shub://provarepro/mlperf-inference:v0.7-tensorflow-2.2.0-c_intelpython-python-3.7
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: fenz-org/tensorflow:2.2.0-c_intelpython-python-3.7

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

