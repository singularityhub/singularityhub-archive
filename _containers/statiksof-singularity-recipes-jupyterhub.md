---
id: 14431
name: "statiksof/singularity-recipes"
branch: "master"
tag: "jupyterhub"
commit: "45f866edab148aab0a8b998c6c7bbc8ed40a7d07"
version: "f94d23290362432abaaa666f0b20e7827e70dc7115f3e37146807d7aed30a792"
build_date: "2020-11-19T14:21:34.836Z"
size_mb: 505.0
size: 529530880
sif: "https://datasets.datalad.org/shub/statiksof/singularity-recipes/jupyterhub/2020-11-19-45f866ed-f94d2329/f94d23290362432abaaa666f0b20e7827e70dc7115f3e37146807d7aed30a792.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/statiksof/singularity-recipes/jupyterhub/2020-11-19-45f866ed-f94d2329/
recipe: https://datasets.datalad.org/shub/statiksof/singularity-recipes/jupyterhub/2020-11-19-45f866ed-f94d2329/Singularity
collection: statiksof/singularity-recipes
---

# statiksof/singularity-recipes:jupyterhub

```bash
$ singularity pull shub://statiksof/singularity-recipes:jupyterhub
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
    conda config --add channels conda-forge
    conda install --yes \
                 jupyterhub \
                 jupyter \
                 jupyterlab \
                 xarray \
                 dask==2.29.0 \
                 netcdf4 \
                 matplotlib \
                 intake-esm 
    conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [statiksof/singularity-recipes](https://github.com/statiksof/singularity-recipes)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

