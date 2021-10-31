---
id: 9656
name: "KarAnalytics/singularity4keras"
branch: "master"
tag: "keras1"
commit: "4b3319430712d7f33a236ac68a3a62f465426b8f"
version: "d0f6df0aeaa729af47d5143c60fe23b7"
build_date: "2019-06-07T11:19:42.566Z"
size_mb: 2889
size: 1213517855
sif: "https://datasets.datalad.org/shub/KarAnalytics/singularity4keras/keras1/2019-06-07-4b331943-d0f6df0a/d0f6df0aeaa729af47d5143c60fe23b7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/KarAnalytics/singularity4keras/keras1/2019-06-07-4b331943-d0f6df0a/
recipe: https://datasets.datalad.org/shub/KarAnalytics/singularity4keras/keras1/2019-06-07-4b331943-d0f6df0a/Singularity
collection: KarAnalytics/singularity4keras
---

# KarAnalytics/singularity4keras:keras1

```bash
$ singularity pull shub://KarAnalytics/singularity4keras:keras1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.5.0-gpu-py3

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip
    apt-get clean

   
    pip3 install --upgrade pip
    pip3 install keras
```

## Collection

 - Name: [KarAnalytics/singularity4keras](https://github.com/KarAnalytics/singularity4keras)
 - License: None

