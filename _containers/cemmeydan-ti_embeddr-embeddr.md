---
id: 8188
name: "cemmeydan/ti_embeddr"
branch: "master"
tag: "embeddr"
commit: "5b2a09ea76ad06cbb1606c5a09f4f8745d2d6172"
version: "c499e6abddced379d781c52f30680618"
build_date: "2019-04-04T22:58:11.802Z"
size_mb: 2267
size: 878194719
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_embeddr/embeddr/2019-04-04-5b2a09ea-c499e6ab/c499e6abddced379d781c52f30680618.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_embeddr/embeddr/2019-04-04-5b2a09ea-c499e6ab/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_embeddr/embeddr/2019-04-04-5b2a09ea-c499e6ab/Singularity
collection: cemmeydan/ti_embeddr
---

# cemmeydan/ti_embeddr:embeddr

```bash
$ singularity pull shub://cemmeydan/ti_embeddr:embeddr
```

## Singularity Recipe

```singularity
########################################################################
##                      DO NOT EDIT THIS FILE!                        ##
##     This file was automatically generated from the dockerfile.     ##
## Run dynmethods/data-raw/convert_dockerfiles.R to update this file. ##
########################################################################

Bootstrap: shub

From: dynverse/dynwrap:bioc

%labels
    version 0.1.0.1

%post
    R -e 'devtools::install_github("dynverse/scaterlegacy")'
    R -e 'devtools::install_github("dynverse/embeddr")'

%files
    . /code

%runscript
    exec /code/run.sh
```

## Collection

 - Name: [cemmeydan/ti_embeddr](https://github.com/cemmeydan/ti_embeddr)
 - License: None

