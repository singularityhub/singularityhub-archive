---
id: 1428
name: "vfonov/minc-toolkit-containers"
branch: "master"
tag: "base-min"
commit: "c1f3f71b418d09cc953d692e85edf1d09d59d531"
version: "38eda2c70927d208b0180a7006940e19"
build_date: "2018-01-23T02:11:58.295Z"
size_mb: 1653
size: 760971295
sif: "https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/base-min/2018-01-23-c1f3f71b-38eda2c7/38eda2c70927d208b0180a7006940e19.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vfonov/minc-toolkit-containers/base-min/2018-01-23-c1f3f71b-38eda2c7/
recipe: https://datasets.datalad.org/shub/vfonov/minc-toolkit-containers/base-min/2018-01-23-c1f3f71b-38eda2c7/Singularity
collection: vfonov/minc-toolkit-containers
---

# vfonov/minc-toolkit-containers:base-min

```bash
$ singularity pull shub://vfonov/minc-toolkit-containers:base-min
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
    apt-get -y upgrade 
    apt-get install -y \
         bc \
         wget \
         libjpeg8 \
         imagemagick \
         perl \
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
```

## Collection

 - Name: [vfonov/minc-toolkit-containers](https://github.com/vfonov/minc-toolkit-containers)
 - License: None

