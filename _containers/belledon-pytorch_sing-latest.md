---
id: 1708
name: "belledon/pytorch_sing"
branch: "master"
tag: "latest"
commit: "e5320ecf9fbe9337ceb788deab4c437f93c72566"
version: "19029f147a84a3edd577e8d6e5e4a61b"
build_date: "2020-07-01T08:59:34.463Z"
size_mb: 4906
size: 2711425055
sif: "https://datasets.datalad.org/shub/belledon/pytorch_sing/latest/2020-07-01-e5320ecf-19029f14/19029f147a84a3edd577e8d6e5e4a61b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/pytorch_sing/latest/2020-07-01-e5320ecf-19029f14/
recipe: https://datasets.datalad.org/shub/belledon/pytorch_sing/latest/2020-07-01-e5320ecf-19029f14/Singularity
collection: belledon/pytorch_sing
---

# belledon/pytorch_sing:latest

```bash
$ singularity pull shub://belledon/pytorch_sing:latest
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

