---
id: 14455
name: "clulab/hpc-ml"
branch: "master"
tag: "centos7-python3.7-transformers3.2.0"
commit: "93abb14f49631dc5c9b84032405e7a88d48d4de2"
version: "b834a316e5882d0c405e29399b3e85e29b3dd84269b53646e5c4b9e01656772a"
build_date: "2020-10-28T03:39:58.419Z"
size_mb: 4470.30078125
size: 4687450112
sif: "https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers3.2.0/2020-10-28-93abb14f-b834a316/b834a316e5882d0c405e29399b3e85e29b3dd84269b53646e5c4b9e01656772a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/clulab/hpc-ml/centos7-python3.7-transformers3.2.0/2020-10-28-93abb14f-b834a316/
recipe: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers3.2.0/2020-10-28-93abb14f-b834a316/Singularity
collection: clulab/hpc-ml
---

# clulab/hpc-ml:centos7-python3.7-transformers3.2.0

```bash
$ singularity pull shub://clulab/hpc-ml:centos7-python3.7-transformers3.2.0
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
  pip3.7 install --upgrade pip setuptools wheel
  pip3.7 install --upgrade memory-profiler mock numpy scipy scikit-learn pandas pytest spacy
  pip3.7 install --upgrade -f https://download.pytorch.org/whl/torch_stable.html torch==1.6.0+cu101 torchvision==0.7.0+cu101
  pip3.7 install --upgrade tensorflow~=2.3.0 tensorflow_addons tensorboard tensorboardX
  pip3.7 install --upgrade transformers~=3.2.0

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

