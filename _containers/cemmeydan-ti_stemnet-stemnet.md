---
id: 8180
name: "cemmeydan/ti_stemnet"
branch: "master"
tag: "stemnet"
commit: "9a8de7be579f9d10b53dd6dd1c99806aaa2f9d56"
version: "f521bba4d2d7e15f1bfffd04e2322518"
build_date: "2019-04-04T22:58:11.924Z"
size_mb: 2257
size: 929124383
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_stemnet/stemnet/2019-04-04-9a8de7be-f521bba4/f521bba4d2d7e15f1bfffd04e2322518.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_stemnet/stemnet/2019-04-04-9a8de7be-f521bba4/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_stemnet/stemnet/2019-04-04-9a8de7be-f521bba4/Singularity
collection: cemmeydan/ti_stemnet
---

# cemmeydan/ti_stemnet:stemnet

```bash
$ singularity pull shub://cemmeydan/ti_stemnet:stemnet
```

## Singularity Recipe

```singularity
########################################################################
##                      DO NOT EDIT THIS FILE!                        ##
##     This file was automatically generated from the dockerfile.     ##
## Run dynmethods/data-raw/convert_dockerfiles.R to update this file. ##
########################################################################

Bootstrap: shub

From: dynverse/dynwrap:r

%labels
    version 0.1.0.1

%post
    apt-get install -y libgsl-dev
    R -e 'devtools::install_git("https://git.embl.de/velten/STEMNET/")'

%files
    . /code

%runscript
    exec /code/run.sh
```

## Collection

 - Name: [cemmeydan/ti_stemnet](https://github.com/cemmeydan/ti_stemnet)
 - License: None

