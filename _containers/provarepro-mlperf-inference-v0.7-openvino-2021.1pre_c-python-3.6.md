---
id: 15868
name: "provarepro/mlperf-inference"
branch: "v0.7"
tag: "v0.7-openvino-2021.1pre_c-python-3.6"
commit: "bbb0f2a097a4ed68f4fd636da6c4b4c10dfaab64"
version: "20a2566f5b0726f84cad30ec4e5751bac63d0f7b354bf613211d6a039d282e9d"
build_date: "2021-04-11T14:24:29.223Z"
size_mb: 1399.5625
size: 1467547648
sif: "https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-openvino-2021.1pre_c-python-3.6/2021-04-11-bbb0f2a0-20a2566f/20a2566f5b0726f84cad30ec4e5751bac63d0f7b354bf613211d6a039d282e9d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/provarepro/mlperf-inference/v0.7-openvino-2021.1pre_c-python-3.6/2021-04-11-bbb0f2a0-20a2566f/
recipe: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-openvino-2021.1pre_c-python-3.6/2021-04-11-bbb0f2a0-20a2566f/Singularity
collection: provarepro/mlperf-inference
---

# provarepro/mlperf-inference:v0.7-openvino-2021.1pre_c-python-3.6

```bash
$ singularity pull shub://provarepro/mlperf-inference:v0.7-openvino-2021.1pre_c-python-3.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: provarepro/openvino:2021.1pre_c-python-3.6

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LANGUAGE=C.UTF-8
    export PYTHON_VERSION="3.6"

    cd /
    git clone https://github.com/gflags/gflags.git
    cd gflags
    mkdir build && cd build
    cmake ..
    make

    cd /
    apt-get update
    apt-get install -y --no-install-recommends \
        libicu-dev \
        libbz2-dev \
        liblzma-dev
    rm -rf /var/lib/apt/lists/*

    export BOOST_VERSION="1.72.0"
    export _BOOST_VERSION="1_72_0"

    wget -q https://dl.bintray.com/boostorg/release/${BOOST_VERSION}/source/boost_${_BOOST_VERSION}.tar.gz
    tar xf boost_${_BOOST_VERSION}.tar.gz
    cd boost_${_BOOST_VERSION}
    ./bootstrap.sh --with-libraries=filesystem
    ./b2 --with-filesystem

    cd /
    python${PYTHON_VERSION} -m pip install \
    pybind11 absl-py
    git clone \
        --depth 1 \
        --single-branch \
        -b v0.7 \
        https://github.com/mlperf/inference.git /mlperf_inference
    cd /mlperf_inference
    mkdir loadgen/build
    cd loadgen/build
    cmake ..
    cmake --build .
    cp libmlperf_loadgen.a ..
    rm -r /mlperf_inference/loadgen/build
    cp -r /mlperf_inference/loadgen /mlperf_loadgen
    rm -rf /mlperf_inference

    export gflags_DIR=/gflags/build
    export InferenceEngine_DIR=/openvino/build

    cd /
    git clone https://github.com/mlperf/inference_results_v0.7.git
    mv inference_results_v0.7/closed/Intel/code/resnet/resnet-ov /mlperf_inference
    rm -rf inference_results_v0.7
    cd /mlperf_inference
    mkdir build && cd build
    cmake \
        -DLOADGEN_DIR=/mlperf_loadgen \
        -DBOOST_INCLUDE_DIRS=/boost_${_BOOST_VERSION} \
        -DBOOST_FILESYSTEM_LIB=/boost_${_BOOST_VERSION}/stage/lib/libboost_filesystem.so \
        -DCMAKE_BUILD_TYPE=Release \
        ..
    cmake --build . --config Release

%environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export LANGUAGE=C.UTF-8
    export LOADGEN_LIB_DIR=/mlperf_loadgen
    export PYTHON_VERSION="3.6"
```

## Collection

 - Name: [provarepro/mlperf-inference](https://github.com/provarepro/mlperf-inference)
 - License: None

