---
id: 8192
name: "cemmeydan/ti_forks"
branch: "master"
tag: "forks"
commit: "4f3e85f0c3cc8d97fefd56a810cc8706f1f94568"
version: "f90b98ca8c2bc1c7cef705b48b8021dd"
build_date: "2019-04-04T22:58:11.724Z"
size_mb: 1408
size: 537624607
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_forks/forks/2019-04-04-4f3e85f0-f90b98ca/f90b98ca8c2bc1c7cef705b48b8021dd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_forks/forks/2019-04-04-4f3e85f0-f90b98ca/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_forks/forks/2019-04-04-4f3e85f0-f90b98ca/Singularity
collection: cemmeydan/ti_forks
---

# cemmeydan/ti_forks:forks

```bash
$ singularity pull shub://cemmeydan/ti_forks:forks
```

## Singularity Recipe

```singularity
########################################################################
##                      DO NOT EDIT THIS FILE!                        ##
##     This file was automatically generated from the dockerfile.     ##
## Run dynmethods/data-raw/convert_dockerfiles.R to update this file. ##
########################################################################

Bootstrap: shub

From: dynverse/dynwrap:py3.6

%labels
    version 0.1.0.1

%post
    pip install seaborn hdbscan
    git clone https://github.com/macsharma/FORKS.git

%files
    . /code

%runscript
    exec /code/run.sh
```

## Collection

 - Name: [cemmeydan/ti_forks](https://github.com/cemmeydan/ti_forks)
 - License: None

