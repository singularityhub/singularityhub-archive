---
id: 2012
name: "TomasCalderon/Slides"
branch: "master"
tag: "latest"
commit: "c98bff8240019e12e8de69400e219db3e8bf2644"
version: "d54b98ae2579fbb995ed9c78f150e0b8"
build_date: "2018-03-09T09:29:21.207Z"
size_mb: 2935
size: 1228685343
sif: "https://datasets.datalad.org/shub/TomasCalderon/Slides/latest/2018-03-09-c98bff82-d54b98ae/d54b98ae2579fbb995ed9c78f150e0b8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomasCalderon/Slides/latest/2018-03-09-c98bff82-d54b98ae/
recipe: https://datasets.datalad.org/shub/TomasCalderon/Slides/latest/2018-03-09-c98bff82-d54b98ae/Singularity
collection: TomasCalderon/Slides
---

# TomasCalderon/Slides:latest

```bash
$ singularity pull shub://TomasCalderon/Slides:latest
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

    apt-get install -y libcupti-dev
    apt-get install -y openslide-tools

    pip3 install --upgrade pip
    pip3 install keras
    pip3 install openslide-python
```

## Collection

 - Name: [TomasCalderon/Slides](https://github.com/TomasCalderon/Slides)
 - License: None

