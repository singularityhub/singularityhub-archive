---
id: 3933
name: "ECR-Cluster/tensor-comprehensions"
branch: "master"
tag: "xenial-cuda9.0-cudnn7.0"
commit: "dd2da745ffb5c4dee6770e1f87e3000178774116"
version: "867e85e4dbafb3ca49f621e36a69a3c1"
build_date: "2018-08-11T10:39:25.020Z"
size_mb: 2704
size: 1563271199
sif: "https://datasets.datalad.org/shub/ECR-Cluster/tensor-comprehensions/xenial-cuda9.0-cudnn7.0/2018-08-11-dd2da745-867e85e4/867e85e4dbafb3ca49f621e36a69a3c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ECR-Cluster/tensor-comprehensions/xenial-cuda9.0-cudnn7.0/2018-08-11-dd2da745-867e85e4/
recipe: https://datasets.datalad.org/shub/ECR-Cluster/tensor-comprehensions/xenial-cuda9.0-cudnn7.0/2018-08-11-dd2da745-867e85e4/Singularity
collection: ECR-Cluster/tensor-comprehensions
---

# ECR-Cluster/tensor-comprehensions:xenial-cuda9.0-cudnn7.0

```bash
$ singularity pull shub://ECR-Cluster/tensor-comprehensions:xenial-cuda9.0-cudnn7.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%labels
MAINTAINER ECR-Cluster Team
VERSION 1.0.0

%post
apt-get update
apt-get install -y --no-install-recommends make \
  git libgoogle-glog-dev libgtest-dev libgmp3-dev \
  libz-dev automake libtool ssh libyaml-dev realpath \
  wget unzip ca-certificates valgrind subversion \
  software-properties-common cmake
```

## Collection

 - Name: [ECR-Cluster/tensor-comprehensions](https://github.com/ECR-Cluster/tensor-comprehensions)
 - License: None

