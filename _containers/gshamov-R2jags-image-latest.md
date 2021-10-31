---
id: 9962
name: "gshamov/R2jags-image"
branch: "master"
tag: "latest"
commit: "1f0b9c35a00634f6801c99e3c9dacc04aeb84fa7"
version: "1cfb78dc84ef251332c429002a1001ba4682d2aa773d7278a6560f7b0a830692"
build_date: "2020-10-22T15:26:54.971Z"
size_mb: 444.8046875
size: 466411520
sif: "https://datasets.datalad.org/shub/gshamov/R2jags-image/latest/2020-10-22-1f0b9c35-1cfb78dc/1cfb78dc84ef251332c429002a1001ba4682d2aa773d7278a6560f7b0a830692.sif"
url: https://datasets.datalad.org/shub/gshamov/R2jags-image/latest/2020-10-22-1f0b9c35-1cfb78dc/
recipe: https://datasets.datalad.org/shub/gshamov/R2jags-image/latest/2020-10-22-1f0b9c35-1cfb78dc/Singularity
collection: gshamov/R2jags-image
---

# gshamov/R2jags-image:latest

```bash
$ singularity pull shub://gshamov/R2jags-image:latest
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

%runscript
        R --version
```

## Collection

 - Name: [gshamov/R2jags-image](https://github.com/gshamov/R2jags-image)
 - License: None

