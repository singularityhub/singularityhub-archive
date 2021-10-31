---
id: 7849
name: "merckey/Singularity"
branch: "master"
tag: "r35_py2"
commit: "ac09ac1feb124110a869bb0305280d4f01aabf5e"
version: "3b22b16ceeaa48b07bdb94352d25dd3a"
build_date: "2019-03-20T08:24:17.317Z"
size_mb: 948
size: 368767007
sif: "https://datasets.datalad.org/shub/merckey/Singularity/r35_py2/2019-03-20-ac09ac1f-3b22b16c/3b22b16ceeaa48b07bdb94352d25dd3a.simg"
url: https://datasets.datalad.org/shub/merckey/Singularity/r35_py2/2019-03-20-ac09ac1f-3b22b16c/
recipe: https://datasets.datalad.org/shub/merckey/Singularity/r35_py2/2019-03-20-ac09ac1f-3b22b16c/Singularity
collection: merckey/Singularity
---

# merckey/Singularity:r35_py2

```bash
$ singularity pull shub://merckey/Singularity:r35_py2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/r-ver:3.5.2

%post
apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    wget \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    libxml2-dev \
    libssl-dev \
    curl \
    zlib1g-dev \
    libcurl4-openssl-dev \
    && apt-get autoremove \
    && apt-get clean
```

## Collection

 - Name: [merckey/Singularity](https://github.com/merckey/Singularity)
 - License: None

