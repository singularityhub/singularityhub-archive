---
id: 4535
name: "dynverse/ti_tscan"
branch: "master"
tag: "latest"
commit: "d1bebf72f651229e67d19fd7a064c53321a77ffe"
version: "c3df39df892106c4b2849e087280bd40"
build_date: "2019-01-16T07:21:13.011Z"
size_mb: 2109
size: 821710879
sif: "https://datasets.datalad.org/shub/dynverse/ti_tscan/latest/2019-01-16-d1bebf72-c3df39df/c3df39df892106c4b2849e087280bd40.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/ti_tscan/latest/2019-01-16-d1bebf72-c3df39df/
recipe: https://datasets.datalad.org/shub/dynverse/ti_tscan/latest/2019-01-16-d1bebf72-c3df39df/Singularity
collection: dynverse/ti_tscan
---

# dynverse/ti_tscan:latest

```bash
$ singularity pull shub://dynverse/ti_tscan:latest
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
    version 0.1.5

%files
    . /code

%post
    chmod -R 755 '/code'
    R -e 'devtools::install_cran("TSCAN")'

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [dynverse/ti_tscan](https://github.com/dynverse/ti_tscan)
 - License: None

