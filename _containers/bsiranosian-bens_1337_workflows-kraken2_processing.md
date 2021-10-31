---
id: 9892
name: "bsiranosian/bens_1337_workflows"
branch: "master"
tag: "kraken2_processing"
commit: "e2af0cef1a301986b5f683c971eb56c0793a2882"
version: "12e35e20b488388248ab7c25db33cf33"
build_date: "2020-01-27T04:49:00.386Z"
size_mb: 2171
size: 963723295
sif: "https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/kraken2_processing/2020-01-27-e2af0cef-12e35e20/12e35e20b488388248ab7c25db33cf33.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bsiranosian/bens_1337_workflows/kraken2_processing/2020-01-27-e2af0cef-12e35e20/
recipe: https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/kraken2_processing/2020-01-27-e2af0cef-12e35e20/Singularity
collection: bsiranosian/bens_1337_workflows
---

# bsiranosian/bens_1337_workflows:kraken2_processing

```bash
$ singularity pull shub://bsiranosian/bens_1337_workflows:kraken2_processing
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04


# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"

%post 
    apt-get update
    apt-get install -y locales wget build-essential libicu-dev

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    conda install -y -c conda-forge -c r r-ggplot2 r-ggpubr r-rcolorbrewer r-reshape2 r-vegan r-stringi 

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bens_1337_workflows](https://github.com/bsiranosian/bens_1337_workflows)
 - License: None

