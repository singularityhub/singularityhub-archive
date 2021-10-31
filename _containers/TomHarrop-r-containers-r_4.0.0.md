---
id: 14000
name: "TomHarrop/r-containers"
branch: "master"
tag: "r_4.0.0"
commit: "64533be48d00c2dc09c91a5d9b920b6d044fe69f"
version: "dd452567223dbe49843ee57c831898710bf57cdb61c931f3b8ec6d4030c8f300"
build_date: "2020-11-30T22:26:35.877Z"
size_mb: 1244.56640625
size: 1305022464
sif: "https://datasets.datalad.org/shub/TomHarrop/r-containers/r_4.0.0/2020-11-30-64533be4-dd452567/dd452567223dbe49843ee57c831898710bf57cdb61c931f3b8ec6d4030c8f300.sif"
url: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_4.0.0/2020-11-30-64533be4-dd452567/
recipe: https://datasets.datalad.org/shub/TomHarrop/r-containers/r_4.0.0/2020-11-30-64533be4-dd452567/Singularity
collection: TomHarrop/r-containers
---

# TomHarrop/r-containers:r_4.0.0

```bash
$ singularity pull shub://TomHarrop/r-containers:r_4.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:4.0.0

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 4.0.0"

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
            'circlize', \
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

