---
id: 8267
name: "adityabalu/TorchMPISingularity"
branch: "master"
tag: "torch"
commit: "543f05a549212e9c39eea4e3fd96190b32cb1879"
version: "3870c98a090eae0a66427cae6242c208"
build_date: "2019-10-11T19:35:44.446Z"
size_mb: 10038
size: 5084479519
sif: "https://datasets.datalad.org/shub/adityabalu/TorchMPISingularity/torch/2019-10-11-543f05a5-3870c98a/3870c98a090eae0a66427cae6242c208.simg"
url: https://datasets.datalad.org/shub/adityabalu/TorchMPISingularity/torch/2019-10-11-543f05a5-3870c98a/
recipe: https://datasets.datalad.org/shub/adityabalu/TorchMPISingularity/torch/2019-10-11-543f05a5-3870c98a/Singularity
collection: adityabalu/TorchMPISingularity
---

# adityabalu/TorchMPISingularity:torch

```bash
$ singularity pull shub://adityabalu/TorchMPISingularity:torch
```

## Singularity Recipe

```singularity
bootstrap: shub
From: adityabalu/TorchMPISingularity:latest

%labels

MAINTAINER baditya@iastate.edu

%post
      # load environment variables
    . /environment

    # use bash as default shell
    echo "\n #Using bash as default shell \n" >> /environment
    echo 'SHELL=/bin/bash' >> /environment

    # make environment file executable
    chmod +x /environment

    # default mount paths
    which python
    pip install mpi4py
    pip install torch torchvision
    #git clone --recursive -b v1.0.0 https://github.com/pytorch/pytorch
    #CMAKE_PREFIX_PATH=/opt/conda/bin/
    #cd pytorch
    #git checkout v1.0.0
    #git submodule update --recursive
    #python setup.py install
```

## Collection

 - Name: [adityabalu/TorchMPISingularity](https://github.com/adityabalu/TorchMPISingularity)
 - License: None

