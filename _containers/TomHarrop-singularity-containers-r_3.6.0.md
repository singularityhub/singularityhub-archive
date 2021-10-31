---
id: 9508
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "r_3.6.0"
commit: "e71b430165a96710a90a31ead095fbc62aa5242b"
version: "3288f13ec7a41862f4e1f99779cb51e6"
build_date: "2020-04-30T23:15:48.265Z"
size_mb: 2810
size: 991764511
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.6.0/2020-04-30-e71b4301-3288f13e/3288f13ec7a41862f4e1f99779cb51e6.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.6.0/2020-04-30-e71b4301-3288f13e/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.6.0/2020-04-30-e71b4301-3288f13e/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:r_3.6.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:r_3.6.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.6.0

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.6.0"

%post

    # install depenedencies
    apt-get update
    apt-get install -y \
        libbz2-dev \
        liblzma-dev \
        libpcre++-dev 

    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        install.packages('BiocManager') ; \
        BiocManager::install(c(\
            'Cairo', \
            'cowplot', \
            'data.table', \
            'extrafont', \
            'ggimage', \
            'ggtree', \
            'hexbin', \
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

