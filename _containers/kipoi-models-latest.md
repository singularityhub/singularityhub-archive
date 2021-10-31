---
id: 5680
name: "kipoi/models"
branch: "master"
tag: "latest"
commit: "b94a8e5e1d2c783409179497810c3f524101be1e"
version: "3b2f5b5b05f8a28b2d4ad63d0bf27e40"
build_date: "2020-11-12T16:34:57.261Z"
size_mb: 8101
size: 2488463391
sif: "https://datasets.datalad.org/shub/kipoi/models/latest/2020-11-12-b94a8e5e-3b2f5b5b/3b2f5b5b05f8a28b2d4ad63d0bf27e40.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kipoi/models/latest/2020-11-12-b94a8e5e-3b2f5b5b/
recipe: https://datasets.datalad.org/shub/kipoi/models/latest/2020-11-12-b94a8e5e-3b2f5b5b/Singularity
collection: kipoi/models
---

# kipoi/models:latest

```bash
$ singularity pull shub://kipoi/models:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: continuumio/miniconda3:4.5.11

# TODO - support also GPU environmnets

%help
    This container provides portable & reproducible environment for running
    Kipoi moddels.

    Please see https://github.com/kipoi/kipoi for complete documentation.

%post
    # install sys-dependencies
    apt-get update
    apt-get install -y build-essential libz-dev libcurl3-dev

    # Configure Kipoi
    export PATH=$PATH:/opt/conda/bin
    export LC_ALL=C

    # Place to store kipoi environment database
    mkdir -p /kipoi
    export KIPOI_ENV_DB_PATH=/kipoi/envs.json

    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge

    # install kipoi from the master branch for now
    # TODO - use a specific tag for the build
    pip install git+https://github.com/kipoi/kipoi

    # Create all the environments
    kipoi ls # list all environments to load the remote repo
    kipoi env create all --vep

    # add write-permission to anyone
    chmod go+r /kipoi/envs.json

    # clean packages
    conda clean --index-cache --tarballs --packages --yes

%environment
    export LC_ALL=C
    export PATH=$PATH:/opt/conda/bin

    # Move the json database to tempdir
    random_string=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo '')
    tmpdir=/tmp/kipoi/$random_string
    mkdir -p $tmpdir
    cp /kipoi/envs.json $tmpdir/envs.json
    export KIPOI_ENV_DB_PATH=$tmpdir/envs.json
    
%labels
    Maintainer avsecz
    Version v0.1
```

## Collection

 - Name: [kipoi/models](https://github.com/kipoi/models)
 - License: [MIT License](https://api.github.com/licenses/mit)

