---
id: 8191
name: "cemmeydan/ti_forks"
branch: "master"
tag: "latest"
commit: "55c176b39dcf3c0e3b424032365b437fbd3fbbf4"
version: "c1ba7c411f1496b3d8228910562da25c"
build_date: "2019-04-04T22:58:11.730Z"
size_mb: 1408
size: 537624607
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_forks/latest/2019-04-04-55c176b3-c1ba7c41/c1ba7c411f1496b3d8228910562da25c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_forks/latest/2019-04-04-55c176b3-c1ba7c41/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_forks/latest/2019-04-04-55c176b3-c1ba7c41/Singularity
collection: cemmeydan/ti_forks
---

# cemmeydan/ti_forks:latest

```bash
$ singularity pull shub://cemmeydan/ti_forks:latest
```

## Singularity Recipe

```singularity
#######################################################################################
## DO NOT EDIT THIS FILE! This file was automatically generated from the dockerfile. ##
## Run dynwrap:::.container_dockerfile_to_singularityrecipe() to update this file.   ##
#######################################################################################

Bootstrap: shub

From: dynverse/dynwrap:py3.6

%labels
    version 0.1.0

%post
    pip install seaborn hdbscan
    git clone https://github.com/macsharma/FORKS.git

%files
    . /code

%runscript
    exec python /code/run.py
```

## Collection

 - Name: [cemmeydan/ti_forks](https://github.com/cemmeydan/ti_forks)
 - License: None

