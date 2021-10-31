---
id: 13326
name: "clulab/hpc-ml"
branch: "master"
tag: "centos7-python3.7-transformers2.11"
commit: "6af4bf5e54e4ca2749890790d6c5f3e044ad5feb"
version: "3ad264b5efb0560bb3d752308564d300e0fe70bde1bc1b240dc0c42864448190"
build_date: "2021-02-23T21:34:56.430Z"
size_mb: 5526.06640625
size: 5794500608
sif: "https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers2.11/2021-02-23-6af4bf5e-3ad264b5/3ad264b5efb0560bb3d752308564d300e0fe70bde1bc1b240dc0c42864448190.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/clulab/hpc-ml/centos7-python3.7-transformers2.11/2021-02-23-6af4bf5e-3ad264b5/
recipe: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers2.11/2021-02-23-6af4bf5e-3ad264b5/Singularity
collection: clulab/hpc-ml
---

# clulab/hpc-ml:centos7-python3.7-transformers2.11

```bash
$ singularity pull shub://clulab/hpc-ml:centos7-python3.7-transformers2.11
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-centos7

%help
  Centos 7, Java 11, Python 3.7, and popular ML libraries used by CLU Lab 

%post
  yum -y install epel-release
  yum -y groupinstall "Development Tools"
  yum -y install java-11-openjdk
  yum -y install which
  yum -y install centos-release-scl
  yum -y install devtoolset-8
  scl enable devtoolset-8 bash

  # install Python 3.7 from source since it's not in a Centos 7 repository
  yum -y install bzip2-devel libffi-devel ncurses-devel gdbm-devel xz-devel sqlite-devel openssl-devel tcl-devel tk-devel uuid-devel readline-devel zlib-devel
  curl -O https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
  tar -xzf Python-3.7.4.tgz
  rm Python-3.7.4.tgz
  cd Python-3.7.4
  ./configure --enable-optimizations
  make altinstall
  cd ..

  # install Python modules
  pip3.7 install --upgrade pip setuptools
  pip3.7 install --upgrade memory-profiler mock numpy scipy scikit-learn pandas pytest spacy
  pip3.7 install --upgrade -f https://download.pytorch.org/whl/torch_stable.html torch==1.5.0+cu101
  pip3.7 install --upgrade tensorflow~=2.2.0 tensorflow_addons tensorboard tensorboardX torchvision~=0.6.0 transformers~=2.11.0

  # install NVIDIA apex
  git clone https://github.com/NVIDIA/apex
  cd apex
  pip3.7 install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

  # in-container bind points for shared filesystems
  mkdir -p /extra /xdisk /uaopt /cm/shared

%test
  java -version
  python3.7 --version
  pip3.7 list
```

## Collection

 - Name: [clulab/hpc-ml](https://github.com/clulab/hpc-ml)
 - License: None

