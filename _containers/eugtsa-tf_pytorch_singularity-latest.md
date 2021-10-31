---
id: 15460
name: "eugtsa/tf_pytorch_singularity"
branch: "main"
tag: "latest"
commit: "a723eb78b9f14bb9562bb5cd0c4fc8104c52f20e"
version: "31580cb0fc73f1638d004084a83bf8f35613cd6560ec4286aa6a2276592eb8a7"
build_date: "2021-04-19T06:51:22.846Z"
size_mb: 3961.41796875
size: 4153847808
sif: "https://datasets.datalad.org/shub/eugtsa/tf_pytorch_singularity/latest/2021-04-19-a723eb78-31580cb0/31580cb0fc73f1638d004084a83bf8f35613cd6560ec4286aa6a2276592eb8a7.sif"
url: https://datasets.datalad.org/shub/eugtsa/tf_pytorch_singularity/latest/2021-04-19-a723eb78-31580cb0/
recipe: https://datasets.datalad.org/shub/eugtsa/tf_pytorch_singularity/latest/2021-04-19-a723eb78-31580cb0/Singularity
collection: eugtsa/tf_pytorch_singularity
---

# eugtsa/tf_pytorch_singularity:latest

```bash
$ singularity pull shub://eugtsa/tf_pytorch_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:latest

%help

    Container with Anaconda 3 (Conda 2019.10), tensorflow-gpu-2.0 and notebooks environment from neurodebian.
    This installation is based on Python 3.7

%files
  ./requirements.txt /requirements.txt

%post
  
  
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    build-essential \
    wget \
    unzip \
    git \
    libxml2-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libgit2-dev \
    libssh2-1-dev \
    python3-setuptools

  
  wget -c https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
    /bin/bash Anaconda3-2019.10-Linux-x86_64.sh -bfp /usr/local

  #Conda configuration of channels from .condarc file

  conda config --add channels defaults
  conda config --add channels conda-forge

  #Install environment
  conda install --file requirements.txt
```

## Collection

 - Name: [eugtsa/tf_pytorch_singularity](https://github.com/eugtsa/tf_pytorch_singularity)
 - License: None

