---
id: 8166
name: "cemmeydan/ti_celltree_gibbs"
branch: "master"
tag: "latest"
commit: "0fa1ea208ce5ae743976d2ec4b354402e008a361"
version: "e71ffd7725145a433c73a63c7dc8e8ca"
build_date: "2019-04-04T22:58:11.977Z"
size_mb: 2275
size: 874479647
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_celltree_gibbs/latest/2019-04-04-0fa1ea20-e71ffd77/e71ffd7725145a433c73a63c7dc8e8ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_celltree_gibbs/latest/2019-04-04-0fa1ea20-e71ffd77/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_celltree_gibbs/latest/2019-04-04-0fa1ea20-e71ffd77/Singularity
collection: cemmeydan/ti_celltree_gibbs
---

# cemmeydan/ti_celltree_gibbs:latest

```bash
$ singularity pull shub://cemmeydan/ti_celltree_gibbs:latest
```

## Singularity Recipe

```singularity
#######################################################################################
## DO NOT EDIT THIS FILE! This file was automatically generated from the dockerfile. ##
## Run dynwrap:::.container_dockerfile_to_singularityrecipe() to update this file.   ##
#######################################################################################

Bootstrap: shub

From: dynverse/dynwrap:bioc

%labels
    version 0.1.0

%post
    apt-get install -y libgsl-dev
    R -e 'devtools::install_cran("cellTree")'

%files
    . /code

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [cemmeydan/ti_celltree_gibbs](https://github.com/cemmeydan/ti_celltree_gibbs)
 - License: None

