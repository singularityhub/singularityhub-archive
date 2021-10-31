---
id: 12421
name: "regicor/mofa"
branch: "master"
tag: "latest"
commit: "94b20426fa45abf640c2bbe51031057a544ac801"
version: "f1e61636da66f5f2329e2159f0ae0433"
build_date: "2020-03-05T10:54:51.767Z"
size_mb: 1687.0
size: 650539039
sif: "https://datasets.datalad.org/shub/regicor/mofa/latest/2020-03-05-94b20426-f1e61636/f1e61636da66f5f2329e2159f0ae0433.sif"
url: https://datasets.datalad.org/shub/regicor/mofa/latest/2020-03-05-94b20426-f1e61636/
recipe: https://datasets.datalad.org/shub/regicor/mofa/latest/2020-03-05-94b20426-f1e61636/Singularity
collection: regicor/mofa
---

# regicor/mofa:latest

```bash
$ singularity pull shub://regicor/mofa:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:18.04

%post
    # Installing ubuntu dependencies
    apt-get update
    apt-get install -y apt-utils
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
    apt-get install -y software-properties-common
    apt-get update
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
    apt-get update
    apt-get install -y libcurl4-gnutls-dev libxml2-dev libssl-dev libmariadb-client-lgpl-dev ibglib2.0-dev libcairo2-dev \
    ghostscript libxt-dev 
    # libssh2-1-dev
    # Installing R and python-pip
    apt-get install -y r-base python-pip
    # Installing MOFA python dependencies
    pip install mofapy2
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    # Installing all R packages
    Rscript -e 'r = getOption("repos"); r["CRAN"] = "https://cran.rstudio.com/"; options(repos = r); install.packages(c("devtools","BiocManager"))' 
    # Installing MOFA R package dependencies
    Rscript -e 'r = getOption("repos"); r["CRAN"] = "https://cran.rstudio.com/"; options(repos = r); BiocManager::install(c("MultiAssayExperiment","Biobase","rhdf5","dplyr","reshape2","pheatmap","corrplot","ggplot2","ggbeeswarm","methods","scales","GGally","RColorBrewer","cowplot","ggrepel","doParallel","foreach","reticulate","grDevices","stats","utils"))'
    Rscript -e 'install.packages("devtools", dependencies = TRUE, repos = "https://cran.rstudio.com"); library(devtools); devtools::install_github("bioFAM/MOFA2/MOFA2", build_opts = c("--no-resave-data --no-build-vignettes"))'
%test
    R --version
```

## Collection

 - Name: [regicor/mofa](https://github.com/regicor/mofa)
 - License: None

