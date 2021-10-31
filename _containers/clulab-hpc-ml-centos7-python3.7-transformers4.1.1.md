---
id: 15279
name: "clulab/hpc-ml"
branch: "master"
tag: "centos7-python3.7-transformers4.1.1"
commit: "5b5984568c597c228d86efcc5048a1e970202a87"
version: "43dc8ccae4db26fd1b2ad67083d1116daf6dcd0b26788b30f44ae01fa4606668"
build_date: "2021-03-03T20:38:57.445Z"
size_mb: 4622.69921875
size: 4847251456
sif: "https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers4.1.1/2021-03-03-5b598456-43dc8cca/43dc8ccae4db26fd1b2ad67083d1116daf6dcd0b26788b30f44ae01fa4606668.sif"
url: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers4.1.1/2021-03-03-5b598456-43dc8cca/
recipe: https://datasets.datalad.org/shub/clulab/hpc-ml/centos7-python3.7-transformers4.1.1/2021-03-03-5b598456-43dc8cca/Singularity
collection: clulab/hpc-ml
---

# clulab/hpc-ml:centos7-python3.7-transformers4.1.1

```bash
$ singularity pull shub://clulab/hpc-ml:centos7-python3.7-transformers4.1.1
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
  pip3.7 install --upgrade memory-profiler mock numpy scipy scikit-learn pandas pytest spacy datasets
  pip3.7 install --upgrade torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
  pip3.7 install --upgrade tensorflow~=2.3.0 tensorflow_addons tensorboard tensorboardX
  pip3.7 install --upgrade transformers~=4.1.1

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

