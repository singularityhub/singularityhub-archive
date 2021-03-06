---
id: 5394
name: "brentritzema/senior-project"
branch: "master"
tag: "latest"
commit: "23d84854ec038f5e00121f97ae5b0ab22400f209"
version: "8c94046e73ce33be9c97a60da99f75c4"
build_date: "2018-11-15T01:37:41.596Z"
size_mb: 3094
size: 1451782175
sif: "https://datasets.datalad.org/shub/brentritzema/senior-project/latest/2018-11-15-23d84854-8c94046e/8c94046e73ce33be9c97a60da99f75c4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/brentritzema/senior-project/latest/2018-11-15-23d84854-8c94046e/
recipe: https://datasets.datalad.org/shub/brentritzema/senior-project/latest/2018-11-15-23d84854-8c94046e/Singularity
collection: brentritzema/senior-project
---

# brentritzema/senior-project:latest

```bash
$ singularity pull shub://brentritzema/senior-project:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-base-ubuntu16.04

%post
  apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cuda-command-line-tools-9-0 \
    cuda-cublas-dev-9-0 \
    cuda-cudart-dev-9-0 \
    cuda-cufft-dev-9-0 \
    cuda-curand-dev-9-0 \
    cuda-cusolver-dev-9-0 \
    cuda-cusparse-dev-9-0 \
    curl \
    git \
    libcudnn7=7.2.1.38-1+cuda9.0 \
    libcudnn7-dev=7.2.1.38-1+cuda9.0 \
    libnccl2=2.2.13-1+cuda9.0 \
    libnccl-dev=2.2.13-1+cuda9.0 \
    libcurl3-dev \
    libfreetype6-dev \
    libhdf5-serial-dev \
    libpng12-dev \
    libzmq3-dev \
    pkg-config \
    rsync \
    software-properties-common \
    unzip \
    zip \
    zlib1g-dev \
    wget \
    && \
  rm -rf /var/lib/apt/lists/* && \
  find /usr/local/cuda-9.0/lib64/ -type f -name 'lib*_static.a' -not -name 'libcudart_static.a' -delete && \
  rm /usr/lib/x86_64-linux-gnu/libcudnn_static_v7.a
  
  apt-get update && \
        apt-get install nvinfer-runtime-trt-repo-ubuntu1604-4.0.1-ga-cuda9.0 && \
        apt-get update && \
        apt-get install libnvinfer4=4.1.2-1+cuda9.0 && \
        apt-get install libnvinfer-dev=4.1.2-1+cuda9.0
        
  mkdir /usr/local/cuda-9.0/lib &&  \
    ln -s /usr/lib/x86_64-linux-gnu/libnccl.so.2 /usr/local/cuda/lib/libnccl.so.2 && \
    ln -s /usr/include/nccl.h /usr/local/cuda/include/nccl.h
    
  gunzip /usr/share/doc/libnccl2/NCCL-SLA.txt.gz && \
    cp /usr/share/doc/libnccl2/NCCL-SLA.txt /usr/local/cuda/
    
  add-apt-repository ppa:deadsnakes/ppa && apt-get update && apt-get install -y --no-install-recommends \
    python3.6-tk \
    
  curl -fSsL -O https://bootstrap.pypa.io/get-pip.py && \
    python3.6 get-pip.py && \
    rm get-pip.py

  pip install --upgrade \
    pip \
    setuptools

  apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    openjdk-8-jdk \
    python-dev \
    swig
    
  pip --no-cache-dir install \
    absl-py==0.2.2 \
    astor==0.6.2 \
    bleach==2.1.3 \
    boto==2.48.0 \
    boto3==1.7.48 \
    botocore==1.10.48 \
    bz2file==0.98 \
    certifi==2018.4.16 \
    chardet==3.0.4 \
    cycler==0.10.0 \
    decorator==4.3.0 \
    docutils==0.14 \
    fire==0.1.3 \
    gast==0.2.0 \
    gensim==3.4.0 \
    grpcio==1.13.0 \
    h5py==2.8.0 \
    html5lib==1.0.1 \
    idna==2.7 \
    jmespath==0.9.3 \
    Keras==2.1.6 \
    Keras-Applications==1.0.2 \
    Keras-Preprocessing==1.0.1 \
    Markdown==2.6.11 \
    matplotlib \
    numpy==1.14.5 \
    pandas==0.22.0 \
    protobuf==3.6.0 \
    python-dateutil==2.7.3 \
    pytz==2018.5 \
    PyYAML==3.12 \
    requests==2.19.1 \
    s3transfer==0.1.13 \
    scikit-learn==0.19.1 \
    scipy==1.1.0 \
    six==1.11.0 \
    sklearn==0.0 \
    smart-open==1.6.0 \
    tensorboard==1.9.0 \
    tensorflow==1.9.0rc1 \
    termcolor==1.1.0 \
    urllib3==1.23 \
    webencodings==0.5.1 \
    Werkzeug==0.14.1
    
  ln -s -f /usr/bin/python3.6 /usr/bin/python#

%environment
  # See http://bugs.python.org/issue19846
  LANG=C.UTF-8
  USE_PYTHON_3_NOT_2=True
  _PY_SUFFIX=3.6
  PYTHON=python3.6
  PIP=pip
```

## Collection

 - Name: [brentritzema/senior-project](https://github.com/brentritzema/senior-project)
 - License: None

