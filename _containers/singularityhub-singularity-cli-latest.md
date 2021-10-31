---
id: 3121
name: "singularityhub/singularity-cli"
branch: "master"
tag: "latest"
commit: "7b430f5ca90eb311f46a0f7f913e1ac86c3d691d"
version: "79e9e2c960494c898636b539e2463478"
build_date: "2020-11-17T17:07:30.926Z"
size_mb: 461
size: 180199455
sif: "https://datasets.datalad.org/shub/singularityhub/singularity-cli/latest/2020-11-17-7b430f5c-79e9e2c9/79e9e2c960494c898636b539e2463478.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/singularityhub/singularity-cli/latest/2020-11-17-7b430f5c-79e9e2c9/
recipe: https://datasets.datalad.org/shub/singularityhub/singularity-cli/latest/2020-11-17-7b430f5c-79e9e2c9/Singularity
collection: singularityhub/singularity-cli
---

# singularityhub/singularity-cli:latest

```bash
$ singularity pull shub://singularityhub/singularity-cli:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%runscript
    exec /opt/conda/bin/spython "$@"

%labels
    maintainer vsochat@stanford.edu

%post
    apt-get update && apt-get install -y git

# Dependencies
    cd /opt
    git clone https://www.github.com/singularityhub/singularity-cli
    cd singularity-cli
    /opt/conda/bin/pip install setuptools
    /opt/conda/bin/python setup.py install
```

## Collection

 - Name: [singularityhub/singularity-cli](https://github.com/singularityhub/singularity-cli)
 - License: [GNU Affero General Public License v3.0](https://api.github.com/licenses/agpl-3.0)

