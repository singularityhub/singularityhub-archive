---
id: 8467
name: "phelelani/transcriptomics"
branch: "master"
tag: "r"
commit: "2727089b11ee4cc02389edffc42a55d20429d7d5"
version: "d7f8bba7d0a1902f846eca9c8d0875da"
build_date: "2020-02-12T21:23:08.125Z"
size_mb: 2287
size: 880869407
sif: "https://datasets.datalad.org/shub/phelelani/transcriptomics/r/2020-02-12-2727089b-d7f8bba7/d7f8bba7d0a1902f846eca9c8d0875da.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/phelelani/transcriptomics/r/2020-02-12-2727089b-d7f8bba7/
recipe: https://datasets.datalad.org/shub/phelelani/transcriptomics/r/2020-02-12-2727089b-d7f8bba7/Singularity
collection: phelelani/transcriptomics
---

# phelelani/transcriptomics:r

```bash
$ singularity pull shub://phelelani/transcriptomics:r
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:singularityhub/ubuntu

%labels
Maintainer Phelelani.Mpangase@wits.ac.za

%post
## Updates and essentials
apt-get update
apt-get install -y build-essential
apt-get install -y wget git curl gfortran zlib1g-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-gnutls-dev
apt-get install -y libxml2-dev libssl-dev libopenblas-dev libmagick++-dev libudunits2-dev libcairo2-dev libxt-dev

## Install R
cd /opt \
    && wget https://cran.r-project.org/src/base/R-3/R-3.5.1.tar.gz \
    && tar -vxf R-3.5.1.tar.gz \
    && cd R-3.5.1 \
    && ./configure --with-x=no --with-readline=no \
    && make \
    && make install \
    && rm /opt/R-3.5.1.tar.gz

## Install basic CRAN R packages
R -e 'install.packages(c("tidyverse","data.table","dtplyr","devtools","roxygen2", "Cairo"), repos="http://cloud.r-project.org/", dependencies=TRUE)'

## Install CRAN R packages
R -e 'install.packages(c("ggplot2", "gridExtra", "ggrepel", "xtable", "gplots", "kableExtra", "grid", "pheatmap", "enrichR", "BiocManager", "UpSetR", "PoiClaClu"), repos="http://cloud.r-project.org/", dependencies=TRUE)'

## Install Bioconductor R packages
R -e 'BiocManager::install(c("DESeq2", "biomaRt", "genefilter", "AnnotationDbi", "org.Hs.eg.db", "pathview", "gage", "gageData", "PROPER"), version = "3.8")'
```

## Collection

 - Name: [phelelani/transcriptomics](https://github.com/phelelani/transcriptomics)
 - License: None

