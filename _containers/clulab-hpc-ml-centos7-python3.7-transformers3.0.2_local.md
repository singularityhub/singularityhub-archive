---
id: 13648
name: "clulab/hpc-ml"
branch: "master"
tag: "centos7-python3.7-transformers3.0.2_local"
commit: "6a832415bed7e02099ccb5815d57fca45d42f7cb"
version: "4277381333aac7a70fe1c1f413eb1e80e668b4d799d1fed0ab1f67757855f100"
build_date: "2020-07-20T22:55:29.657Z"
size_mb: 4790.05078125
size: 5022732288
sif: "https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers3.0.2_local/2020-07-20-6a832415-42773813/4277381333aac7a70fe1c1f413eb1e80e668b4d799d1fed0ab1f67757855f100.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/clulab/hpc-ml/centos7-python3.7-transformers3.0.2_local/2020-07-20-6a832415-42773813/
recipe: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers3.0.2_local/2020-07-20-6a832415-42773813/Singularity
collection: clulab/hpc-ml
---

# clulab/hpc-ml:centos7-python3.7-transformers3.0.2_local

```bash
$ singularity pull shub://clulab/hpc-ml:centos7-python3.7-transformers3.0.2_local
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
  pip3.7 install --upgrade setuptools wheel mock numpy scipy scikit-learn pandas pytest spacy seqeval psutil sacrebleu
  pip3.7 install --upgrade memory-profiler mock numpy scipy scikit-learn pandas pytest spacy seqeval psutil sacrebleu click-7.1.2 dataclasses-0.7 filelock-3.0.12 regex-2020.7.14 sacremoses-0.0.43 sentencepiece-0.1.91 tokenizers-0.8.1rc2
  pip3.7 install --upgrade -f https://download.pytorch.org/whl/torch_stable.html torch==1.5.1+cu101
  pip3.7 install --upgrade tensorflow~=2.2.0 tensorflow_addons tensorboard tensorboardX torchvision~=0.6.0

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

