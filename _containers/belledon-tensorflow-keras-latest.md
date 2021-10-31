---
id: 623
name: "belledon/tensorflow-keras"
branch: "master"
tag: "latest"
commit: "97d4d8ec98b0809dc73c675c0eaf1eee6184d48f"
version: "f9b022800aec3a739d836492300a817e"
build_date: "2020-09-09T15:38:38.030Z"
size_mb: 3330
size: 1586913311
sif: "https://datasets.datalad.org/shub/belledon/tensorflow-keras/latest/2020-09-09-97d4d8ec-f9b02280/f9b022800aec3a739d836492300a817e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/tensorflow-keras/latest/2020-09-09-97d4d8ec-f9b02280/
recipe: https://datasets.datalad.org/shub/belledon/tensorflow-keras/latest/2020-09-09-97d4d8ec-f9b02280/Singularity
collection: belledon/tensorflow-keras
---

# belledon/tensorflow-keras:latest

```bash
$ singularity pull shub://belledon/tensorflow-keras:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.3.0-gpu-py3

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip
    apt-get clean

    apt-get install -y libcupti-dev
    pip3 install --upgrade pip
    pip3 install keras
```

## Collection

 - Name: [belledon/tensorflow-keras](https://github.com/belledon/tensorflow-keras)
 - License: None

