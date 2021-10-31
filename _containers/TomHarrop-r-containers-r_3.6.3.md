---
id: 12937
name: "TomHarrop/r-containers"
branch: "master"
tag: "r_3.6.3"
commit: "3ddd6a174ed787e9bd803b971b7afc9837b4cbf1"
version: "0847e24668c6afe2dad35cebe7b71c79526f400c5554441fbcf6f907af9c0d24"
build_date: "2020-05-28T02:49:42.196Z"
size_mb: 1217.578125
size: 1276723200
sif: "https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.3/2020-05-28-3ddd6a17-0847e246/0847e24668c6afe2dad35cebe7b71c79526f400c5554441fbcf6f907af9c0d24.sif"
url: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.3/2020-05-28-3ddd6a17-0847e246/
recipe: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.3/2020-05-28-3ddd6a17-0847e246/Singularity
collection: TomHarrop/r-containers
---

# TomHarrop/r-containers:r_3.6.3

```bash
$ singularity pull shub://TomHarrop/r-containers:r_3.6.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.6.3

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.6.2"

%post

    # install dependencies
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
            'gtools', \
            'hexbin', \
            'sysfonts', \
            'UpSetR', \
            'VennDiagram', \
            'viridis'), 
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

 - Name: [TomHarrop/r-containers](https://github.com/TomHarrop/r-containers)
 - License: None

