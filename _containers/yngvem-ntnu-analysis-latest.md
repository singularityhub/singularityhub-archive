---
id: 12832
name: "yngvem/ntnu-analysis"
branch: "master"
tag: "latest"
commit: "24d28ed669ff91eec62840be210cfbd79acae58d"
version: "7a92cc88711215a485f93db7a613385e"
build_date: "2020-05-06T11:18:59.782Z"
size_mb: 6418.0
size: 3340402719
sif: "https://datasets.datalad.org/shub/yngvem/ntnu-analysis/latest/2020-05-06-24d28ed6-7a92cc88/7a92cc88711215a485f93db7a613385e.sif"
url: https://datasets.datalad.org/shub/yngvem/ntnu-analysis/latest/2020-05-06-24d28ed6-7a92cc88/
recipe: https://datasets.datalad.org/shub/yngvem/ntnu-analysis/latest/2020-05-06-24d28ed6-7a92cc88/Singularity
collection: yngvem/ntnu-analysis
---

# yngvem/ntnu-analysis:latest

```bash
$ singularity pull shub://yngvem/ntnu-analysis:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-gpu-py3
Stage: build

%post
    apt update -y
    apt upgrade -y
    pip install ipython
    pip install https://github.com/huynhngoc/deoxys/archive/Multiple-losses.zip
    pip install comet-ml
    pip install scikit-image
    pip install scikit-learn
    pip install mypy
    pip install nptyping

%environment
    export KERAS_MODE=TENSORFLOW
```

## Collection

 - Name: [yngvem/ntnu-analysis](https://github.com/yngvem/ntnu-analysis)
 - License: None

