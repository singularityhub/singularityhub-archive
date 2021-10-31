---
id: 10031
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "pengu-ddt"
commit: "8e9a5b29d032a207f6728d528a165e4969182aed"
version: "75c56c12e284e7c74eb7d78911b73147"
build_date: "2019-06-25T18:43:26.702Z"
size_mb: 709
size: 282697759
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/pengu-ddt/2019-06-25-8e9a5b29-75c56c12/75c56c12e284e7c74eb7d78911b73147.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/pengu-ddt/2019-06-25-8e9a5b29-75c56c12/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/pengu-ddt/2019-06-25-8e9a5b29-75c56c12/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:pengu-ddt

```bash
$ singularity pull shub://connor-lab/singularity-recipes:pengu-ddt
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:latest

%post
    apt-get -y update && apt-get -y upgrade
    apt-get install -y git make python3-pip

    pip3 install git+https://github.com/connor-lab/pengu-ddt

%runscript
    exec pengu-ddt "$@"

%labels
    Maintainer m-bull
    Version pengu-ddt-0.1
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

