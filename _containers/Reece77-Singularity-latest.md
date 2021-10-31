---
id: 10626
name: "Reece77/Singularity"
branch: "master"
tag: "latest"
commit: "916997f606ac86881bca54fb7c024174c1019057"
version: "d193970c6bd7e1d97a0c455f10f60f8e"
build_date: "2019-08-21T17:49:21.591Z"
size_mb: 5261.0
size: 1903931423
sif: "https://datasets.datalad.org/shub/Reece77/Singularity/latest/2019-08-21-916997f6-d193970c/d193970c6bd7e1d97a0c455f10f60f8e.sif"
url: https://datasets.datalad.org/shub/Reece77/Singularity/latest/2019-08-21-916997f6-d193970c/
recipe: https://datasets.datalad.org/shub/Reece77/Singularity/latest/2019-08-21-916997f6-d193970c/Singularity
collection: Reece77/Singularity
---

# Reece77/Singularity:latest

```bash
$ singularity pull shub://Reece77/Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
IncludeCmd: yes

%environment
  R_VERSION=3.6.1
  export R_VERSION
  R_CONFIG_DIR=/etc/R/
  export R_CONFIG_DIR
  export LC_ALL=C
  export PATH=$PATH
 
  RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

%labels
  Author Reece DeHaan
  Version v0.0.4
  R_Version 3.6.1
  build_date 2019 Aug 14
  R_bioconductor True

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"

%post
  apt-get update
  apt-get install -y apt-transport-https apt-utils software-properties-common
  apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

  #add CRAN/Ubuntu repo, add key, then refresh
   apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
   apt-add-repository "deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/"
   apt-get update

  apt-get install -y wget nano
  apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 curl
  apt-get install -y gcc fort77 aptitude
  aptitude install -y g++
  aptitude install -y xorg-dev
  aptitude install -y libreadline-dev
  aptitude install -y gfortran
  gfortran --version
  apt-get install -y libssl-dev libxml2-dev libpcre3-dev liblzma-dev libbz2-dev libcurl4-openssl-dev 
  apt-get install -y libhdf5-dev hdf5-helpers libmariadb-client-lgpl-dev

  apt-get install -y r-base r-base-dev
  
  cd /tmp/
  wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
  bash /tmp/Anaconda3-2019.07-Linux-x86_64.sh -b  
  eval "$(/root/anaconda3/bin/conda shell.bash hook)"
  conda install -c conda-forge umap-learn
  conda clean --packages -y
  
  R --version
  
  # installing packages from cran
  R --slave -e 'install.packages("devtools",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("dplyr",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("rhdr5",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("Seurat",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("Matrix.utils",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("SingleCellExperiment",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("tidyverse",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("ggplot2",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("SingleR",repos="https://cran.rstudio.com/")'
  R --slave -e 'install.packages("future",repos="https://cran.rstudio.com/")'
```

## Collection

 - Name: [Reece77/Singularity](https://github.com/Reece77/Singularity)
 - License: None

