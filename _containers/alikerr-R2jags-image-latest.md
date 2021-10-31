---
id: 9992
name: "alikerr/R2jags-image"
branch: "master"
tag: "latest"
commit: "0a276cfe4801bdcb17fa160176c6c009934ceaba"
version: "2e31700da27566eba46a44ad18181927"
build_date: "2019-06-23T23:32:49.262Z"
size_mb: 1484
size: 439549983
sif: "https://datasets.datalad.org/shub/alikerr/R2jags-image/latest/2019-06-23-0a276cfe-2e31700d/2e31700da27566eba46a44ad18181927.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/alikerr/R2jags-image/latest/2019-06-23-0a276cfe-2e31700d/
recipe: https://datasets.datalad.org/shub/alikerr/R2jags-image/latest/2019-06-23-0a276cfe-2e31700d/Singularity
collection: alikerr/R2jags-image
---

# alikerr/R2jags-image:latest

```bash
$ singularity pull shub://alikerr/R2jags-image:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From:  rocker/r-ver:latest

%post
        apt-get update
        apt-get install -y libssl-dev libsasl2-dev jags   autoconf automake
        apt-get install -y curl wget libudunits2-dev bash libicu-dev libeigen3-dev
        apt-get install -y gcc-multilib g++-multilib
        # generic R packages
        R -e "install.packages('ggplot2')"
        R -e "install.packages('tidyr')"
        R -e "install.packages('stringr')"
        R -e "install.packages('data.table')"
        R -e "install.packages('reshape2')"
        R -e "install.packages('digest')"
        R -e "install.packages('lattice')"
        R -e "install.packages('colorspace')"
        R -e "install.packages('labeling')"
        R -e "install.packages('mvtnorm')"       
        #R2Jags
        R -e "install.packages('boot')"
        R -e "install.packages('coda')"
        R -e "install.packages('rjags')"
        R -e "install.packages('dclone')"
        R -e "install.packages('R2jags')"
        #R2OpenBUGS
        wget http://pj.freefaculty.org/Ubuntu/15.04/amd64/openbugs/openbugs_3.2.3.orig.tar.gz
        tar xzf openbugs_3.2.3.orig.tar.gz
        cd openbugs-3.2.3
        ./configure
        make && make check && make install
        R -e "install.packages('R2OpenBUGS')"
        #HPC directories just in case
        mkdir /global
        mkdir /global/scratch
        mkdir /scratch
        mkdir /project

%run
        R --version
```

## Collection

 - Name: [alikerr/R2jags-image](https://github.com/alikerr/R2jags-image)
 - License: None

