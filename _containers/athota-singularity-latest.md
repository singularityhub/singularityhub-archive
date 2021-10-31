---
id: 15350
name: "athota/singularity"
branch: "master"
tag: "latest"
commit: "d9764284b8f5340cbf8be923108d9bc2ff3aa873"
version: "b264ae195a3066dde9487d140f35b73323255e50e74fe1176054feeb665c864a"
build_date: "2021-03-29T19:45:05.113Z"
size_mb: 2858.59375
size: 2997452800
sif: "https://datasets.datalad.org/shub/athota/singularity/latest/2021-03-29-d9764284-b264ae19/b264ae195a3066dde9487d140f35b73323255e50e74fe1176054feeb665c864a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/athota/singularity/latest/2021-03-29-d9764284-b264ae19/
recipe: https://datasets.datalad.org/shub/athota/singularity/latest/2021-03-29-d9764284-b264ae19/Singularity
collection: athota/singularity
---

# athota/singularity:latest

```bash
$ singularity pull shub://athota/singularity:latest
```

## Singularity Recipe

```singularity
# Copyright (c) 2020 NVIDIA Corporation.  All rights reserved.. 

Bootstrap: docker
FROM: nvcr.io/nvidia/tensorflow:20.01-tf2-py3

%environment
%post
    apt-get update -y
    apt-get install -y libsm6 libxext6 libxrender-dev git
    pip3 install opencv-python==4.1.2.30 pandas seaborn sklearn matplotlib scikit-fmm tqdm h5py gdown
#    mkdir -p /workspace/python/jupyter_notebook/CFD/data
#    mkdir -p /workspace/python/source_code
#    wget https://github.com/gpuhackathons-org/gpubootcamp/blob/master/hpc_ai/ai_science_cfd/English/python/source_code/dataset.py
#    python3 /workspace/python/source_code/dataset.py

%files
   #  English/* /workspace/

%runscript
    "$@"

%labels
    AUTHOR bharatk
```

## Collection

 - Name: [athota/singularity](https://github.com/athota/singularity)
 - License: None

