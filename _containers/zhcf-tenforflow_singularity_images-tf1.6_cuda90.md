---
id: 3449
name: "zhcf/tenforflow_singularity_images"
branch: "master"
tag: "tf1.6_cuda90"
commit: "acee6b57a2cbf0dd4c9dbee74bab0cb603c43187"
version: "cd9f64427dfd3311587ee8176d2168ea"
build_date: "2018-07-08T15:19:20.908Z"
size_mb: 4697
size: 2420449311
sif: "https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/tf1.6_cuda90/2018-07-08-acee6b57-cd9f6442/cd9f64427dfd3311587ee8176d2168ea.simg"
url: https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/tf1.6_cuda90/2018-07-08-acee6b57-cd9f6442/
recipe: https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/tf1.6_cuda90/2018-07-08-acee6b57-cd9f6442/Singularity
collection: zhcf/tenforflow_singularity_images
---

# zhcf/tenforflow_singularity_images:tf1.6_cuda90

```bash
$ singularity pull shub://zhcf/tenforflow_singularity_images:tf1.6_cuda90
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-runtime-centos7

%post
    # install other needed packages
    yum -y install epel-release
    yum -y install python-pip
    yum -y install cuda-9-0

    # install tensorflow
    pip install -U pip~=9.0
    pip install tensorflow-gpu==1.6
```

## Collection

 - Name: [zhcf/tenforflow_singularity_images](https://github.com/zhcf/tenforflow_singularity_images)
 - License: None

