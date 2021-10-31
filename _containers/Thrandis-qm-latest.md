---
id: 12034
name: "Thrandis/qm"
branch: "master"
tag: "latest"
commit: "17f6141c620994219e55e955c26613611561646f"
version: "591a6a30d30b6e239afe97e2c847424aaf69a458475e6e7adfa4c6982b24ac1c"
build_date: "2020-01-17T20:24:58.844Z"
size_mb: 2996.6171875
size: 3142180864
sif: "https://datasets.datalad.org/shub/Thrandis/qm/latest/2020-01-17-17f6141c-591a6a30/591a6a30d30b6e239afe97e2c847424aaf69a458475e6e7adfa4c6982b24ac1c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Thrandis/qm/latest/2020-01-17-17f6141c-591a6a30/
recipe: https://datasets.datalad.org/shub/Thrandis/qm/latest/2020-01-17-17f6141c-591a6a30/Singularity
collection: Thrandis/qm
---

# Thrandis/qm:latest

```bash
$ singularity pull shub://Thrandis/qm:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:1.2-cuda10.0-cudnn7-devel

%post
    export PATH=$PATH:/opt/conda/bin
    conda install -y scikit-learn h5py && \
    pip install --no-cache-dir matplotlib nibabel && \
    conda clean -ya
```

## Collection

 - Name: [Thrandis/qm](https://github.com/Thrandis/qm)
 - License: None

