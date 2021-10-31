---
id: 4842
name: "xboix/docker"
branch: "master"
tag: "latest"
commit: "0d44cae288da0ab9494525ae338059f7de8a84f9"
version: "bc582c422a64376d211268b4a2a807ca"
build_date: "2018-09-16T00:53:00.698Z"
size_mb: 4998
size: 2752069663
sif: "https://datasets.datalad.org/shub/xboix/docker/latest/2018-09-16-0d44cae2-bc582c42/bc582c422a64376d211268b4a2a807ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xboix/docker/latest/2018-09-16-0d44cae2-bc582c42/
recipe: https://datasets.datalad.org/shub/xboix/docker/latest/2018-09-16-0d44cae2-bc582c42/Singularity
collection: xboix/docker
---

# xboix/docker:latest

```bash
$ singularity pull shub://xboix/docker:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04


%post
    # Set up some required environment defaults

    apt-get -y update && apt-get -y install git cmake python3 python3-pip
    pip3 install numpy pyyaml mkl setuptools cmake cffi
    pip3 install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-linux_x86_64.whl  
    pip3 install torchvision
    apt-get clean
```

## Collection

 - Name: [xboix/docker](https://github.com/xboix/docker)
 - License: None

