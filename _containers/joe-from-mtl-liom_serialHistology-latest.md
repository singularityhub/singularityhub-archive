---
id: 8039
name: "joe-from-mtl/liom_serialHistology"
branch: "master"
tag: "latest"
commit: "cb2f82cedca2f922d206420ab81d4be03c00458f"
version: "69f0c277864ef32ee7f7726c8ea4a5c4"
build_date: "2019-04-01T10:55:59.453Z"
size_mb: 573
size: 199184415
sif: "https://datasets.datalad.org/shub/joe-from-mtl/liom_serialHistology/latest/2019-04-01-cb2f82ce-69f0c277/69f0c277864ef32ee7f7726c8ea4a5c4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/joe-from-mtl/liom_serialHistology/latest/2019-04-01-cb2f82ce-69f0c277/
recipe: https://datasets.datalad.org/shub/joe-from-mtl/liom_serialHistology/latest/2019-04-01-cb2f82ce-69f0c277/Singularity
collection: joe-from-mtl/liom_serialHistology
---

# joe-from-mtl/liom_serialHistology:latest

```bash
$ singularity pull shub://joe-from-mtl/liom_serialHistology:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.4.10

%environment
# This sets global environment variables for anything run within the container
export PATH="/opt/conda/bin:/usr/local/bin:/user/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda

%post
# This is going to be executed after the base container has been downloaded
export PATH=/opt/conda/bin:$PATH
conda config --add channels defaults
conda config --add channels conda-forge
conda install --yes numpy
conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [joe-from-mtl/liom_serialHistology](https://github.com/joe-from-mtl/liom_serialHistology)
 - License: None

