---
id: 15724
name: "GreetDB/test"
branch: "master"
tag: "latest"
commit: "4b0c959dea29c8a2f7ba008ee4b0dee9ad9d08ee"
version: "645838a5bb5eb1fd89b8b6b74a42a868"
build_date: "2021-03-16T18:29:45.722Z"
size_mb: 2251.0
size: 851345439
sif: "https://datasets.datalad.org/shub/GreetDB/test/latest/2021-03-16-4b0c959d-645838a5/645838a5bb5eb1fd89b8b6b74a42a868.sif"
url: https://datasets.datalad.org/shub/GreetDB/test/latest/2021-03-16-4b0c959d-645838a5/
recipe: https://datasets.datalad.org/shub/GreetDB/test/latest/2021-03-16-4b0c959d-645838a5/Singularity
collection: GreetDB/test
---

# GreetDB/test:latest

```bash
$ singularity pull shub://GreetDB/test:latest
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
                             'GEOmetadb'))"

R -e "devtools::install_git(url = 'https://gitlab.com/Gustafsson-lab/MODifieR.git')"

R -e "devtools::install_github('jpvert/tigress')"
R -e "BiocManager::install('minet')"
R -e "install.packages('tidyverse')"


#R -e "devtools::install_git(url = 'https://github.com/ddeweerd/ComhubbeR.git')"
```

## Collection

 - Name: [GreetDB/test](https://github.com/GreetDB/test)
 - License: None

