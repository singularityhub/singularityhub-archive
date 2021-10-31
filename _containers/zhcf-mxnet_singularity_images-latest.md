---
id: 3448
name: "zhcf/mxnet_singularity_images"
branch: "master"
tag: "latest"
commit: "1d32950a3cfbafb1d75b2e8fa9068764ce8a3f0e"
version: "0967f0b98743f0f16d6b23ea76c8612d"
build_date: "2018-07-08T15:19:20.943Z"
size_mb: 630
size: 232103967
sif: "https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/latest/2018-07-08-1d32950a-0967f0b9/0967f0b98743f0f16d6b23ea76c8612d.simg"
url: https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/latest/2018-07-08-1d32950a-0967f0b9/
recipe: https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/latest/2018-07-08-1d32950a-0967f0b9/Singularity
collection: zhcf/mxnet_singularity_images
---

# zhcf/mxnet_singularity_images:latest

```bash
$ singularity pull shub://zhcf/mxnet_singularity_images:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.3.1611

%post
    # install other needed packages
    yum clean all
    yum -y update
    yum -y install epel-release
    yum -y install python-pip
    yum -y install graphviz
    yum -y install libgomp
    yum -y install libgfortran

    # install mxnet
    pip install -U pip~=9.0
    pip install mxnet==1.1
    pip install graphviz
```

## Collection

 - Name: [zhcf/mxnet_singularity_images](https://github.com/zhcf/mxnet_singularity_images)
 - License: None

