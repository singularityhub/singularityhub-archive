---
id: 15886
name: "provarepro/mlperf-inference"
branch: "v0.7"
tag: "v0.7-openvino-2020.3.1-python3.6-gcc-7.5.0"
commit: "a2836460a6c3137570375ff9fdbe769470b903f7"
version: "38799012f787d93dab019d07a88ab42db78c340fb65ed78eb2ef5a1c2eb4d6f9"
build_date: "2021-04-13T08:01:21.407Z"
size_mb: 526.60546875
size: 552185856
sif: "https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-openvino-2020.3.1-python3.6-gcc-7.5.0/2021-04-13-a2836460-38799012/38799012f787d93dab019d07a88ab42db78c340fb65ed78eb2ef5a1c2eb4d6f9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/provarepro/mlperf-inference/v0.7-openvino-2020.3.1-python3.6-gcc-7.5.0/2021-04-13-a2836460-38799012/
recipe: https://datasets.datalad.org/shub/provarepro/mlperf-inference/v0.7-openvino-2020.3.1-python3.6-gcc-7.5.0/2021-04-13-a2836460-38799012/Singularity
collection: provarepro/mlperf-inference
---

# provarepro/mlperf-inference:v0.7-openvino-2020.3.1-python3.6-gcc-7.5.0

```bash
$ singularity pull shub://provarepro/mlperf-inference:v0.7-openvino-2020.3.1-python3.6-gcc-7.5.0
```

## Singularity Recipe

```singularity
# Dockerfile: https://raw.githubusercontent.com/openvinotoolkit/docker_ci/40b3b8226a61fc96ebe48d0f9f95f86cdc7deabb/dockerfiles/ubuntu18/openvino_cgvh_runtime_2020.dockerfile
Bootstrap: docker
From: openvino/ubuntu18_runtime:2020.3.1

%post
    export DEBIAN_FRONTEND=noninteractive

    DEPENDENCIES="build-essential \
                  git \
                  wget"

    apt-get update
    apt-get install -y --no-install-recommends \
        ${DEPENDENCIES}

    # Build MLPerf loadgen
    python3 -m pip install --no-cache-dir \
        cmake \
        pybind11 \
        absl-py

    TEMP_DIR=$(mktemp -d)
    cd ${TEMP_DIR}

    ## Install MLPerf loadgen (CPP)
    git clone \
        --depth 1 \
        --single-branch \
        -b v0.7 \
        https://github.com/mlperf/inference.git ${TEMP_DIR}/mlperf_inference
    cd ${TEMP_DIR}/mlperf_inference
    mkdir loadgen/build && cd loadgen/build
    cmake .. && cmake --build .
    cp libmlperf_loadgen.a ..
    rm -r ${TEMP_DIR}/mlperf_inference/loadgen/build
    cp -r ${TEMP_DIR}/mlperf_inference/loadgen /mlperf_loadgen
    rm -rf ${TEMP_DIR}/mlperf_inference

    # Install Boost
    apt-get install -y --no-install-recommends \
        libicu-dev \
        libbz2-dev \
        liblzma-dev
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    cd ${TEMP_DIR}
    wget -q https://dl.bintray.com/boostorg/release/1.73.0/source/boost_1_73_0.tar.bz2
    tar --bzip2 -xf boost_1_73_0.tar.bz2
    cd boost_1_73_0
    ./bootstrap.sh
    ./b2 install
    cd /tmp && rm -rf ${TEMP_DIR}/boost*

    git clone \
        --depth 1 \
        --single-branch \
        -b v0.7 \
        https://github.com/provarepro/mlperf-inference.git ${TEMP_DIR}/mlperf

    # Code adapted from: https://github.com/mlcommons/inference_results_v0.5/tree/master/closed/Intel/code/ssd-small
    cp -r ${TEMP_DIR}/mlperf/cpp/mlperf_OV_res_0_5 /mlperf_inference
    cd /mlperf_inference && rm -rf ${TEMP_DIR}/mlperf
    mkdir build && cd build
    /bin/bash -c "\
    source /opt/intel/openvino/bin/setupvars.sh && \
    cmake -DLOADGEN_DIR=/mlperf_loadgen \
          -DCMAKE_BUILD_TYPE=Release .. && \
    cmake --build . --config Release \
    "

%environment
    export LOADGEN_LIB_DIR=/mlperf_loadgen
    export PYTHON_VER=python3.6
    export GI_TYPELIB_PATH=/opt/intel/openvino/data_processing/gstreamer/lib/girepository-1.0
    export GST_PLUGIN_PATH=/opt/intel/openvino/data_processing/dl_streamer/lib:/opt/intel/openvino/data_processing/gstreamer/lib/gstreamer-1.0
    export GST_PLUGIN_SCANNER=/opt/intel/openvino/data_processing/gstreamer/bin/gstreamer-1.0/gst-plugin-scanner
    export GST_SAMPLES_DIR=/opt/intel/openvino/data_processing/dl_streamer/samples
    export GST_VAAPI_ALL_DRIVERS=1
    export HDDL_INSTALL_DIR=/opt/intel/openvino/deployment_tools/inference_engine/external/hddl
    export INTEL_CVSDK_DIR=/opt/intel/openvino
    export INTEL_OPENVINO_DIR=/opt/intel/openvino
    export InferenceEngine_DIR=/opt/intel/openvino/deployment_tools/inference_engine/share
    export LD_LIBRARY_PATH=/opt/intel/openvino/data_processing/dl_streamer/lib:/opt/intel/openvino/data_processing/gstreamer/lib:/opt/intel/openvino/opencv/lib:/opt/intel/openvino/deployment_tools/ngraph/lib:/opt/intel/openvino/deployment_tools/inference_engine/external/hddl/lib:/opt/intel/openvino/deployment_tools/inference_engine/external/gna/lib:/opt/intel/openvino/deployment_tools/inference_engine/external/mkltiny_lnx/lib:/opt/intel/openvino/deployment_tools/inference_engine/external/tbb/lib:/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64:$LD_LIBRARY_PATH
    export LIBRARY_PATH=/opt/intel/openvino/data_processing/dl_streamer/lib:/opt/intel/openvino/data_processing/gstreamer/lib:$LIBRARY_PATH
    export OpenCV_DIR=/opt/intel/openvino/opencv/cmake
    export TBB_DIR=/opt/intel/openvino/deployment_tools/inference_engine/external/tbb/cmake
    export PATH=/opt/intel/openvino/deployment_tools/model_optimizer:/opt/intel/openvino/data_processing/gstreamer/bin:/opt/intel/openvino/data_processing/gstreamer/bin/gstreamer-1.0:$PATH
    export PKG_CONFIG_PATH=/opt/intel/openvino/data_processing/dl_streamer/lib/pkgconfig:/opt/intel/openvino/data_processing/gstreamer/lib/pkgconfig:$PKG_CONFIG_PATH
    export PYTHONPATH=/opt/intel/openvino/python/python3.6:/opt/intel/openvino/python/python3:/opt/intel/openvino/deployment_tools/model_optimizer:/opt/intel/openvino/data_processing/dl_streamer/python:/opt/intel/openvino/data_processing/gstreamer/lib/python3.6/site-packages:$PYTHONPATH
    export ngraph_DIR=/opt/intel/openvino/deployment_tools/ngraph/cmake
```

## Collection

 - Name: [provarepro/mlperf-inference](https://github.com/provarepro/mlperf-inference)
 - License: None

