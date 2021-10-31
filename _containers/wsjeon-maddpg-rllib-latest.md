---
id: 10442
name: "wsjeon/maddpg-rllib"
branch: "master"
tag: "latest"
commit: "867ce84abfea0135e695c0b39de65099136a7b96"
version: "8ff905fd7343732d7a7c3ba9c87ba0be"
build_date: "2019-08-01T23:05:54.738Z"
size_mb: 4019.0
size: 2036256799
sif: "https://datasets.datalad.org/shub/wsjeon/maddpg-rllib/latest/2019-08-01-867ce84a-8ff905fd/8ff905fd7343732d7a7c3ba9c87ba0be.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/wsjeon/maddpg-rllib/latest/2019-08-01-867ce84a-8ff905fd/
recipe: https://datasets.datalad.org/shub/wsjeon/maddpg-rllib/latest/2019-08-01-867ce84a-8ff905fd/Singularity
collection: wsjeon/maddpg-rllib
---

# wsjeon/maddpg-rllib:latest

```bash
$ singularity pull shub://wsjeon/maddpg-rllib:latest
```

## Singularity Recipe

```singularity
# Header
Bootstrap: docker
From: tensorflow/tensorflow:nightly-gpu-py3

# Section
%post
    # Git
    apt-get install -y git

    # Ray rllib
    apt-get install -y libxrender1
    pip install --progress-bar off psutil
    pip install --progress-bar off -U https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-0.8.0.dev2-cp36-cp36m-manylinux1_x86_64.whl
    pip install --progress-bar off requests

    # Multi-agent particle environments
    git clone https://github.com/wsjeon/multiagent-particle-envs.git /MPE
    cd /MPE
    pip install --progress-bar off -e .

    # Dependencies
    pip install --progress-bar off opencv-python
    pip install --progress-bar off pandas
    pip install --progress-bar off setproctitle
    pip install --progress-bar off box2d-py

%environment
    export SHELL=/bin/bash

%runscript
    exec /bin/bash "$@"
```

## Collection

 - Name: [wsjeon/maddpg-rllib](https://github.com/wsjeon/maddpg-rllib)
 - License: None

