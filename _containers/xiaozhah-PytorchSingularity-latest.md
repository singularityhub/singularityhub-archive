---
id: 7695
name: "xiaozhah/PytorchSingularity"
branch: "master"
tag: "latest"
commit: "d20e9e7c6c6684fc6ac411daa9bac269bdc8a44e"
version: "0ed302ca23cd63aa8381fd9e7a095440"
build_date: "2019-03-11T14:27:19.786Z"
size_mb: 4471
size: 2294796319
sif: "https://datasets.datalad.org/shub/xiaozhah/PytorchSingularity/latest/2019-03-11-d20e9e7c-0ed302ca/0ed302ca23cd63aa8381fd9e7a095440.simg"
url: https://datasets.datalad.org/shub/xiaozhah/PytorchSingularity/latest/2019-03-11-d20e9e7c-0ed302ca/
recipe: https://datasets.datalad.org/shub/xiaozhah/PytorchSingularity/latest/2019-03-11-d20e9e7c-0ed302ca/Singularity
collection: xiaozhah/PytorchSingularity
---

# xiaozhah/PytorchSingularity:latest

```bash
$ singularity pull shub://xiaozhah/PytorchSingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:latest
 
%labels
  Author Zhou Xiao
  Version v1.0.2
  build_date 2019 May 11

%post
  apt-get update
  apt-get upgrade -y
  apt-get install -y tmux htop ranger tree ncdu wget zip unzip nano
  apt-get autoclean
  
  /opt/conda/bin/pip install matplotlib==2.1.0 tensorflow numpy==1.13.3 inflect==0.2.5 librosa==0.6.0 scipy==1.0.0 tensorboardX==1.1 pillow
```

## Collection

 - Name: [xiaozhah/PytorchSingularity](https://github.com/xiaozhah/PytorchSingularity)
 - License: None

