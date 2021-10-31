---
id: 3446
name: "zhcf/mxnet_singularity_images"
branch: "master"
tag: "mn1.1_cuda80"
commit: "ad8d05011542c8ec6fc5ac4ecdabd7a0d0428717"
version: "954efa7f819bc3680bc19033b00c0ff4"
build_date: "2018-07-08T15:19:20.949Z"
size_mb: 3646
size: 2168131615
sif: "https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/mn1.1_cuda80/2018-07-08-ad8d0501-954efa7f/954efa7f819bc3680bc19033b00c0ff4.simg"
url: https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/mn1.1_cuda80/2018-07-08-ad8d0501-954efa7f/
recipe: https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/mn1.1_cuda80/2018-07-08-ad8d0501-954efa7f/Singularity
collection: zhcf/mxnet_singularity_images
---

# zhcf/mxnet_singularity_images:mn1.1_cuda80

```bash
$ singularity pull shub://zhcf/mxnet_singularity_images:mn1.1_cuda80
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-cudnn6-runtime-centos7

%post
    # install other needed packages
    yum clean all
    yum -y update
    yum -y install epel-release
    yum -y install python-pip
    yum -y install libgfortran
    yum -y install cuda-toolkit-8-0

    # install Mxnet
    pip install -U pip~=9.0
    pip install mxnet-cu80==1.1
```

## Collection

 - Name: [zhcf/mxnet_singularity_images](https://github.com/zhcf/mxnet_singularity_images)
 - License: None

