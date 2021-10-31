---
id: 3229
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "r_3.5.0"
commit: "ec5fffa2069e1657ee57d416828956f3f0c34eb9"
version: "7322eba66379576b4a0a426070a5103d"
build_date: "2021-03-06T01:06:33.348Z"
size_mb: 2501
size: 956510239
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.0/2021-03-06-ec5fffa2-7322eba6/7322eba66379576b4a0a426070a5103d.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.0/2021-03-06-ec5fffa2-7322eba6/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r_3.5.0/2021-03-06-ec5fffa2-7322eba6/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:r_3.5.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:r_3.5.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.5.0

%help

    Container for plotting with R data.table and ggplot2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.5.0"

%post

    # install packages from bioconductor
    Rscript -e "source('https://bioconductor.org/biocLite.R') ; \
        biocLite(c('Cairo', 'data.table', 'extrafont', 'ggimage', 'ggtree', 'sysfonts'), \
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
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

