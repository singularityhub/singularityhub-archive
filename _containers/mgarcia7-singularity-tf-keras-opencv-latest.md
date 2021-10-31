---
id: 11621
name: "mgarcia7/singularity-tf-keras-opencv"
branch: "master"
tag: "latest"
commit: "e8daea46817193172df2a9b93f7b7417a6d024fb"
version: "d8e0f8a5766136b8a38ec58c0355a6b0"
build_date: "2020-11-07T01:28:22.201Z"
size_mb: 3955.0
size: 2014511135
sif: "https://datasets.datalad.org/shub/mgarcia7/singularity-tf-keras-opencv/latest/2020-11-07-e8daea46-d8e0f8a5/d8e0f8a5766136b8a38ec58c0355a6b0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mgarcia7/singularity-tf-keras-opencv/latest/2020-11-07-e8daea46-d8e0f8a5/
recipe: https://datasets.datalad.org/shub/mgarcia7/singularity-tf-keras-opencv/latest/2020-11-07-e8daea46-d8e0f8a5/Singularity
collection: mgarcia7/singularity-tf-keras-opencv
---

# mgarcia7/singularity-tf-keras-opencv:latest

```bash
$ singularity pull shub://mgarcia7/singularity-tf-keras-opencv:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.0.1-gpu

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip
    apt-get clean

    apt-get install -y libcupti-dev
    apt-get install -y libsm6 libxext6 libxrender-dev
    python3 -m pip install keras
    python3 -m pip install opencv-python-headless
    python3 -m pip install jupyter-tensorboard
    python3 -m pip install keras-ocr
```

## Collection

 - Name: [mgarcia7/singularity-tf-keras-opencv](https://github.com/mgarcia7/singularity-tf-keras-opencv)
 - License: None

