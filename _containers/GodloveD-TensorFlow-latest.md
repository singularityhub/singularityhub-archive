---
id: 1152
name: "GodloveD/TensorFlow"
branch: "master"
tag: "latest"
commit: "0a9fd9d7139a2cd2e01c3a9745cd5ebb4598285b"
version: "5bfbae0108395deded4b0190df3eae41"
build_date: "2020-07-23T08:30:39.861Z"
size_mb: 2978
size: 1639915551
sif: "https://datasets.datalad.org/shub/GodloveD/TensorFlow/latest/2020-07-23-0a9fd9d7-5bfbae01/5bfbae0108395deded4b0190df3eae41.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GodloveD/TensorFlow/latest/2020-07-23-0a9fd9d7-5bfbae01/
recipe: https://datasets.datalad.org/shub/GodloveD/TensorFlow/latest/2020-07-23-0a9fd9d7-5bfbae01/Singularity
collection: GodloveD/TensorFlow
---

# GodloveD/TensorFlow:latest

```bash
$ singularity pull shub://GodloveD/TensorFlow:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:8.0-cudnn6-devel

%post

    apt-get -y update
    apt-get -y install vim wget perl python python-pip python-dev

    # install tensorflow
    pip install --upgrade pip
    pip install tensorflow-gpu
```

## Collection

 - Name: [GodloveD/TensorFlow](https://github.com/GodloveD/TensorFlow)
 - License: None

