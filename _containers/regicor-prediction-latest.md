---
id: 12703
name: "regicor/prediction"
branch: "master"
tag: "latest"
commit: "647543d85cbaa81925efefda56a98751c36cb305"
version: "bdd6563c51382aeaa1d9ee76a31264c5"
build_date: "2020-05-12T15:24:28.458Z"
size_mb: 1075.0
size: 376344607
sif: "https://datasets.datalad.org/shub/regicor/prediction/latest/2020-05-12-647543d8-bdd6563c/bdd6563c51382aeaa1d9ee76a31264c5.sif"
url: https://datasets.datalad.org/shub/regicor/prediction/latest/2020-05-12-647543d8-bdd6563c/
recipe: https://datasets.datalad.org/shub/regicor/prediction/latest/2020-05-12-647543d8-bdd6563c/Singularity
collection: regicor/prediction
---

# regicor/prediction:latest

```bash
$ singularity pull shub://regicor/prediction:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:18.04

%post
    # Installing ubuntu dependencies
    apt-get update
    apt-get install -y libcurl4-gnutls-dev libxml2-dev libssl-dev libmariadb-client-lgpl-dev ibglib2.0-dev libcairo2-dev \
    ghostscript libxt-dev r-base
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    # Installing all R packagesss
    Rscript -e 'r = getOption("repos"); r["CRAN"] = "https://cran.rstudio.com/"; options(repos = r); install.packages(c("graphics","ggplot2","mvtnorm","cluster","grDevices","png","jpeg","RColorBrewer","Matrix","nnet","methods","splines","stats","utils","lattice","Formula","latticeExtra","ggpubr","survminer","survival","rpart","car","rstatix","survAUC","nricens","Hmisc"))' 
%test
    R --version
```

## Collection

 - Name: [regicor/prediction](https://github.com/regicor/prediction)
 - License: None

