---
id: 4264
name: "dynverse/dynwrap_tester"
branch: "devel"
tag: "r_text"
commit: "b8ae412e759b7a5be45559b61cd615b67566f7fe"
version: "f9d1dbe79456ca141b88975b7d6eb263"
build_date: "2018-10-29T20:59:11.194Z"
size_mb: 2093
size: 806367263
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap_tester/r_text/2018-10-29-b8ae412e-f9d1dbe7/f9d1dbe79456ca141b88975b7d6eb263.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/dynwrap_tester/r_text/2018-10-29-b8ae412e-f9d1dbe7/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap_tester/r_text/2018-10-29-b8ae412e-f9d1dbe7/Singularity
collection: dynverse/dynwrap_tester
---

# dynverse/dynwrap_tester:r_text

```bash
$ singularity pull shub://dynverse/dynwrap_tester:r_text
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

