---
id: 4263
name: "dynverse/dynwrap_tester"
branch: "devel"
tag: "r_rds"
commit: "05cae27f8a9c751b5e91bbf2bbb5e0a3f511e5a2"
version: "03c3125a4c8d6f6e0c78b1d125e8a7bf"
build_date: "2018-10-29T20:59:11.181Z"
size_mb: 2095
size: 807579679
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap_tester/r_rds/2018-10-29-05cae27f-03c3125a/03c3125a4c8d6f6e0c78b1d125e8a7bf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/dynwrap_tester/r_rds/2018-10-29-05cae27f-03c3125a/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap_tester/r_rds/2018-10-29-05cae27f-03c3125a/Singularity
collection: dynverse/dynwrap_tester
---

# dynverse/dynwrap_tester:r_rds

```bash
$ singularity pull shub://dynverse/dynwrap_tester:r_rds
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
    version 0.2.0.1

%files
    . /code

%post
    chmod -R 755 '/code'

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [dynverse/dynwrap_tester](https://github.com/dynverse/dynwrap_tester)
 - License: None

