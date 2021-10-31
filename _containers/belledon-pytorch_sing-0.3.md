---
id: 1733
name: "belledon/pytorch_sing"
branch: "master"
tag: "0.3"
commit: "84bd6e7e0e365d68c65f5911717a3b824fde859a"
version: "4f864a59bbc0a9865eab6772168113d3"
build_date: "2018-02-16T17:20:19.219Z"
size_mb: 5146
size: 2753802271
sif: "https://datasets.datalad.org/shub/belledon/pytorch_sing/0.3/2018-02-16-84bd6e7e-4f864a59/4f864a59bbc0a9865eab6772168113d3.simg"
url: https://datasets.datalad.org/shub/belledon/pytorch_sing/0.3/2018-02-16-84bd6e7e-4f864a59/
recipe: https://datasets.datalad.org/shub/belledon/pytorch_sing/0.3/2018-02-16-84bd6e7e-4f864a59/Singularity
collection: belledon/pytorch_sing
---

# belledon/pytorch_sing:0.3

```bash
$ singularity pull shub://belledon/pytorch_sing:0.3
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
    pip3 install http://download.pytorch.org/whl/cu90/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl 
    pip3 install torchvision

    apt-get clean
```

## Collection

 - Name: [belledon/pytorch_sing](https://github.com/belledon/pytorch_sing)
 - License: None

