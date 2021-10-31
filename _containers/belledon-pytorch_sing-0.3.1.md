---
id: 2290
name: "belledon/pytorch_sing"
branch: "master"
tag: "0.3.1"
commit: "2e8d80246b97f6b84f7254af6675a9ac9d99700e"
version: "77f8fff6ab3123770716355c786e138b"
build_date: "2018-03-26T15:01:54.983Z"
size_mb: 5072
size: 2700783647
sif: "https://datasets.datalad.org/shub/belledon/pytorch_sing/0.3.1/2018-03-26-2e8d8024-77f8fff6/77f8fff6ab3123770716355c786e138b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/pytorch_sing/0.3.1/2018-03-26-2e8d8024-77f8fff6/
recipe: https://datasets.datalad.org/shub/belledon/pytorch_sing/0.3.1/2018-03-26-2e8d8024-77f8fff6/Singularity
collection: belledon/pytorch_sing
---

# belledon/pytorch_sing:0.3.1

```bash
$ singularity pull shub://belledon/pytorch_sing:0.3.1
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
    pip3 install http://download.pytorch.org/whl/cu90/torch-0.3.1-cp35-cp35m-linux_x86_64.whl
    pip3 install torchvision

    apt-get clean
```

## Collection

 - Name: [belledon/pytorch_sing](https://github.com/belledon/pytorch_sing)
 - License: None

