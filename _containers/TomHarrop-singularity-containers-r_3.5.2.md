---
id: 6774
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "r_3.5.2"
commit: "ab0dfe940f1c57cacc6f7b0f0588e5fa0b560f54"
version: "f4e1feb1a9776e3e255c8fafeb033219"
build_date: "2019-02-01T14:00:53.188Z"
size_mb: 2510
size: 940613663
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.2/2019-02-01-ab0dfe94-f4e1feb1/f4e1feb1a9776e3e255c8fafeb033219.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/r_3.5.2/2019-02-01-ab0dfe94-f4e1feb1/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.2/2019-02-01-ab0dfe94-f4e1feb1/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:r_3.5.2

```bash
$ singularity pull shub://TomHarrop/singularity-containers:r_3.5.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.5.2

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.5.2"

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
            'cowplot', \
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

