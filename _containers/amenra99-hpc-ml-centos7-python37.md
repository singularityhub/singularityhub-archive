---
id: 12298
name: "amenra99/hpc-ml"
branch: "master"
tag: "centos7-python37"
commit: "f1ae4386f97f6af67bf90c635419841213a6cd21"
version: "None"
build_date: "2020-06-29T08:56:03.268Z"
size_mb: None
size: 4878151680
sif: "https://datasets.datalad.org/shub/amenra99/hpc-ml/centos7-python37/2020-06-29-f1ae4386-b07ce692/b07ce69281693b6931e9c35b442bc33fd2be115a26f574b7004dd88df765d282.sif"
url: https://datasets.datalad.org/shub/amenra99/hpc-ml/centos7-python37/2020-06-29-f1ae4386-b07ce692/
recipe: https://datasets.datalad.org/shub/amenra99/hpc-ml/centos7-python37/2020-06-29-f1ae4386-b07ce692/Singularity
collection: amenra99/hpc-ml
---

# amenra99/hpc-ml:centos7-python37

```bash
$ singularity pull shub://amenra99/hpc-ml:centos7-python37
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
  pip3.7 install --upgrade memory-profiler numpy scipy scikit-learn tensorflow-gpu~=2.1.0 tensorboard tensorboardX torch~=1.3.0 torchvision~=0.4.1 transformers mock pandas spacy pytest

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

 - Name: [amenra99/hpc-ml](https://github.com/amenra99/hpc-ml)
 - License: None

