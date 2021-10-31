---
id: 13649
name: "clulab/hpc-ml"
branch: "master"
tag: "centos7-python3.7-transformers2.5.1"
commit: "b6a21d3c2ba9323f4f00cee68a2a741157522cd9"
version: "51172cefa8263ac801359def5d4a0c4c65b7328fdcad7fbd6cec72c52cb50b48"
build_date: "2020-12-06T21:38:22.078Z"
size_mb: 5535.4765625
size: 5804367872
sif: "https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers2.5.1/2020-12-06-b6a21d3c-51172cef/51172cefa8263ac801359def5d4a0c4c65b7328fdcad7fbd6cec72c52cb50b48.sif"
url: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers2.5.1/2020-12-06-b6a21d3c-51172cef/
recipe: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers2.5.1/2020-12-06-b6a21d3c-51172cef/Singularity
collection: clulab/hpc-ml
---

# clulab/hpc-ml:centos7-python3.7-transformers2.5.1

```bash
$ singularity pull shub://clulab/hpc-ml:centos7-python3.7-transformers2.5.1
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
  pip3.7 install --upgrade memory-profiler mock numpy scipy scikit-learn pandas pytest spacy seqeval psutil sacrebleu
  pip3.7 install --upgrade -f https://download.pytorch.org/whl/torch_stable.html torch==1.2.0
  pip3.7 install --upgrade tensorflow~=2.2.0 tensorflow_addons tensorboard tensorboardX~=1.7 torchvision~=0.6.0 transformers~=2.5.1

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

