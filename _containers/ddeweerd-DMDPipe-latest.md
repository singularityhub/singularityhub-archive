---
id: 15633
name: "ddeweerd/DMDPipe"
branch: "main"
tag: "latest"
commit: "56c31f2a0b4c8ac946440ae1a6cd2b19ec9d488c"
version: "273042865af692572e03a9a73ebd5fb718898720d30b112c1ecdaf36beb0bb84"
build_date: "2021-04-16T09:15:31.895Z"
size_mb: 817.73046875
size: 857452544
sif: "https://datasets.datalad.org/shub/ddeweerd/DMDPipe/latest/2021-04-16-56c31f2a-27304286/273042865af692572e03a9a73ebd5fb718898720d30b112c1ecdaf36beb0bb84.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ddeweerd/DMDPipe/latest/2021-04-16-56c31f2a-27304286/
recipe: https://datasets.datalad.org/shub/ddeweerd/DMDPipe/latest/2021-04-16-56c31f2a-27304286/Singularity
collection: ddeweerd/DMDPipe
---

# ddeweerd/DMDPipe:latest

```bash
$ singularity pull shub://ddeweerd/DMDPipe:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: rocker/r-base

%runscript




%files

%environment

%labels

%post
apt-get update

export DEBIAN_FRONTEND=noninteractive

apt-get -qq install -y --no-install-recommends \
       libgsl-dev \
       python3 \
       python3-pip \
       build-essential \
       r-base \
       gfortran \
       libcurl4-openssl-dev \
       libssl-dev \
       libxml2-dev \
       libxslt-dev \
       python3-dev \
       git \
       python3-sklearn
       
  

pip install numpy
pip install pandas 
pip install scipy
pip install joblib
pip install networkx

R -e "install.packages('BiocManager', repos = 'http://cran.us.r-project.org')"

R -e "BiocManager::install(c('AnnotationDbi', \
                             'MODA', \
                             'STRINGdb', \
                             'limma', \
                             'devtools', \
                             'org.Hs.eg.db', \
                             'foreach', \
                             'doParallel', \
                             'Rcpp', \
                             'dynamicTreeCut', \
                             'flashClust', \
                             'reticulate', \
                             'plyr', \
                             'parallel', \
                             'igraph', \
                             'WGCNA', \
                             'RSQLite', \
                             'stackoverflow', \
                             'preprocessCore', \
                             'DESeq2', \
                             'edgeR', \
                             'openxlsx', \
                             'ggdendro', \
                             'ggrepel', \
                             'clusterProfiler', \
                             'GEOmetadb', \
                             'argparser'))"

R -e "devtools::install_git(url = 'https://gitlab.com/Gustafsson-lab/MODifieR.git')"

R -e "devtools::install_github('jpvert/tigress')"
R -e "BiocManager::install('minet')"
R -e "install.packages('tidyverse')"



R -e "devtools::install_git(url = 'https://github.com/ddeweerd/ComhubbeR.git')"
```

## Collection

 - Name: [ddeweerd/DMDPipe](https://github.com/ddeweerd/DMDPipe)
 - License: None

