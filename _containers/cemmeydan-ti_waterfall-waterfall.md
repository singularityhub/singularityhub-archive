---
id: 8160
name: "cemmeydan/ti_waterfall"
branch: "master"
tag: "waterfall"
commit: "62b7c1b52047bfef82ec7f77bc5804bca2d9d810"
version: "78996a006bd4f46db67f869d9cafcd0d"
build_date: "2019-04-04T22:58:11.655Z"
size_mb: 2523
size: 930865183
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_waterfall/waterfall/2019-04-04-62b7c1b5-78996a00/78996a006bd4f46db67f869d9cafcd0d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_waterfall/waterfall/2019-04-04-62b7c1b5-78996a00/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_waterfall/waterfall/2019-04-04-62b7c1b5-78996a00/Singularity
collection: cemmeydan/ti_waterfall
---

# cemmeydan/ti_waterfall:waterfall

```bash
$ singularity pull shub://cemmeydan/ti_waterfall:waterfall
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
    wget http://www.cell.com/cms/attachment/2038326541/2052521637/mmc9.zip && unzip mmc9.zip
    apt-get install -y libcgal-dev libglu1-mesa-dev libglu1-mesa-dev
    R -e 'devtools::install_cran(c("matrixStats", "rgl", "pheatmap", "limma", "MASS", "ape", "RColorBrewer"))'
    R -e 'devtools::install_github("rcannood/RHmm")'

%files
    . /code

%runscript
    exec /code/run.sh
```

## Collection

 - Name: [cemmeydan/ti_waterfall](https://github.com/cemmeydan/ti_waterfall)
 - License: None

