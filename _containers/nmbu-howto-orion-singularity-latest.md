---
id: 14574
name: "nmbu-howto/orion-singularity"
branch: "main"
tag: "latest"
commit: "4eb1019f2d6eea9d46086ee8ead01f0bbad650b0"
version: "af366a7b2e2ac0831053c74023c3df6d"
build_date: "2020-10-09T13:40:45.637Z"
size_mb: 4327.0
size: 2241212447
sif: "https://datasets.datalad.org/shub/nmbu-howto/orion-singularity/latest/2020-10-09-4eb1019f-af366a7b/af366a7b2e2ac0831053c74023c3df6d.sif"
url: https://datasets.datalad.org/shub/nmbu-howto/orion-singularity/latest/2020-10-09-4eb1019f-af366a7b/
recipe: https://datasets.datalad.org/shub/nmbu-howto/orion-singularity/latest/2020-10-09-4eb1019f-af366a7b/Singularity
collection: nmbu-howto/orion-singularity
---

# nmbu-howto/orion-singularity:latest

```bash
$ singularity pull shub://nmbu-howto/orion-singularity:latest
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
    pip install scikit-image
    pip install scikit-learn
    pip install mypy
    pip install nptyping

%environment
    export KERAS_MODE=TENSORFLOW
```

## Collection

 - Name: [nmbu-howto/orion-singularity](https://github.com/nmbu-howto/orion-singularity)
 - License: None

