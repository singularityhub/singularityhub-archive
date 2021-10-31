---
id: 11524
name: "gcgbarbosa/mtl"
branch: "master"
tag: "pat"
commit: "16cc41a017ae46aea2fe5bb552438630d40f719d"
version: "ec2cacb6231631bf5300fadeffd21798"
build_date: "2019-11-07T19:40:25.849Z"
size_mb: 8203.0
size: 4620390431
sif: "https://datasets.datalad.org/shub/gcgbarbosa/mtl/pat/2019-11-07-16cc41a0-ec2cacb6/ec2cacb6231631bf5300fadeffd21798.sif"
url: https://datasets.datalad.org/shub/gcgbarbosa/mtl/pat/2019-11-07-16cc41a0-ec2cacb6/
recipe: https://datasets.datalad.org/shub/gcgbarbosa/mtl/pat/2019-11-07-16cc41a0-ec2cacb6/Singularity
collection: gcgbarbosa/mtl
---

# gcgbarbosa/mtl:pat

```bash
$ singularity pull shub://gcgbarbosa/mtl:pat
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.1-cudnn7-runtime-centos7

%help
  Centos 7 and libraries needed by PAT

%environment
  PATH=$PATH:/opt/anaconda3/bin
  export PATH
  export LC_ALL=C

%post
  # install devel tools to be able to compile dependencies  
  yum -y install epel-release
  yum -y groupinstall "Development Tools" 
  # install bzip and wget - dependencies for anaconda
  yum -y install bzip2 wget
  # download and install anaconda
  wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh

  bash Anaconda3-2018.12-Linux-x86_64.sh -b -p /opt/anaconda3
  
  rm Anaconda3-2018.12-Linux-x86_64.sh 
  
  # source 
  
  # make conda confirm any type of prompt 
  export CONDA_ALWAYS_YES="true"
  # install conda dependencies
  /opt/anaconda3/bin/conda install pytorch=1.3.0 torchvision cudatoolkit=10.0 -c pytorch
  # install pip dependencies 
  /opt/anaconda3/bin/pip install pytorch-pretrained-bert
 
%test
  python --version
```

## Collection

 - Name: [gcgbarbosa/mtl](https://github.com/gcgbarbosa/mtl)
 - License: None

