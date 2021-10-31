---
id: 14555
name: "statiksof/singularity-recipes"
branch: "master"
tag: "ml"
commit: "e7ab4935bbffa0806fe9b23e014a73be68fee8ea"
version: "88b42cb32238a3cbb3f04d2bdbba7df5197ec3b5908fb0fc4022b79090f9bfc6"
build_date: "2020-10-06T15:11:30.276Z"
size_mb: 451.81640625
size: 473763840
sif: "https://datasets.datalad.org/shub/statiksof/singularity-recipes/ml/2020-10-06-e7ab4935-88b42cb3/88b42cb32238a3cbb3f04d2bdbba7df5197ec3b5908fb0fc4022b79090f9bfc6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/statiksof/singularity-recipes/ml/2020-10-06-e7ab4935-88b42cb3/
recipe: https://datasets.datalad.org/shub/statiksof/singularity-recipes/ml/2020-10-06-e7ab4935-88b42cb3/Singularity
collection: statiksof/singularity-recipes
---

# statiksof/singularity-recipes:ml

```bash
$ singularity pull shub://statiksof/singularity-recipes:ml
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.6.14

%labels
MAINTAINER statiksof

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

 - Name: [statiksof/singularity-recipes](https://github.com/statiksof/singularity-recipes)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

