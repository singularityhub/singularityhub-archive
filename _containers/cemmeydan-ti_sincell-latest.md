---
id: 8157
name: "cemmeydan/ti_sincell"
branch: "master"
tag: "latest"
commit: "31e95062af7cbff427d1abe4c68aef21f7e63b6f"
version: "7c9fc45b732c0ae73c08409cca340eb8"
build_date: "2019-04-04T22:58:11.677Z"
size_mb: 2168
size: 838688799
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_sincell/latest/2019-04-04-31e95062-7c9fc45b/7c9fc45b732c0ae73c08409cca340eb8.simg"
url: https://datasets.datalad.org/shub/cemmeydan/ti_sincell/latest/2019-04-04-31e95062-7c9fc45b/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_sincell/latest/2019-04-04-31e95062-7c9fc45b/Singularity
collection: cemmeydan/ti_sincell
---

# cemmeydan/ti_sincell:latest

```bash
$ singularity pull shub://cemmeydan/ti_sincell:latest
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
    mkdir /scratchLocal
    mkdir /pbtech_mounts
    mkdir /pbtech_mounts/softlib001
    mkdir /athena
    mkdir /zenodotus



    chmod -R 755 '/code'
    R -e 'devtools::install_cran("sincell")'

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [cemmeydan/ti_sincell](https://github.com/cemmeydan/ti_sincell)
 - License: None
