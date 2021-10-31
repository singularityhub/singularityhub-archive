---
id: 12121
name: "regicor/mrna"
branch: "master"
tag: "latest"
commit: "b0c747246fc76c4decc1ce5cd2000b7e276e5c5b"
version: "e5e94bbdefa5e46d73bcbd8622cb70eb"
build_date: "2020-02-28T14:56:08.471Z"
size_mb: 1718.0
size: 764764191
sif: "https://datasets.datalad.org/shub/regicor/mrna/latest/2020-02-28-b0c74724-e5e94bbd/e5e94bbdefa5e46d73bcbd8622cb70eb.sif"
url: https://datasets.datalad.org/shub/regicor/mrna/latest/2020-02-28-b0c74724-e5e94bbd/
recipe: https://datasets.datalad.org/shub/regicor/mrna/latest/2020-02-28-b0c74724-e5e94bbd/Singularity
collection: regicor/mrna
---

# regicor/mrna:latest

```bash
$ singularity pull shub://regicor/mrna:latest
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
    # Installing all R packages
    Rscript -e 'r = getOption("repos"); r["CRAN"] = "https://cran.rstudio.com/"; options(repos = r); install.packages("BiocManager")'
    Rscript -e 'r = getOption("repos"); r["CRAN"] = "https://cran.rstudio.com/"; options(repos = r); BiocManager::install(c("sva","edgeR","limma","oligo","oligoClasses","BiocGenerics","ggplot2","parallel","Biobase","Biostrings","S4Vectors","stats4","IRanges","XVector","pd.huex.1.0.st.v2","genefilter"))'
    Rscript -e 'install.packages("devtools", dependencies = TRUE, repos = "https://cran.rstudio.com"); library(devtools); install_github("brentp/celltypes450")'
    #Rscript -e 'install.packages("BiocManager", repos = "https://cran.rstudio.com/")'
%test
    R --version
```

## Collection

 - Name: [regicor/mrna](https://github.com/regicor/mrna)
 - License: None

