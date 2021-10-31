---
id: 11719
name: "TomHarrop/r-containers"
branch: "master"
tag: "r_3.6.1"
commit: "e1eb426cd153fd0669bc24508673228d2f25dd76"
version: "81564080ee7be3b52f48d98449208a143012a9f196ad9b9d60810acd1868c6f8"
build_date: "2020-04-20T01:05:39.141Z"
size_mb: 958.58984375
size: 1005154304
sif: "https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.1/2020-04-20-e1eb426c-81564080/81564080ee7be3b52f48d98449208a143012a9f196ad9b9d60810acd1868c6f8.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/r-containers/r_3.6.1/2020-04-20-e1eb426c-81564080/
recipe: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.1/2020-04-20-e1eb426c-81564080/Singularity
collection: TomHarrop/r-containers
---

# TomHarrop/r-containers:r_3.6.1

```bash
$ singularity pull shub://TomHarrop/r-containers:r_3.6.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.6.1

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.6.1"

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

 - Name: [TomHarrop/r-containers](https://github.com/TomHarrop/r-containers)
 - License: None

