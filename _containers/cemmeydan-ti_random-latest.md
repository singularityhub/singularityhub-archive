---
id: 8201
name: "cemmeydan/ti_random"
branch: "master"
tag: "latest"
commit: "7f7d8141e8b27744d33f89db621c1ae9fa01f1a1"
version: "36207a5ea4e5015a00d336a52d500e99"
build_date: "2019-04-04T22:58:11.561Z"
size_mb: 2149
size: 824647711
sif: "https://datasets.datalad.org/shub/cemmeydan/ti_random/latest/2019-04-04-7f7d8141-36207a5e/36207a5ea4e5015a00d336a52d500e99.simg"
url: https://datasets.datalad.org/shub/cemmeydan/ti_random/latest/2019-04-04-7f7d8141-36207a5e/
recipe: https://datasets.datalad.org/shub/cemmeydan/ti_random/latest/2019-04-04-7f7d8141-36207a5e/Singularity
collection: cemmeydan/ti_random
---

# cemmeydan/ti_random:latest

```bash
$ singularity pull shub://cemmeydan/ti_random:latest
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
    version 0.1.5


    
    
    
    
    

%files

    . /code

%post
    mkdir /scratchLocal
    mkdir /pbtech_mounts
    mkdir /pbtech_mounts/softlib001
    mkdir /athena
    mkdir /zenodotus



    chmod -R 755 '/code'

%runscript
    exec Rscript /code/run.R
```

## Collection

 - Name: [cemmeydan/ti_random](https://github.com/cemmeydan/ti_random)
 - License: None
