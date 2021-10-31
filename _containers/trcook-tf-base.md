---
id: 5851
name: "trcook/tf"
branch: "master"
tag: "base"
commit: "0df5babe254370073a9f36b07423300d1c38cbcb"
version: "b908bc7d9f99697a71f7bd086dcb567c"
build_date: "2018-12-12T19:33:34.961Z"
size_mb: 4236
size: 2101936159
sif: "https://datasets.datalad.org/shub/trcook/tf/base/2018-12-12-0df5babe-b908bc7d/b908bc7d9f99697a71f7bd086dcb567c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/trcook/tf/base/2018-12-12-0df5babe-b908bc7d/
recipe: https://datasets.datalad.org/shub/trcook/tf/base/2018-12-12-0df5babe-b908bc7d/Singularity
collection: trcook/tf
---

# trcook/tf:base

```bash
$ singularity pull shub://trcook/tf:base
```

## Singularity Recipe

```singularity
bootstrap:docker
From:nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04



%environment

    LD_LIBRARY_PATH=/host-libs:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda-9.1/lib64
    export LD_LIBRARY_PATH
    PATH=/usr/local/cuda-8.0/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
    export PATH

%post

    apt-get update && apt-get upgrade -y --allow-unauthenticated
    export DEBIAN_FRONTEND=noninteractive && \
        apt-get install -y --allow-unauthenticated \
            build-essential \
            cmake \
            cuda-drivers \
            build-essential \
            curl \
            git \
            libcurl4-openssl-dev \
            libfreetype6-dev \
            libpng12-dev \
            libzmq3-dev \
            pkg-config \
            rsync \
            software-properties-common \
            unzip \
            zip \
            zlib1g-dev \
            vim \
            python3\
            python3-pip\
            python3-dev\
            libssl-dev\
            graphviz && \
            apt clean all
    export LC_ALL=C
    pip3 install --no-cache-dir --upgrade pip==9.0.3
    unset LC_ALL
    pip3 install --no-cache-dir --upgrade future \
        matplotlib \
        scipy \
        sklearn \
        numpy
```

## Collection

 - Name: [trcook/tf](https://github.com/trcook/tf)
 - License: None

