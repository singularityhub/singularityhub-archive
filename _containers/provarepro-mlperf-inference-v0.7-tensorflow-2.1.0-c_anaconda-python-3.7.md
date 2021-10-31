---
id: 14704
name: "provarepro/mlperf-inference"
branch: "v0.7"
tag: "v0.7-tensorflow-2.1.0-c_anaconda-python-3.7"
commit: "a7017d003c374684b99a18a823776ccad7263a56"
version: "137affba7cdb91d6431d5bf74551e4444fc8c42a85ea72987e71f6921918cf43"
build_date: "2020-10-26T20:56:15.110Z"
size_mb: 1685.921875
size: 1767817216
sif: "https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-c_anaconda-python-3.7/2020-10-26-a7017d00-137affba/137affba7cdb91d6431d5bf74551e4444fc8c42a85ea72987e71f6921918cf43.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-c_anaconda-python-3.7/2020-10-26-a7017d00-137affba/
recipe: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-tensorflow-2.1.0-c_anaconda-python-3.7/2020-10-26-a7017d00-137affba/Singularity
collection: provarepro/mlperf-inference
---

# provarepro/mlperf-inference:v0.7-tensorflow-2.1.0-c_anaconda-python-3.7

```bash
$ singularity pull shub://provarepro/mlperf-inference:v0.7-tensorflow-2.1.0-c_anaconda-python-3.7
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: fenz-org/tensorflow:2.1.0-c_anaconda-python-3.7

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

