---
id: 4939
name: "dynverse/ti_paga_tree"
branch: "master"
tag: "latest"
commit: "d70d27f9bf22facc8ec1763c8d748fdb1e92da38"
version: "f09019fc944f125cee9ea79f213413c3"
build_date: "2020-10-15T14:07:41.894Z"
size_mb: 1545
size: 591712287
sif: "https://datasets.datalad.org/shub/dynverse/ti_paga_tree/latest/2020-10-15-d70d27f9-f09019fc/f09019fc944f125cee9ea79f213413c3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/ti_paga_tree/latest/2020-10-15-d70d27f9-f09019fc/
recipe: https://datasets.datalad.org/shub/dynverse/ti_paga_tree/latest/2020-10-15-d70d27f9-f09019fc/Singularity
collection: dynverse/ti_paga_tree
---

# dynverse/ti_paga_tree:latest

```bash
$ singularity pull shub://dynverse/ti_paga_tree:latest
```

## Singularity Recipe

```singularity
#######################################################################################
## DO NOT EDIT THIS FILE! This file was automatically generated from the dockerfile. ##
## Run babelwhale::convert_dockerfile_to_singularityrecipe() to update this file.    ##
#######################################################################################

Bootstrap: shub

From: dynverse/dynwrap:py3.6

%labels
    version 0.1.5

%files
    . /code

%post
    chmod -R 755 '/code'
    pip install python-igraph louvain 
    pip install scanpy
    pip install fa2

%runscript
    exec python /code/run.py
```

## Collection

 - Name: [dynverse/ti_paga_tree](https://github.com/dynverse/ti_paga_tree)
 - License: None

