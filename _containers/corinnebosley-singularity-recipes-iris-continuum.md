---
id: 1063
name: "corinnebosley/singularity-recipes"
branch: "master"
tag: "iris-continuum"
commit: "9a2de3db0ec0dba5fcec1ac429a4a00a3bdd4891"
version: "2e57dc4e1b58dda4821c174aeff3b26e"
build_date: "2020-06-19T10:49:53.786Z"
size_mb: 600
size: 260161567
sif: "https://datasets.datalad.org/shub/corinnebosley/singularity-recipes/iris-continuum/2020-06-19-9a2de3db-2e57dc4e/2e57dc4e1b58dda4821c174aeff3b26e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/corinnebosley/singularity-recipes/iris-continuum/2020-06-19-9a2de3db-2e57dc4e/
recipe: https://datasets.datalad.org/shub/corinnebosley/singularity-recipes/iris-continuum/2020-06-19-9a2de3db-2e57dc4e/Singularity
collection: corinnebosley/singularity-recipes
---

# corinnebosley/singularity-recipes:iris-continuum

```bash
$ singularity pull shub://corinnebosley/singularity-recipes:iris-continuum
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda3:latest

%runscript
exec conda install --yes -c conda-forge iris
```

## Collection

 - Name: [corinnebosley/singularity-recipes](https://github.com/corinnebosley/singularity-recipes)
 - License: None

