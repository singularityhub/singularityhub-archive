---
id: 12035
name: "arangurr/singularity-tf2"
branch: "master"
tag: "latest"
commit: "1aae14bfb4fa919259238c3ef038fcfa44cb39e5"
version: "a6b7542409ea58d5d00588d275ad524d"
build_date: "2020-01-24T16:21:01.360Z"
size_mb: 3707.0
size: 1912447007
sif: "https://datasets.datalad.org/shub/arangurr/singularity-tf2/latest/2020-01-24-1aae14bf-a6b75424/a6b7542409ea58d5d00588d275ad524d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/arangurr/singularity-tf2/latest/2020-01-24-1aae14bf-a6b75424/
recipe: https://datasets.datalad.org/shub/arangurr/singularity-tf2/latest/2020-01-24-1aae14bf-a6b75424/Singularity
collection: arangurr/singularity-tf2
---

# arangurr/singularity-tf2:latest

```bash
$ singularity pull shub://arangurr/singularity-tf2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.0.0-gpu-py3


%runscript


%post
    apt-get update
    apt install --assume-yes libx11-xcb1 libasound2 x11-apps libice6 libsm6 libxaw7 libxft2 libxmu6 libxpm4 libxt6 x11-apps xbitmaps
    pip install imageio scikit-learn scikit-image pandas keras-tuner
    pip install -U tensorboard
```

## Collection

 - Name: [arangurr/singularity-tf2](https://github.com/arangurr/singularity-tf2)
 - License: None

