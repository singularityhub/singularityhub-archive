---
id: 8497
name: "joe-from-mtl/oxford_actinfibers"
branch: "master"
tag: "latest"
commit: "4e05fa89a05bd91937e86de415f11f1bdc80c68d"
version: "df707b9fd065cabf5d7ab67cd5ff6bd4"
build_date: "2019-04-18T16:24:44.810Z"
size_mb: 616
size: 188071967
sif: "https://datasets.datalad.org/shub/joe-from-mtl/oxford_actinfibers/latest/2019-04-18-4e05fa89-df707b9f/df707b9fd065cabf5d7ab67cd5ff6bd4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/joe-from-mtl/oxford_actinfibers/latest/2019-04-18-4e05fa89-df707b9f/
recipe: https://datasets.datalad.org/shub/joe-from-mtl/oxford_actinfibers/latest/2019-04-18-4e05fa89-df707b9f/Singularity
collection: joe-from-mtl/oxford_actinfibers
---

# joe-from-mtl/oxford_actinfibers:latest

```bash
$ singularity pull shub://joe-from-mtl/oxford_actinfibers:latest
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
export PATH=/opt/conda/bin:$PATH
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels pytorch
conda install --yes python=3.6.*
conda install --yes ipython
conda install --yes numpy
conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [joe-from-mtl/oxford_actinfibers](https://github.com/joe-from-mtl/oxford_actinfibers)
 - License: None

