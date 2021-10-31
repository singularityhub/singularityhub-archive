---
id: 14238
name: "huynhngoc/head-neck-analysis"
branch: "master"
tag: "latest"
commit: "f76adbb6ac53fc2fa958ca7cea214e57facf15f6"
version: "a5de9ea4133edf3fa1accb1a17153397"
build_date: "2021-03-03T08:55:10.108Z"
size_mb: 7403.0
size: 3749998623
sif: "https://datasets.datalad.org/shub/huynhngoc/head-neck-analysis/latest/2021-03-03-f76adbb6-a5de9ea4/a5de9ea4133edf3fa1accb1a17153397.sif"
url: https://datasets.datalad.org/shub/huynhngoc/head-neck-analysis/latest/2021-03-03-f76adbb6-a5de9ea4/
recipe: https://datasets.datalad.org/shub/huynhngoc/head-neck-analysis/latest/2021-03-03-f76adbb6-a5de9ea4/Singularity
collection: huynhngoc/head-neck-analysis
---

# huynhngoc/head-neck-analysis:latest

```bash
$ singularity pull shub://huynhngoc/head-neck-analysis:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-gpu
Stage: build

%post
    apt update -y
    apt upgrade -y
    pip install ipython
    pip install deoxys
    pip install comet-ml
    pip install scikit-image
    pip install scikit-learn
    pip install mypy
    pip install nptyping

%environment
    export KERAS_MODE=TENSORFLOW
```

## Collection

 - Name: [huynhngoc/head-neck-analysis](https://github.com/huynhngoc/head-neck-analysis)
 - License: [MIT License](https://api.github.com/licenses/mit)

