---
id: 4513
name: "dynverse/ti_recat"
branch: "master"
tag: "latest"
commit: "c99b687b3f26437f8f1efbb2330c4e358bcaf864"
version: "393029cbaec7114a8915cf526a56e3f9"
build_date: "2018-10-29T20:59:12.806Z"
size_mb: 2104
size: 817238047
sif: "https://datasets.datalad.org/shub/dynverse/ti_recat/latest/2018-10-29-c99b687b-393029cb/393029cbaec7114a8915cf526a56e3f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/ti_recat/latest/2018-10-29-c99b687b-393029cb/
recipe: https://datasets.datalad.org/shub/dynverse/ti_recat/latest/2018-10-29-c99b687b-393029cb/Singularity
collection: dynverse/ti_recat
---

# dynverse/ti_recat:latest

```bash
$ singularity pull shub://dynverse/ti_recat:latest
```

## Singularity Recipe

```singularity
#######################################################################################
## DO NOT EDIT THIS FILE! This file was automatically generated from the dockerfile. ##
## Run babelwhale::convert_dockerfile_to_singularityrecipe() to update this file.    ##
#######################################################################################

Bootstrap: shub

From: dynverse/dynwrap:r

%labels
    version 0.1.4

%files
    . /code

%post
    chmod -R 755 '/code'
    R -e 'devtools::install_github("dynverse/reCAT")'

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [dynverse/ti_recat](https://github.com/dynverse/ti_recat)
 - License: None

