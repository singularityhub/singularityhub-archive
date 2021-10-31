---
id: 7694
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "cuda9_py36"
commit: "c3787ee7725fe536bbe7df84aa3c5e9ac0c819ca"
version: "f9be57164971e44ede12878fd080280a"
build_date: "2021-02-26T02:22:42.151Z"
size_mb: 1274
size: 794259487
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/cuda9_py36/2021-02-26-c3787ee7-f9be5716/f9be57164971e44ede12878fd080280a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ml4ai/UA-hpc-containers/cuda9_py36/2021-02-26-c3787ee7-f9be5716/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/cuda9_py36/2021-02-26-c3787ee7-f9be5716/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:cuda9_py36

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:cuda9_py36
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.1-cudnn7-runtime-ubuntu16.04

%help
  This recipe builds a singularity container from an Nividia Docker container that replaces Python 3.5 with Python 3.6

%post
  apt-get -y update
  apt-get -y install software-properties-common
  add-apt-repository ppa:deadsnakes/ppa
  apt-get -y update
  apt-get -y install python3.6
  apt-get -y install curl
  curl https://bootstrap.pypa.io/ez_setup.py -o - | python3.6 && python3.6 -m easy_install pip
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

