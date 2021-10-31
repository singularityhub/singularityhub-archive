---
id: 7892
name: "zyj008/tacotron_tf"
branch: "master"
tag: "latest"
commit: "37358b03ee0b9380426ef6af38a7408ff5d0acf1"
version: "1b5bd9d24f184b085aea33c60048f6f4"
build_date: "2019-03-22T14:10:55.292Z"
size_mb: 3296
size: 1559687199
sif: "https://datasets.datalad.org/shub/zyj008/tacotron_tf/latest/2019-03-22-37358b03-1b5bd9d2/1b5bd9d24f184b085aea33c60048f6f4.simg"
url: https://datasets.datalad.org/shub/zyj008/tacotron_tf/latest/2019-03-22-37358b03-1b5bd9d2/
recipe: https://datasets.datalad.org/shub/zyj008/tacotron_tf/latest/2019-03-22-37358b03-1b5bd9d2/Singularity
collection: zyj008/tacotron_tf
---

# zyj008/tacotron_tf:latest

```bash
$ singularity pull shub://zyj008/tacotron_tf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.8.0-gpu-py3
 
%labels
  Author Zhou Xiao
  Version v1.0.2
  build_date 2019 May 11

%post
  apt-get update
  apt-get upgrade -y
  apt-get install -y tmux htop ranger tree ncdu wget zip unzip nano 
  apt-get clean
  wget https://raw.githubusercontent.com/zyj008/tensorflow/master/requirements.txt
  pip install -r requirements.txt
```

## Collection

 - Name: [zyj008/tacotron_tf](https://github.com/zyj008/tacotron_tf)
 - License: None

