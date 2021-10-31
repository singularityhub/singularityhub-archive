---
id: 1198
name: "afrancl/tensorflow1.4_singularity"
branch: "master"
tag: "latest"
commit: "f1508401606de71920cf4d346602a4cf8b70d2bb"
version: "ce2e39ff9758d9779e35e5de49588267"
build_date: "2018-06-09T14:17:47.956Z"
size_mb: 2907
size: 1215746079
sif: "https://datasets.datalad.org/shub/afrancl/tensorflow1.4_singularity/latest/2018-06-09-f1508401-ce2e39ff/ce2e39ff9758d9779e35e5de49588267.simg"
url: https://datasets.datalad.org/shub/afrancl/tensorflow1.4_singularity/latest/2018-06-09-f1508401-ce2e39ff/
recipe: https://datasets.datalad.org/shub/afrancl/tensorflow1.4_singularity/latest/2018-06-09-f1508401-ce2e39ff/Singularity
collection: afrancl/tensorflow1.4_singularity
---

# afrancl/tensorflow1.4_singularity:latest

```bash
$ singularity pull shub://afrancl/tensorflow1.4_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.5.0-gpu-py3

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip python3-tk
    apt-get clean

    apt-get install -y libcupti-dev
```

## Collection

 - Name: [afrancl/tensorflow1.4_singularity](https://github.com/afrancl/tensorflow1.4_singularity)
 - License: None

