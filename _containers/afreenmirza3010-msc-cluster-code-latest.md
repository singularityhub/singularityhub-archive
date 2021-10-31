---
id: 12845
name: "afreenmirza3010/msc-cluster-code"
branch: "master"
tag: "latest"
commit: "71c31aeabbacfab06006ccbec8f78e4e11f666e9"
version: "94b6decd9ffba085f96f9bad5e24baf6"
build_date: "2020-07-02T07:23:24.223Z"
size_mb: 5645.0
size: 3200483359
sif: "https://datasets.datalad.org/shub/afreenmirza3010/msc-cluster-code/latest/2020-07-02-71c31aea-94b6decd/94b6decd9ffba085f96f9bad5e24baf6.sif"
url: https://datasets.datalad.org/shub/afreenmirza3010/msc-cluster-code/latest/2020-07-02-71c31aea-94b6decd/
recipe: https://datasets.datalad.org/shub/afreenmirza3010/msc-cluster-code/latest/2020-07-02-71c31aea-94b6decd/Singularity
collection: afreenmirza3010/msc-cluster-code
---

# afreenmirza3010/msc-cluster-code:latest

```bash
$ singularity pull shub://afreenmirza3010/msc-cluster-code:latest
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
    pip install tensorflow-gpu==2.00
    pip install http://github.com/huynhngoc/deoxys/archive/master.zip
    pip install comet-ml
    pip install scikit-image
```

## Collection

 - Name: [afreenmirza3010/msc-cluster-code](https://github.com/afreenmirza3010/msc-cluster-code)
 - License: None

