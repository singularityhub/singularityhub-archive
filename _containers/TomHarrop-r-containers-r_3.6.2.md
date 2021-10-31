---
id: 12012
name: "TomHarrop/r-containers"
branch: "master"
tag: "r_3.6.2"
commit: "5eb2eca6057d9a6ec27ae3f7f9e58b518e4172cb"
version: "8fd1c7b3aadf247212f012dd10b63cb9010a5c18c22425bf70b9e5d3d80df14c"
build_date: "2021-03-01T03:47:16.213Z"
size_mb: 1203.390625
size: 1261846528
sif: "https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.2/2021-03-01-5eb2eca6-8fd1c7b3/8fd1c7b3aadf247212f012dd10b63cb9010a5c18c22425bf70b9e5d3d80df14c.sif"
url: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.2/2021-03-01-5eb2eca6-8fd1c7b3/
recipe: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_3.6.2/2021-03-01-5eb2eca6-8fd1c7b3/Singularity
collection: TomHarrop/r-containers
---

# TomHarrop/r-containers:r_3.6.2

```bash
$ singularity pull shub://TomHarrop/r-containers:r_3.6.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.6.2

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

