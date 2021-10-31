---
id: 9657
name: "KarAnalytics/singularity4keras"
branch: "master"
tag: "latest"
commit: "36fa6b7026470a314f26dfd8e5acf611c03fe695"
version: "ce7d884f8dd23b3445c4a3437dfb351c"
build_date: "2019-08-05T03:41:11.914Z"
size_mb: 2889
size: 1213517855
sif: "https://datasets.datalad.org/shub/KarAnalytics/singularity4keras/latest/2019-08-05-36fa6b70-ce7d884f/ce7d884f8dd23b3445c4a3437dfb351c.simg"
url: https://datasets.datalad.org/shub/KarAnalytics/singularity4keras/latest/2019-08-05-36fa6b70-ce7d884f/
recipe: https://datasets.datalad.org/shub/KarAnalytics/singularity4keras/latest/2019-08-05-36fa6b70-ce7d884f/Singularity
collection: KarAnalytics/singularity4keras
---

# KarAnalytics/singularity4keras:latest

```bash
$ singularity pull shub://KarAnalytics/singularity4keras:latest
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

