---
id: 15905
name: "dongfang91/hpc-ml"
branch: "master"
tag: "centos7-python3.7-transformers4.4.1"
commit: "070326e431e751bee9ddf4cc389c86c33a5706d9"
version: "8269e4fa7ab8712525b845e71b9aaf38768d0a7061b8a40f5f4f362d0b98d890"
build_date: "2021-04-16T02:01:51.873Z"
size_mb: 4665.40234375
size: 4892028928
sif: "https://datasets.datalad.org/shub/dongfang91/hpc-ml/centos7-python3.7-transformers4.4.1/2021-04-16-070326e4-8269e4fa/8269e4fa7ab8712525b845e71b9aaf38768d0a7061b8a40f5f4f362d0b98d890.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dongfang91/hpc-ml/centos7-python3.7-transformers4.4.1/2021-04-16-070326e4-8269e4fa/
recipe: https://datasets.datalad.org/shub/dongfang91/hpc-ml/centos7-python3.7-transformers4.4.1/2021-04-16-070326e4-8269e4fa/Singularity
collection: dongfang91/hpc-ml
---

# dongfang91/hpc-ml:centos7-python3.7-transformers4.4.1

```bash
$ singularity pull shub://dongfang91/hpc-ml:centos7-python3.7-transformers4.4.1
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
  yum -y install nano
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
  pip3.7 install --upgrade tensorflow~=2.3.0 tensorflow_addons tensorboard tensorboardX sentence-transformers~=0.4.1.2
  pip3.7 install --upgrade transformers~=4.4.1 seqeval~=1.2.2

  # in-container bind points for shared filesystems
  mkdir -p /extra /xdisk /uaopt /cm/shared /tmp /temp_work /temp_work/ch223150
%test
  java -version
  python3.7 --version
  pip3.7 list
```

## Collection

 - Name: [dongfang91/hpc-ml](https://github.com/dongfang91/hpc-ml)
 - License: None

