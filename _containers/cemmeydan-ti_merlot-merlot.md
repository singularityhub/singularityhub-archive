---
id: 8208
name: "cemmeydan/ti_merlot"
branch: "master"
tag: "merlot"
commit: "f68f41718d91f028e3b41b75675e81329af6cf43"
version: "3fa9a6ef988f0a5b25084f83ad9fae8e"
build_date: "2019-04-04T22:58:11.755Z"
size_mb: 2783
size: 1017860127
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_merlot/merlot/2019-04-04-f68f4171-3fa9a6ef/3fa9a6ef988f0a5b25084f83ad9fae8e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_merlot/merlot/2019-04-04-f68f4171-3fa9a6ef/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_merlot/merlot/2019-04-04-f68f4171-3fa9a6ef/Singularity
collection: cemmeydan/ti_merlot
---

# cemmeydan/ti_merlot:merlot

```bash
$ singularity pull shub://cemmeydan/ti_merlot:merlot
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
    R -e 'devtools::install_cran("destiny")'
    apt-get update && apt-get install -y libcgal-dev libglu1-mesa-dev libglu1-mesa-dev
    apt-get install -y python3 python3-tk python3-pip
    apt-get install -y python3-scipy python3-numpy python3-pandas
    pip3 install cython
    pip3 install git+https://github.com/soedinglab/csgraph_mod
    apt-get -y install libudunits2-dev
    Rscript -e 'devtools::install_cran("udunits2", configure.args =  c(udunits2 = "--with-udunits2-include=/usr/include/udunits2"))'
    R -e "devtools::install_github('soedinglab/merlot')"

%files
    . /code

%runscript
    exec /code/run.sh
```

## Collection

 - Name: [cemmeydan/ti_merlot](https://github.com/cemmeydan/ti_merlot)
 - License: None

