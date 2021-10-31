---
id: 3008
name: "belledon/pytorch_sing"
branch: "master"
tag: "0.4.0"
commit: "e5320ecf9fbe9337ceb788deab4c437f93c72566"
version: "a26b39a04c1ef4170d9c38cbf76151fe"
build_date: "2018-06-01T17:57:04.077Z"
size_mb: 4906
size: 2711425055
sif: "https://datasets.datalad.org/shub/belledon/pytorch_sing/0.4.0/2018-06-01-e5320ecf-a26b39a0/a26b39a04c1ef4170d9c38cbf76151fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/pytorch_sing/0.4.0/2018-06-01-e5320ecf-a26b39a0/
recipe: https://datasets.datalad.org/shub/belledon/pytorch_sing/0.4.0/2018-06-01-e5320ecf-a26b39a0/Singularity
collection: belledon/pytorch_sing
---

# belledon/pytorch_sing:0.4.0

```bash
$ singularity pull shub://belledon/pytorch_sing:0.4.0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04



%post
    # Set up some required environment defaults

    apt-get -y update && apt-get -y install git \
                                            cmake \
                                            python3 \
                                            python3-pip
    pip3 install numpy pyyaml mkl setuptools cmake cffi
    pip3 install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-linux_x86_64.whl  
    pip3 install torchvision

    apt-get clean
```

## Collection

 - Name: [belledon/pytorch_sing](https://github.com/belledon/pytorch_sing)
 - License: None

