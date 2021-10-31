---
id: 9145
name: "albafsanles/cellcount_epic"
branch: "master"
tag: "latest"
commit: "2ccaf90c1ebffcdf65b5069421769d9c0d02794e"
version: "ea859d14b43329d6ae21c1a88a161094"
build_date: "2019-05-18T10:56:40.595Z"
size_mb: 1857
size: 686436383
sif: "https://datasets.datalad.org/shub/albafsanles/cellcount_epic/latest/2019-05-18-2ccaf90c-ea859d14/ea859d14b43329d6ae21c1a88a161094.simg"
url: https://datasets.datalad.org/shub/albafsanles/cellcount_epic/latest/2019-05-18-2ccaf90c-ea859d14/
recipe: https://datasets.datalad.org/shub/albafsanles/cellcount_epic/latest/2019-05-18-2ccaf90c-ea859d14/Singularity
collection: albafsanles/cellcount_epic
---

# albafsanles/cellcount_epic:latest

```bash
$ singularity pull shub://albafsanles/cellcount_epic:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest


%post

apt-get update && apt-get install -y libcurl4-gnutls-dev libxml2-dev libssl-dev libmariadb-client-lgpl-dev ibglib2.0-dev libcairo2-dev ghostscript 
apt-get update && apt-get -y install r-base
apt-get update && apt-get install -y libxt-dev 

Rscript -e 'install.packages("devtools", dependencies = TRUE)'
Rscript -e 'library(devtools); install_github("brentp/celltypes450")'   
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("sva")'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("minfi","FlowSorted.Blood.450k","FlowSorted.Blood.EPIC","IlluminaHumanMethylation450kmanifest", "IlluminaHumanMethylationEPICmanifest"))'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("DEXSeq","impute","wateRmelon","methylumi"))'
Rscript -e 'install.packages(c("gam","Hmisc","devtools","MASS","lmtest","markdown","Cairo","knitr","doParallel","compareGroups","MatrixEQTL","plyr","dplyr","matrixStats","sandwich","ggplot2","glmnet","parallel"))'
```

## Collection

 - Name: [albafsanles/cellcount_epic](https://github.com/albafsanles/cellcount_epic)
 - License: None

