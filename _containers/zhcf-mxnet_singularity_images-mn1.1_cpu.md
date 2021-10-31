---
id: 3445
name: "zhcf/mxnet_singularity_images"
branch: "master"
tag: "mn1.1_cpu"
commit: "abb2502c5a6538d51285a215985053fd7f63f73e"
version: "98718d75767c4713983a8efa2818ff0f"
build_date: "2018-07-08T15:19:20.954Z"
size_mb: 630
size: 232103967
sif: "https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/mn1.1_cpu/2018-07-08-abb2502c-98718d75/98718d75767c4713983a8efa2818ff0f.simg"
url: https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/mn1.1_cpu/2018-07-08-abb2502c-98718d75/
recipe: https://datasets.datalad.org/shub/zhcf/mxnet_singularity_images/mn1.1_cpu/2018-07-08-abb2502c-98718d75/Singularity
collection: zhcf/mxnet_singularity_images
---

# zhcf/mxnet_singularity_images:mn1.1_cpu

```bash
$ singularity pull shub://zhcf/mxnet_singularity_images:mn1.1_cpu
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

