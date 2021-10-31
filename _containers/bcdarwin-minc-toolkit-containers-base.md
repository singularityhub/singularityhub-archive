---
id: 5763
name: "bcdarwin/minc-toolkit-containers"
branch: "master"
tag: "base"
commit: "df4202ee09dd9a9684472b9a6ab4ad251c3939be"
version: "5eca773d29dbe05fd1b406b11c6b275a"
build_date: "2018-12-01T16:42:26.399Z"
size_mb: 2370
size: 1071468575
sif: "https://datasets.datalad.org/shub/bcdarwin/minc-toolkit-containers/base/2018-12-01-df4202ee-5eca773d/5eca773d29dbe05fd1b406b11c6b275a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bcdarwin/minc-toolkit-containers/base/2018-12-01-df4202ee-5eca773d/
recipe: https://datasets.datalad.org/shub/bcdarwin/minc-toolkit-containers/base/2018-12-01-df4202ee-5eca773d/Singularity
collection: bcdarwin/minc-toolkit-containers
---

# bcdarwin/minc-toolkit-containers:base

```bash
$ singularity pull shub://bcdarwin/minc-toolkit-containers:base
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

# install basic system packages
%post
    apt-get -y update
    apt-get install -y gnupg
    echo "deb http://cran.rstudio.com/bin/linux/ubuntu bionic-cran35/" > /etc/apt/sources.list.d/cran.list 
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 
    sed -i 's/$/ universe/' /etc/apt/sources.list 
    apt-get -y update 
    apt-get install -y \
         bc \
         libxi6  \
         libxmu6 \
         wget \
         gnupg2 \
         libjpeg8 \
         imagemagick \
         perl octave \
         libgl1-mesa-glx \
         libglu1-mesa \
         r-base r-base-dev \
         ed libxml2-dev libcurl4-openssl-dev libssl-dev \
         python-pip python3-pip python-dev python3-dev libzmq3-dev \
         cython python-cffi \
         cython3 python3-cffi \
         locales automake git lsof 

    # update locales
    locale-gen en_US.UTF-8 en_US en_CA.UTF-8 en_CA
    dpkg-reconfigure locales
    
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
    
    # Update R packages 
    Rscript -e 'update.packages(repos="https://cloud.r-project.org",ask=F)'

    # Install additional R packages
    Rscript -e 'install.packages(c("lme4","tidyverse","batchtools","Rcpp","rjson","jsonlite","tidyr","shiny","visNetwork","DT","testthat"),repos="https://cloud.r-project.org",ask=F)'
    Rscript -e 'install.packages(c("rgl", "plotrix", "lmerTest", "qvalue", "testthat", "igraph"),repos="https://cloud.r-project.org",ask=F)'
    Rscript -e 'install.packages(c("gridBase","data.tree"),repos="https://cloud.r-project.org",ask=F)'

    # scoop
    wget https://github.com/vfonov/scoop/archive/master.tar.gz && \
    pip install master.tar.gz --no-cache-dir && \
    pip3 install master.tar.gz --no-cache-dir && \
    rm -rf master.tar.gz     

    
%labels
    Maintainer Vladimir S. Fonov
    AUTHOR vladimir.fonov@gmail.com
    Version 1.1
    
%help
    Base image for minc-toolkit, based on Ubuntu 18.04. Contains only standard and 3rd party packages
```

## Collection

 - Name: [bcdarwin/minc-toolkit-containers](https://github.com/bcdarwin/minc-toolkit-containers)
 - License: None

