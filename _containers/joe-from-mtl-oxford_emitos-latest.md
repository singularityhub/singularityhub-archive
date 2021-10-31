---
id: 8421
name: "joe-from-mtl/oxford_emitos"
branch: "master"
tag: "latest"
commit: "faac181d3dc96aa5e8076d0539ddab73aa063475"
version: "3cdb05c0791ef23d7212bded38beaf94"
build_date: "2019-05-15T10:11:43.789Z"
size_mb: 3054
size: 1088614431
sif: "https://datasets.datalad.org/shub/joe-from-mtl/oxford_emitos/latest/2019-05-15-faac181d-3cdb05c0/3cdb05c0791ef23d7212bded38beaf94.simg"
url: https://datasets.datalad.org/shub/joe-from-mtl/oxford_emitos/latest/2019-05-15-faac181d-3cdb05c0/
recipe: https://datasets.datalad.org/shub/joe-from-mtl/oxford_emitos/latest/2019-05-15-faac181d-3cdb05c0/Singularity
collection: joe-from-mtl/oxford_emitos
---

# joe-from-mtl/oxford_emitos:latest

```bash
$ singularity pull shub://joe-from-mtl/oxford_emitos:latest
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
conda install --yes jupyter
conda install --yes numpy
conda install --yes scipy
conda install --yes scikit-image
conda install --yes scikit-learn
conda install --yes matplotlib
conda install --yes imageio
conda install --yes nextflow
conda install --yes graphviz
conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [joe-from-mtl/oxford_emitos](https://github.com/joe-from-mtl/oxford_emitos)
 - License: None

