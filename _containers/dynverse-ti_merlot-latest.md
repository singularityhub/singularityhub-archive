---
id: 4470
name: "dynverse/ti_merlot"
branch: "master"
tag: "latest"
commit: "2d6fb37a5ea75dbd9108d3bc3b0510f910cef19a"
version: "c6498723ac0fc6e4c6cf54c894dd9804"
build_date: "2018-10-29T20:59:12.585Z"
size_mb: 2717
size: 1003900959
sif: "https://datasets.datalad.org/shub/dynverse/ti_merlot/latest/2018-10-29-2d6fb37a-c6498723/c6498723ac0fc6e4c6cf54c894dd9804.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/ti_merlot/latest/2018-10-29-2d6fb37a-c6498723/
recipe: https://datasets.datalad.org/shub/dynverse/ti_merlot/latest/2018-10-29-2d6fb37a-c6498723/Singularity
collection: dynverse/ti_merlot
---

# dynverse/ti_merlot:latest

```bash
$ singularity pull shub://dynverse/ti_merlot:latest
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
    version 0.1.4

%files
    . /code

%post
    chmod -R 755 '/code'
    R -e 'devtools::install_cran("destiny")'
    apt-get update && apt-get install -y libcgal-dev libglu1-mesa-dev libglu1-mesa-dev
    apt-get install -y python3 python3-tk python3-pip
    apt-get install -y python3-scipy python3-numpy python3-pandas
    pip3 install cython
    pip3 install git+https://github.com/soedinglab/csgraph_mod
    apt-get -y install libudunits2-dev
    Rscript -e 'devtools::install_cran("udunits2", configure.args =  c(udunits2 = "--with-udunits2-include=/usr/include/udunits2"))'
    R -e "devtools::install_github('soedinglab/merlot')"

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [dynverse/ti_merlot](https://github.com/dynverse/ti_merlot)
 - License: None

