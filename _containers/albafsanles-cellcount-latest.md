---
id: 7450
name: "albafsanles/cellcount"
branch: "master"
tag: "latest"
commit: "4300918f6d05a552bba48e8e1cd6b7e34f61f6ca"
version: "13be1ded90c9db3c3df6e49d828c1eed"
build_date: "2019-02-25T20:22:55.882Z"
size_mb: 2374
size: 1218945055
sif: "https://datasets.datalad.org/shub/albafsanles/cellcount/latest/2019-02-25-4300918f-13be1ded/13be1ded90c9db3c3df6e49d828c1eed.simg"
url: https://datasets.datalad.org/shub/albafsanles/cellcount/latest/2019-02-25-4300918f-13be1ded/
recipe: https://datasets.datalad.org/shub/albafsanles/cellcount/latest/2019-02-25-4300918f-13be1ded/Singularity
collection: albafsanles/cellcount
---

# albafsanles/cellcount:latest

```bash
$ singularity pull shub://albafsanles/cellcount:latest
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
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("minfi","FlowSorted.Blood.450k"))'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("DEXSeq","impute","wateRmelon","methylumi"))'
Rscript -e 'install.packages(c("gam","Hmisc","devtools","MASS","lmtest","markdown","Cairo","knitr","doParallel","compareGroups","MatrixEQTL","plyr","dplyr","matrixStats","sandwich","ggplot2","glmnet","parallel"))'
Rscript -e 'install.packages("devtools", dependencies = TRUE)'
Rscript -e 'library(devtools); install_github("brentp/celltypes450")'   
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("sva")'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("minfi","FlowSorted.Blood.450k","IlluminaHumanMethylation450kmanifest"))'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("DEXSeq","impute","wateRmelon","methylumi"))'
Rscript -e 'install.packages(c("gam","Hmisc","devtools","MASS","lmtest","markdown","Cairo","knitr","doParallel","compareGroups","MatrixEQTL","plyr","dplyr","matrixStats","sandwich","ggplot2","glmnet","parallel"))'
```

## Collection

 - Name: [albafsanles/cellcount](https://github.com/albafsanles/cellcount)
 - License: None

