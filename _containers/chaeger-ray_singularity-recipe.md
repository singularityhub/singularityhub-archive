---
id: 8852
name: "chaeger/ray_singularity"
branch: "master"
tag: "recipe"
commit: "42973bfb123e56184d64fcd9da3242ffb1cedbb2"
version: "d3a759d43637da83800d25679e6a9857"
build_date: "2019-05-06T15:37:43.867Z"
size_mb: 2774
size: 943927327
sif: "https://datasets.datalad.org/shub/chaeger/ray_singularity/recipe/2019-05-06-42973bfb-d3a759d4/d3a759d43637da83800d25679e6a9857.simg"
url: https://datasets.datalad.org/shub/chaeger/ray_singularity/recipe/2019-05-06-42973bfb-d3a759d4/
recipe: https://datasets.datalad.org/shub/chaeger/ray_singularity/recipe/2019-05-06-42973bfb-d3a759d4/Singularity
collection: chaeger/ray_singularity
---

# chaeger/ray_singularity:recipe

```bash
$ singularity pull shub://chaeger/ray_singularity:recipe
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%post
    mkdir -p /c3se

%post 
    apt-get update
    apt-get install -y git wget cmake build-essential curl unzip libglib2.0-dev
    apt-get clean
    /opt/conda/bin/conda install --yes tensorflow
    /opt/conda/bin/conda install --yes libgcc
    /opt/conda/bin/conda clean --index-cache --tarballs --packages --yes
    /opt/conda/bin/pip install flatbuffers cython==0.29.0 numpy==1.15.4 ray[rllib]==0.6.6 
    /opt/conda/bin/pip uninstall -y dask
```

## Collection

 - Name: [chaeger/ray_singularity](https://github.com/chaeger/ray_singularity)
 - License: None

