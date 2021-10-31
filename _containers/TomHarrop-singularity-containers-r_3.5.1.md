---
id: 4892
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "r_3.5.1"
commit: "6fa6a4a5a2b6da669923db2a3b8a0bb3f876003c"
version: "5cb3d63cbffa61bf80f532997f31859f"
build_date: "2018-09-28T05:14:35.569Z"
size_mb: 2471
size: 918769695
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.1/2018-09-28-6fa6a4a5-5cb3d63c/5cb3d63cbffa61bf80f532997f31859f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/r_3.5.1/2018-09-28-6fa6a4a5-5cb3d63c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.1/2018-09-28-6fa6a4a5-5cb3d63c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:r_3.5.1

```bash
$ singularity pull shub://TomHarrop/singularity-containers:r_3.5.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.5.1

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.5.1"

%post

    # install depenedencies
    apt-get update
    apt-get install -y \
        libbz2-dev \
        liblzma-dev \
        libpcre++-dev 

    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        source('https://bioconductor.org/biocLite.R') ; \
        biocLite(c(\
            'Cairo', \
            'data.table', \
            'extrafont', \
            'ggimage', \
            'ggtree', \
            'UpSetR', \
            'sysfonts', \
            'VennDiagram'), \
            type='source', ask=FALSE)"

    # install lato
    wget -O "lato.zip" \
        http://www.latofonts.com/download/Lato2OFL.zip
    unzip lato.zip
    mv Lato2OFL /usr/share/fonts/truetype/
    rm lato.zip
    fc-cache -f -v
    Rscript -e "library('extrafont') ; \
        font_import(prompt=FALSE) ; \
        loadfonts()"

%runscript

    exec /usr/local/bin/R "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

