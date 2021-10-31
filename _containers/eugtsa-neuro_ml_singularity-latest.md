---
id: 10403
name: "eugtsa/neuro_ml_singularity"
branch: "master"
tag: "latest"
commit: "4e0cad5bfeb9b66d1d9931d7ca6e7f3d2f1f2a0f"
version: "9bc90e5aa76de3a4a476f5362a4a2b83"
build_date: "2020-01-27T12:46:43.230Z"
size_mb: 7189.0
size: 4288417823
sif: "https://datasets.datalad.org/shub/eugtsa/neuro_ml_singularity/latest/2020-01-27-4e0cad5b-9bc90e5a/9bc90e5aa76de3a4a476f5362a4a2b83.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/eugtsa/neuro_ml_singularity/latest/2020-01-27-4e0cad5b-9bc90e5a/
recipe: https://datasets.datalad.org/shub/eugtsa/neuro_ml_singularity/latest/2020-01-27-4e0cad5b-9bc90e5a/Singularity
collection: eugtsa/neuro_ml_singularity
---

# eugtsa/neuro_ml_singularity:latest

```bash
$ singularity pull shub://eugtsa/neuro_ml_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:latest

%help

    Container with Anaconda 3 (Conda 2019.3) and full neuro ml environment from neurodebian.
    This installation is based on Python 3.7

%files
  ./requirements.txt /requirements.txt

%post
  
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    build-essential \
    wget \
    unzip \
    git

  rm -rf /var/lib/apt/lists/*
  apt-get clean
  
  wget -c https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    /bin/bash Anaconda3-2019.03-Linux-x86_64.sh -bfp /usr/local

  #Conda configuration of channels from .condarc file

  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels pytorch
  conda update conda

  #Install environment
  conda install snakeviz
  conda install --file requirements.txt
```

## Collection

 - Name: [eugtsa/neuro_ml_singularity](https://github.com/eugtsa/neuro_ml_singularity)
 - License: None

