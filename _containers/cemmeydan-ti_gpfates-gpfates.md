---
id: 8198
name: "cemmeydan/ti_gpfates"
branch: "master"
tag: "gpfates"
commit: "db37e65d5987ebbbc87734efe06e85ad36dba2ce"
version: "435541005b3613fd46caff00f29a3769"
build_date: "2019-04-04T22:58:11.847Z"
size_mb: 1395
size: 527515679
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_gpfates/gpfates/2019-04-04-db37e65d-43554100/435541005b3613fd46caff00f29a3769.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_gpfates/gpfates/2019-04-04-db37e65d-43554100/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_gpfates/gpfates/2019-04-04-db37e65d-43554100/Singularity
collection: cemmeydan/ti_gpfates
---

# cemmeydan/ti_gpfates:gpfates

```bash
$ singularity pull shub://cemmeydan/ti_gpfates:gpfates
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
    pip install GPy
    pip install git+https://github.com/SheffieldML/GPclust.git
    pip install git+https://github.com/Teichlab/GPfates.git@bccd5496b4121b3e634ce7cd5b0bff823b2850fa

%files
    . /code

%runscript
    exec /code/run.sh
```

## Collection

 - Name: [cemmeydan/ti_gpfates](https://github.com/cemmeydan/ti_gpfates)
 - License: None

