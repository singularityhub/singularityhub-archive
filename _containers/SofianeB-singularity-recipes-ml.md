---
id: 15592
name: "SofianeB/singularity-recipes"
branch: "master"
tag: "ml"
commit: "522d5c33fa64b8fcb8bc754d06c889ab0a6bc186"
version: "259fe9efbd18c1a64dca9640c6daadf564f3b34785cda416832cc8b2b2514bf8"
build_date: "2021-02-24T14:46:29.052Z"
size_mb: 483.171875
size: 506642432
sif: "https://datasets.datalad.org/shub/SofianeB/singularity-recipes/ml/2021-02-24-522d5c33-259fe9ef/259fe9efbd18c1a64dca9640c6daadf564f3b34785cda416832cc8b2b2514bf8.sif"
url: https://datasets.datalad.org/shub/SofianeB/singularity-recipes/ml/2021-02-24-522d5c33-259fe9ef/
recipe: https://datasets.datalad.org/shub/SofianeB/singularity-recipes/ml/2021-02-24-522d5c33-259fe9ef/Singularity
collection: statiksof/singularity-recipes
---

# SofianeB/singularity-recipes:ml

```bash
$ singularity pull shub://SofianeB/singularity-recipes:ml
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.6.14

%labels
MAINTAINER SofianeB

%environment    
    # conda
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
    unset CONDA_DEFAULT_ENV
    export ANACONDA_HOME=/opt/conda


%post
    # update and install pip
    apt-get -y update

    # clean apt
    apt-get autoremove -y
    apt-get clean

    # install packages
    export PATH=/opt/conda/bin:$PATH
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda install --yes jupyter
    conda install --yes jupyterlab
    conda install --yes intake-esm
    conda clean --index-cache --tarballs --packages --yes

%runscript
    echo "Starting the notebook ..."
    echo "Open browser to localhost:8888"
    exec /opt/conda/bin/jupyter notebook --ip='*' --port=8888 --no-browser
```

## Collection

 - Name: [SofianeB/singularity-recipes](https://github.com/SofianeB/singularity-recipes)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

