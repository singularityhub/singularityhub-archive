---
id: 7851
name: "merckey/Singularity"
branch: "master"
tag: "chipqc"
commit: "57a3225fcab51c2f90003bf2277b970512761a5c"
version: "7c0e42d5b51eb2f9e7f97d3847d0c4ee"
build_date: "2019-03-20T08:24:17.307Z"
size_mb: 1831
size: 719892511
sif: "https://datasets.datalad.org/shub/merckey/Singularity/chipqc/2019-03-20-57a3225f-7c0e42d5/7c0e42d5b51eb2f9e7f97d3847d0c4ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/merckey/Singularity/chipqc/2019-03-20-57a3225f-7c0e42d5/
recipe: https://datasets.datalad.org/shub/merckey/Singularity/chipqc/2019-03-20-57a3225f-7c0e42d5/Singularity
collection: merckey/Singularity
---

# merckey/Singularity:chipqc

```bash
$ singularity pull shub://merckey/Singularity:chipqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/r-ver:3.5.2

%labels
    AUTHOR merckey@gmail.com
    Name  ChIPQC
    Maintainer "JL" 

%environment
    export PATH=/usr/local/bin:/usr/local/:/usr/local/ngsplot-2.63/bin:$PATH
    export NGSPLOT=/usr/local/ngsplot-2.63/

%post
    apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y \
        build-essential \
        ca-certificates \
        wget \
        gcc \
        git \
        libpq-dev \
        make \
        python-pip \
        python2.7 \
        python2.7-dev \
        ssh \
        libxml2-dev \
        libssl-dev \
        curl \
        zlib1g-dev \
        libcurl4-openssl-dev \
        && apt-get autoremove \
        && apt-get clean

    R -q -e 'install.packages(c("doMC"), repos = "https://cloud.r-project.org/", dep=T)'
    R -q -e 'install.packages(c("Rcpp"), repos = "https://cloud.r-project.org/", dep=T)'
    R -q -e 'install.packages(c("caTools"), repos = "https://cloud.r-project.org/", dep=T)'
    R -q -e 'install.packages(c("BiocManager"), repos = "https://cloud.r-project.org/", dep=T)'
    R -q -e 'install.packages(c("optparse"), repos = "https://cloud.r-project.org/", dep=T)'

    R -q -e 'source("http://bioconductor.org/biocLite.R")' -e 'biocLite( "BSgenome" )'
    R -q -e 'source("http://bioconductor.org/biocLite.R")' -e 'biocLite( "ShortRead" )'
    R -q -e 'BiocManager::install("ChIPQC", version = "3.8")'




    cd /tmp/ && wget https://github.com/shenlab-sinai/ngsplot/archive/2.63.zip && \
    unzip 2.63.zip && mv ngsplot-2.63/ /usr/local/ && cd /usr/local/ngsplot-2.63/

    # cd /usr/local/ngsplot-2.63/database && \
    # wget https://dl.dropboxusercontent.com/s/6pybll8uhjjfc4v/ngsplotdb_mm10_75_3.00.tar.gz && \
    # /usr/local/ngsplot-2.63/ngsplotdb.py -y install ngsplotdb_mm10_75_3.00.tar.gz
```

## Collection

 - Name: [merckey/Singularity](https://github.com/merckey/Singularity)
 - License: None

