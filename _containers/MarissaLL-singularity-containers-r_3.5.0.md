---
id: 4653
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "r_3.5.0"
commit: "5b5a2e264c6b4cc2aded70eff4edaa661c63c21d"
version: "f713cf93d67765d2d37eb87339495de5"
build_date: "2019-10-07T00:05:40.847Z"
size_mb: 2021
size: 730239007
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/r_3.5.0/2019-10-07-5b5a2e26-f713cf93/f713cf93d67765d2d37eb87339495de5.simg"
url: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/r_3.5.0/2019-10-07-5b5a2e26-f713cf93/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/r_3.5.0/2019-10-07-5b5a2e26-f713cf93/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:r_3.5.0

```bash
$ singularity pull shub://MarissaLL/singularity-containers:r_3.5.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2:R3.5.0_Bioc3.7

%help

    R 3.5.0 with Bioconductor 3.7
    
%labels

    MAINTAINER "Marissa Le Lec"
    VERSION "Bioconductor 3.7"

%post
    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        BiocInstaller::biocLite(c( \
            'adegenet', \
            'boa', \
            'coda', \
            'data.table', \
            'ggmap', \
            'ggridges', \
            'grid', \
            'gtable', \
            'maps', \
            'reshape2', \
            'scales', \
            'SNPRelate', \
            'tidyverse' \
            ), \
        type='source', ask=FALSE)"

%runscript

    exec /usr/local/bin/R "$@"
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

