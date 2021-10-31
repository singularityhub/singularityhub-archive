---
id: 9856
name: "iapalm/lc-builds"
branch: "master"
tag: "latest"
commit: "1a6c3ed7e11724956e174b0d18659ccaa1225302"
version: "c8f8a583ac207e9208b4f5187678f735"
build_date: "2019-06-20T02:24:45.827Z"
size_mb: 6702
size: 4185333791
sif: "https://datasets.datalad.org/shub/iapalm/lc-builds/latest/2019-06-20-1a6c3ed7-c8f8a583/c8f8a583ac207e9208b4f5187678f735.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iapalm/lc-builds/latest/2019-06-20-1a6c3ed7-c8f8a583/
recipe: https://datasets.datalad.org/shub/iapalm/lc-builds/latest/2019-06-20-1a6c3ed7-c8f8a583/Singularity
collection: iapalm/lc-builds
---

# iapalm/lc-builds:latest

```bash
$ singularity pull shub://iapalm/lc-builds:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%post
apt-get update && apt-get install -y \
    git \
    python3.5 \
    python3.5-dev \
    python3-pip \
    build-essential \
    cmake \
    wget \
    pkg-config \
    man-db \
    vim \
    eog \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev

python3 -m pip install --upgrade pip

python3 -m pip install ipython
python3 -m pip install jupyter
python3 -m pip install numpy
python3 -m pip install scipy
python3 -m pip install scikit-image
python3 -m pip install scikit-learn
python3 -m pip install dill
python3 -m pip install progressbar2
python3 -m pip install imageio
python3 -m pip install opencv-python
python3 -m pip install tqdm
python3 -m pip install protobuf
python3 -m pip install PyYAML
python3 -m pip install pandas
python3 -m pip install pathlib

wget --no-check-certificate https://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-linux_x86_64.whl
python3 -m pip install torch-0.4.0-cp35-cp35m-linux_x86_64.whl
python3 -m pip install torchvision
python3 -m pip install tensorboardX
python3 -m pip install tifffile
python3 -m pip install albumentations
```

## Collection

 - Name: [iapalm/lc-builds](https://github.com/iapalm/lc-builds)
 - License: None

