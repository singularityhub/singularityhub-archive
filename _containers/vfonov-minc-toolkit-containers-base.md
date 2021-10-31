---
id: 1272
name: "vfonov/minc-toolkit-containers"
branch: "master"
tag: "base"
commit: "8c1a10972cf8a3be6440f534365c67787851149d"
version: "e1079b7ec2c9ab822139fca14bb1965d"
build_date: "2020-07-08T22:11:17.432Z"
size_mb: 1654
size: 761143327
sif: "https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/base/2020-07-08-8c1a1097-e1079b7e/e1079b7ec2c9ab822139fca14bb1965d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vfonov/minc-toolkit-containers/base/2020-07-08-8c1a1097-e1079b7e/
recipe: https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/base/2020-07-08-8c1a1097-e1079b7e/Singularity
collection: vfonov/minc-toolkit-containers
---

# vfonov/minc-toolkit-containers:base

```bash
$ singularity pull shub://vfonov/minc-toolkit-containers:base
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

# install basic system packages
%post
    echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" > /etc/apt/sources.list.d/cran.list 
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 
    sed -i 's/$/ universe/' /etc/apt/sources.list 
    apt-get -y update 
    apt-get install -y \
         bc \
         libxi6  \
         libxmu6  \
         wget \
         libjpeg8 \
         imagemagick \
         perl \
         libgl1-mesa-glx \
         libglu1-mesa \
         r-base r-base-dev \
         ed libxml2-dev libcurl4-openssl-dev libssl-dev \
         python-pip python-dev libzmq-dev cython python-cffi python-numpy python-scipy python-matplotlib
    
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
    
    
    # Update R packages 
    Rscript -e 'update.packages(repos="https://cloud.r-project.org",ask=F)'

    # Install additional R packages
    Rscript -e 'install.packages(c("lme4","tidyverse","batchtools","Rcpp","rjson","jsonlite","tidyr","shiny","visNetwork","DT"),repos="https://cloud.r-project.org")'

    Rscript -e 'install.packages(c("gridBase","data.tree"),repos="https://cloud.r-project.org")'

    # scoop
    pip install scoop --no-cache-dir 

    
%labels
    Maintainer Vladimir S. Fonov
    AUTHOR vladimir.fonov@gmail.com
    Version 1.0
    
%help
    Help me. I'm in the container.
```

## Collection

 - Name: [vfonov/minc-toolkit-containers](https://github.com/vfonov/minc-toolkit-containers)
 - License: None

