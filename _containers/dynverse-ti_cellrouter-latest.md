---
id: 4433
name: "dynverse/ti_cellrouter"
branch: "master"
tag: "latest"
commit: "1951e185715945951902089832b345d3b8403017"
version: "0161593f461a9aad1525a2bdb75daeff"
build_date: "2018-11-12T16:21:16.831Z"
size_mb: 2437
size: 938475551
sif: "https://datasets.datalad.org/shub/dynverse/ti_cellrouter/latest/2018-11-12-1951e185-0161593f/0161593f461a9aad1525a2bdb75daeff.simg"
url: https://datasets.datalad.org/shub/dynverse/ti_cellrouter/latest/2018-11-12-1951e185-0161593f/
recipe: https://datasets.datalad.org/shub/dynverse/ti_cellrouter/latest/2018-11-12-1951e185-0161593f/Singularity
collection: dynverse/ti_cellrouter
---

# dynverse/ti_cellrouter:latest

```bash
$ singularity pull shub://dynverse/ti_cellrouter:latest
```

## Singularity Recipe

```singularity
#######################################################################################
## DO NOT EDIT THIS FILE! This file was automatically generated from the dockerfile. ##
## Run babelwhale::convert_dockerfile_to_singularityrecipe() to update this file.    ##
#######################################################################################

Bootstrap: shub

From: dynverse/dynwrap:bioc

%labels
    version 0.1.8

%files
    . /code

%post
    chmod -R 755 '/code'
    R -e 'devtools::install_cran(c("reshape", "reshape2", "pheatmap", "tsne", "igraph", "ggplot2", "mclust", "Rtsne", "cccd", "irlba"))'
    git clone https://github.com/edroaldo/cellrouter.git && find cellrouter -type f | grep -v "^cellrouter/CellRouter" | xargs rm
    apt-get update && apt-get install -y default-jre

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [dynverse/ti_cellrouter](https://github.com/dynverse/ti_cellrouter)
 - License: None
