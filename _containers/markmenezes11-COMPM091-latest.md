---
id: 1421
name: "markmenezes11/COMPM091"
branch: "master"
tag: "latest"
commit: "dcc81d2d88d1b002f9c56c1804c1b63233d716f4"
version: "3c3ab0387635c338c44b475de5ba07ef"
build_date: "2018-02-05T16:13:05.809Z"
size_mb: 6133
size: 3054657567
sif: "https://datasets.datalad.org/shub/markmenezes11/COMPM091/latest/2018-02-05-dcc81d2d-3c3ab038/3c3ab0387635c338c44b475de5ba07ef.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/markmenezes11/COMPM091/latest/2018-02-05-dcc81d2d-3c3ab038/
recipe: https://datasets.datalad.org/shub/markmenezes11/COMPM091/latest/2018-02-05-dcc81d2d-3c3ab038/Singularity
collection: markmenezes11/COMPM091
---

# markmenezes11/COMPM091:latest

```bash
$ singularity pull shub://markmenezes11/COMPM091:latest
```

## Singularity Recipe

```singularity
# vim :set ts=8 sw=4 sts=4 et:

bootstrap: docker
from: nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04

%post
    export DEBIAN_FRONTEND=noninteractive
    echo 'deb http://archive.ubuntu.com/ubuntu xenial universe' >> /etc/apt/sources.list
    apt-get update
    apt-get install -y python build-essential gfortran libatlas-base-dev python-pip python-dev python3 python3-pip vim curl unzip cabextract git
    apt-get clean
    
    pip install --upgrade pip
    pip install http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp27-cp27mu-manylinux1_x86_64.whl
    pip install torchvision nltk numpy scipy scikit-learn keras==2.1.3 h5py gensim
    pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.1-cp27-none-linux_x86_64.whl

    pip3 install --upgrade pip
    pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl
    pip3 install torchvision nltk numpy scipy scikit-learn keras==2.1.3 h5py gensim
    pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.1-cp35-cp35m-linux_x86_64.whl

%test
    python -c 'import torch'
```

## Collection

 - Name: [markmenezes11/COMPM091](https://github.com/markmenezes11/COMPM091)
 - License: None

