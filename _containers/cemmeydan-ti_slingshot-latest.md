---
id: 8144
name: "cemmeydan/ti_slingshot"
branch: "master"
tag: "latest"
commit: "8f19d593f428eb65d32139d9443f567a22c51731"
version: "e1285afb8440b496e6aba34835dbb7e8"
build_date: "2019-04-04T22:58:11.893Z"
size_mb: 2636
size: 975564831
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_slingshot/latest/2019-04-04-8f19d593-e1285afb/e1285afb8440b496e6aba34835dbb7e8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cemmeydan/ti_slingshot/latest/2019-04-04-8f19d593-e1285afb/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_slingshot/latest/2019-04-04-8f19d593-e1285afb/Singularity
collection: cemmeydan/ti_slingshot
---

# cemmeydan/ti_slingshot:latest

```bash
$ singularity pull shub://cemmeydan/ti_slingshot:latest
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
    version 0.1.5.2

%files
    . /code

%post
    mkdir /scratchLocal
    mkdir /pbtech_mounts
    mkdir /pbtech_mounts/softlib001
    mkdir /athena
    mkdir /zenodotus
    chmod -R 755 '/code'
    apt-get update && apt-get install -y libcgal-dev libglu1-mesa-dev libgsl-dev
    R -e 'devtools::install_github("kstreet13/slingshot")'

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [cemmeydan/ti_slingshot](https://github.com/cemmeydan/ti_slingshot)
 - License: None

